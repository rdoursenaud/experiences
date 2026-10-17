---
title: 'Lenovo ThinkPad Stack Router'
date: '2026-10-16'
tags:
  - Rétro-Ingénierie
  - Reverse Engineering
  - Lenovo
  - ThinkPad
  - Stack
  - Router
  - Realtek
  - MIPS
  - GPL
abbreviations:
  SoC: System on Chip
  SDK: Software Development Kit
  OTA: Over-The-Air
  RCE: Remote Code Execution
  CGI: Common Gateway Interface
  GPL: GNU General Public License
  uClibc: micro C Library
  MTD: Memory Technology Device
  HAL: Hardware Abstraction Layer
  RF: Radio Frequency
  MIPS: Microprocessor without Interlocked Pipeline Stages
  DLP: Digital Light Processing
  procfs: Process Filesystem
  NOR: NOR flash memory
  AP: Access Point
  TR-069: Technical Report 069 (CWMP)
  MIB: Management Information Base
  PSK: Pre-Shared Key
---

# Lenovo ThinkPad Stack Router

> Rétro-ingénierie du module routeur du ThinkPad Stack — extraction firmware, accès root, source GPL publiée, portage envisagé.

:::{figure} /images/lenovo-thinkpad-stack-router.png
:alt: Lenovo ThinkPad Stack Router + Disk (Third)
:::

Ressources :
- https://www.thinkwiki.org/wiki/ThinkPad_Stack

## Démontage

*Ouverture du module routeur (18/02/2024).*

[Album photos](https://photos.app.goo.gl/5F57PyhDLT7txtCX6)

| Poste | Marquage | Rôle |
| --- | --- | --- |
| SoC / radio | Realtek `RTL8881AN` | MIPS + radio 5 GHz |
| Radio 2,4 GHz | Realtek `RTL8192ER` | 2ᵉ radio discrète 802.11n 2,4 GHz |
| EC | ITE `IT8586E` | contrôleur empilement / LEDs / charge |
| Flash | Winbond `25Q128BVSG` | NOR 128 Mbit = **16 Mio** |
| RAM | Micron `MT4D161664A` | DDR SDRAM **128 Mio** |
| Régulation | Silergy `SY8008` | régulateur DC-DC |
| Ethernet | Bothhand `NS0014 LF` | module d’isolation 10/100 BASE TX |

**Ce que les marquages corrigent ou confirment :**

- **EC** : la puce est une **IT8586E**. Le `ITE8566` du firmware et du code source GPL est le *nom du driver*, pas la référence silicium.
- **Dual-band** : il n’est pas porté par le seul `RTL8881A`. Une radio **RTL8192ER** discrète (2,4 GHz) complète le SoC (5 GHz) — ce qui explique la scission `mib_rf` (2,4 GHz) / `mib_rf_ac` (5 GHz) et l’attribution `wlan0` = 5 GHz, `wlan1` = 2,4 GHz.
- **Flash / RAM** : la NOR Winbond 16 Mio et la DDR 128 Mio recoupent exactement le layout MTD et le `MemTotal` relevés en fonctionnement.

**Connecteur pogo** (repérage au multimètre) : **USB** + **3V3** + **5V** + **GND**.

## Identification

Nom de projet interne : `Poker`
Preuve : path de build `…/poker-1.1.3.4/Poker/rtl819x/linux-2.6.30`

| Champ | Valeur |
| --- | --- |
| Rôle | Module routeur du ThinkPad Stack (gateway réseau + partage HDD) |
| Hostname | `lenovo-stack` |
| Firmware | `1.1.3.4` (build 2016-07-07 recovery / 2016-03-24 OTA) |
| EC | `0.1.0.2` |
| Gateway IP | `192.168.33.254` |
| Serveur HTTP | Boa v0.94, User: `root` |

## Connectique pogo — empilement des modules

Les autres modules du Stack (powerbank, disque dur, enceinte, projecteur) se raccordent par connecteur pogo. Le routeur **n’a pas de batterie propre**, pourtant son EC (`/proc/ite8566_PowerSource`, `ite8566_RelativeStateOfChg`) rapporte un état de charge — il ne peut donc lire que la batterie d’un **module empilé**. L’ITE8566 du routeur est ainsi probablement le *négociateur d’empilement* (alim + charge), pas un simple contrôleur de LEDs.

| Plan | Rôle | Statut |
| --- | --- | --- |
| Alimentation | rails **3,3 V + 5 V** | **mesurés** |
| Données | **USB** (Disque dur) | **observé** |
| Énergie | état de charge du powerbank lu par l’EC du routeur | **inférence forte** (le routeur rapporte une charge qu’il ne possède pas) |
| Bus de négociation | I2C/SMBus dédié vs ligne simple (présence + tension) | **à lever au MSO** |

> **Pas de bus vidéo.** Le projecteur est un PC x86 autonome (Intel Z8550, son propre GPU) qui génère sa propre image ; le pilotage inter-modules passe par le **réseau** (Wi-Fi, JSON), pas par les broches. Les pogo portent l’énergie et l’USB, à priori rien d’autre.

:::{note} Validation — mesure au MSO
Le code source GPL ne couvre que la liaison interne SoC↔EC (`ite8566_i2c.c`, I2C simulé sur GPIO B4/B5), jamais ce qui arrive sur les broches. À trancher au multimètre/scope :
- **I2C/SMBus** → couple horloge+données qui « jappe » à l’insertion.
- **Ligne simple** → un seul rail qui monte en RC, sans horloge.
- **USB** → bursts différentiels + chirp de hot-plug.
Déclencher sur le front d’insertion, mémoire profonde : l’échange de négociation dure quelques ms et ne se produit qu’une fois.
:::

## Plateforme

| Composant | Référence | Notes |
| --- | --- | --- |
| SoC | Realtek `RTL8881A` v1.0 (`chipVersion: RTL8881AN`) | MIPS, dual-band 2,4 + 5 GHz (WiFi intégré), intPA, 2T2R |
| Flash | **NOR 16 Mio** (`erasesize` 0x1000) | pas de NAND — pas de bad blocks, pas d’ECC |
| RAM | **128 Mio** | `MemTotal` 117 080 kio (~114 Mio dispo) — large marge pour le port |
| SDK | Realtek SDK `v3.4.6.4-r23198` | rtl819x, fastpath |
| Kernel | `2.6.30.9` | build `software_release_1.1.3.4`, gcc 4.4.5, image **raw** (pas uImage) |
| C library | uClibc `0.9.30.3` | |
| EC (LED/Projecteur)| ITE `ITE8566` | via `/proc/ITE8566_io`, `/proc/ite8566_*` |

> Le RTL8881A est un SoC MIPS à WiFi intégré — pas un RTL8196/8197 générique. C’est ce qui exclut OpenWrt.
> Le NIC Ethernet interne est rapporté comme `8196C` par le driver (`Probing RTL8186… chip name: 8196C`) — même IP interne, pas une puce séparée.

## Logiciel

Voir [Lenovo ThinkPad Stack Assistant](2026-10-16-lenovo-thinkpad-stack-assistant).

## Flash — layout réel (dump MTD)

Trois partitions MTD sur la NOR 16 Mio :

| MTD | Nom | Taille | Contenu |
| --- | --- | --- | --- |
| `mtd0` | `boot+cfg+linux` | 2,3 Mio | header Realtek + LZMA kernel+initrd |
| `mtd1` | `root fs` | 10,2 Mio | **SquashFS v4.0 LZMA** (837 inodes, ~4,5 Mio réels) |
| `mtd2` | `jffs2` | 4,0 Mio | overlay rw (`/var` monté) — config persistante |

```
mtd0: 00240000 00001000 "boot+cfg+linux"
mtd1: 009c0000 00001000 "root fs"
mtd2: 00400000 00001000 "jffs2"
```

`/proc/cmdline` : `console=ttyS0,115200 root=/dev/mtdblock1 cgroup_enable=memory` → le rootfs est `mtd1`, monté directement en SquashFS (pas de pivot initrd).

Dans `mtd0`, deux LZMA : un petit blob à `0x1B00` (= **boot monitor Realtek**, gère recovery/OTA bas niveau — chaînes `Jump to image start=0x%x`, layout flash) et le gros à `0x42818` (= kernel + initrd, 4,3 Mio décompressés). Les offsets diffèrent du conteneur OTA (`0x2818`) : ici on est sur la partition crue, pas le wrapper `fw.bin`.

### Extraction

```bash
# rootfs (mtd1) — SquashFS LZMA standard, unsquashfs natif suffit
binwalk --extract mtd1.bin          # ou unsquashfs -d rootfs mtd1.bin

# kernel (mtd0) — LZMA à 0x42818
binwalk --extract mtd0.bin          # decompressed.bin @ 42818 = kernel raw

# jffs2 (mtd2) — NE PAS parser offline (voir plus bas)
```

> **jffs2** : le dump offline est piégeux (jefferson force le mauvais endianness, je_tools non packagé sur Arch). Le magic `19 85 20 03` est **little-endian**. La méthode fiable : `/var` est déjà monté rw sur le box → on sert les fichiers via Boa, pas de parsing.

## Firmware — conteneurs OTA / recovery

Conteneur `sw_fw.bin` (Source: APK Levono Stack Assistant) et `fw.bin` (Source: OTA réseau), structure identique :

| Offset | Contenu |
| --- | --- |
| `0x0000–0x2817` | Header Realtek (10 264 octets) — conteneur, **pas une signature** |
| `0x2818` | LZMA → kernel `2.6.30.9` + initrd |
| `0x14E022` | SquashFS v4.0 LZMA → rootfs |

### OTA ≠ recovery (même version)

| Source | Build | Rôle |
| --- | --- | --- |
| OTA réseau (`fw.bin`) | 2016-03-24 | poussé par `download.lenovo.com` |
| Recovery APK (`sw_fw.bin`) | 2016-07-07 | embarqué dans le Stack Assistant v2.0.6 |

Le recovery est **3,5 mois plus récent** que l’OTA sous le même numéro `1.1.3.4`. Le `router.cgi` des deux builds a des chaînes **identiques** (aucun patch de sécurité entre les deux) → le header est un conteneur, pas une signature. Un repack custom passe par le POST OTA.

- OTA :
  - http://download.lenovo.com/lenovostack/UpdateInfo.txt
  - Contenu:
    - ```1.1.3.4 http://download.lenovo.com/lenovostack/fw.bin e40361e79be51b83de63e1a5fbb1ac9e```
    - Soit:  `<version> <url> <md5>`
      - **MD5 seul, aucune signature.**

## Accès root

Trivial, confirmé.

- `rcS` lance `telnetd` **inconditionnellement** au boot : `[ -f /bin/telnetd ] && /bin/telnetd&`
- Credentials : **`root:root`** (hash `$1$` cracké en < 1 min sous John).
- Boa tourne en **`User root`** → toute RCE CGI = uid 0.

### Mécanique d’authentification (contre-intuitive)

- **`/bin/login` (busybox) lit `passwd`, pas `shadow`.** Le hash root actif est donc celui de `/var/passwd` (`$1$se4gYKJy$…` = `root`).
- **`/var/shadow` est un leurre** : `rcS` fait `cp /etc/shadow.sample /var/shadow` à chaque boot → son contenu (`$1$KEKJV2R0$…`) est écrasé au boot et ne sert jamais à l’auth.
- **Compte backdoor `IwgfHEmI`** (uid 1000) : `x` dans `passwd` (hash attendu dans `shadow`) mais **absent de `shadow`** → busybox le traite comme un compte **sans mot de passe**. C’est probablement le compte de test usine.

```sh
# Telnet direct (root:root)
telnet 192.168.33.254
```

%```sh
% # RCE via CGI (si telnet muet) → shell root sans auth
% curl -sG http://192.168.33.254/cgi-bin/router.cgi \
%  --data-urlencode method=find_files --data-urlencode path=/ \
%  --data-urlencode 'keyword=x"; telnetd -l /bin/sh; "'
%```

## Configuration persistante — format `COMPCS`

`/var/config.dat` (~9,7 Ko) = blob sérialisé Realtek, **magic `COMPCS`**, **pas compressé** (le `lzma` échoue — c’est un format à table d’offsets little-endian, lisible en `strings`). Les champs texte (`Stackable Router`, `Lenovo`, `admin`, SSID, PSK) sont en clair, entrecoupés de pointeurs d’offset croissants.

```bash
strings -a -t x config.dat | grep -iE 'stack|lenovo|admin|ssid|psk|passw'
```

> Le parseur exact est dans le **source GPL** du `router.cgi` (fonction de lecture de `config.dat`) → format documentable sans rétro-ingénierie aveugle. Pour le port : soit reproduire le parseur, soit remplacer par un store propre.

Le reste de la config live vit dans `/var` (jffs2 monté) : `wpa-wlan0.conf` / `wpa-wlan1.conf` (PSK en clair, `usePassphrase=0`), `passwd`, `wsc-*.conf`.

## WiFi — bandes & procfs

**Attribution des bandes**

| Interface | Bande |
| --- | --- |
| `wlan0` | **5 GHz** |
| `wlan1` | **2,4 GHz** |

Le procfs du driver built-in est **`/proc/wlan0/`** (répertoire de MIBs), **pas** `/proc/rtl8192cd/`. La variante RF se lit dans `mib_rf` :

```sh
cat /proc/wlan0/mib_rf       # → chipVersion: RTL8881AN, MIMO_TR_mode: 2T2R
cat /proc/wlan0/mib_rf_ac    # tables 5 GHz (VHT)
cat /proc/rf_switch          # commutation PA/LNA double bande
```

## Protocole — dispatcher `router.cgi`

Surface applicative unique, **sans authentification** :

```
GET/POST /cgi-bin/router.cgi?method=<action>   (~80 actions)
```

Le CGI lit `QUERY_STRING` → dispatche sur `method=`. Les commandes shell sont construites via `sprintf`/`strcpy` sur des `%s` issus de la requête, puis passées à `system`/`popen`/`execl`. Chaque `%s` non filtré = command injection root.

| `method` | Commande construite | Vecteur |
| --- | --- | --- |
| `find_files` | `find "/var/tmp/usb/%s" -iname "*%s*"` | `path` / `keyword` |
| `get_fileshare_link` | `ln -s %s %s` | `filepath` |
| `set_time_func` | `date -s "%s"` | valeur temps |
| `disk_unlock` | `hdparm --security-unlock %s /dev/%s` | mot de passe disque |
| `set_wps_func` | `iwpriv wlan0 set_mib pin=%s` | PIN WPS |

## Pont projecteur — ITE8566

Le DLP est pilotable **via le routeur**, sans passer par l’Android :

| Interface procfs | Méthode CGI | Rôle |
| --- | --- | --- |
| `/proc/ite8566_PicoProjector` | `proj` | pico projecteur DLP |
| `/proc/ite8566_PowerSource` | `get_ele_status` | batterie / secteur |
| `/proc/ITE8566_io` | — | LED / IO (`LedSet0 1`, `LedSet1 3`) |

> Le routeur commande le projecteur via l’ITE Tech ITE8566. Le DLP n’est pas un front matériel isolé — c’est un fichier procfs du routeur.

## Cloud à neutraliser pour le portage

| Composant | Endpoint | Rôle |
| --- | --- | --- |
| `reachit` | `reachit.lenovo.com` | tunnel de contrôle à distance |
| `sslclient` | `uss.lenovomm.com/authen/1.2/...` | auth compte Lenovo (`lenovoid`) |
| `cwmp` (TR-069) | — | gestion à distance opérateur |
| OTA | `download.lenovo.com/lenovostack/` | mise à jour firmware |

Auth à deux modes : `admin` local OU `lenovoid` cloud (`change_router_login_type`).

> **Sur l’unité analysée, le cloud n’a jamais été appairé** : `/var/private`, `/var/myca`, `/var/cwmp_config`, `/var/cwmp_default` sont vides. L’étape « neutraliser le cloud » se réduit donc à **ne pas embarquer** les binaires (`reachit`, `reachsync`, `sslclient`, `dlserver`, `cwmp`) au recompile — rien à désauthentifier.

## GPL — source complète publiée

Lenovo a livré la **source correspondante intégrale**.  
(Conformité quasi complète, ce qui est asssez rare pour le noter !)

Source : <https://support.lenovo.com/us/en/downloads/DS105234>

| Composant | Statut |
| --- | --- |
| Kernel 2.6.30.9 + patches fastpath Realtek | source ✅ |
| **Driver WiFi RTL8881A** (`rtl8192cd/WlanHAL/RTL8881A/*.c`) | source ✅ — flag `CONFIG_WLAN_HAL_8881A` |
| Userspace (boa, busybox, dropbear, hostapd, iptables, openssl…) | source ✅ |
| `squashfs-tools` (packer du rootfs) | source ✅ |
| Toolchain MIPS (`rsdk-1.5.5` : gcc 4.x + uClibc 0.9.30.3 + binutils) | source ✅ |
| Microcode radio (`WlanHAL/Data/8881A/*.bin`) | blob ❌ — normal, inévitable |

Le driver de **la puce exacte** est en `.c` compilable — 9 fichiers de HAL dédiés RTL8881A (`Hal8881AGen.c`, `Hal8881APhyCfg.c`, `Hal8881ATxDesc.c`…). Le seul binaire restant est le microcode radio, comme tout driver WiFi (iwlwifi, ath9k, rtw89).

:::{warning} Calibrage RF
Le driver embarque ses tables sous le nom interne **RL6310** (= RTL8881A). Variantes : `8881AB` / `8881AM` / `8881AN` / `8881AQ`. Cette unité = **RTL8881AN** (lu dans `/proc/wlan0/mib_rf → chipVersion`), intPA, 2T2R. Table à compiler : `RL6310_MAC_PHY_RF_Parameter_8881AN_v004_20131022`. La variante se lit en **runtime** (`/proc/wlan0/mib_rf`), pas en statique — le driver est **built-in au kernel**, pas de `.ko` séparé (seuls `tntfs.ko` et `scsi_wait_scan.ko` existent en modules). Le recompile patche donc la table **dans le kernel**, pas dans un module.
:::

## Verdict portage

:::{note}
RAM 128 Mio : contrairement aux 32/64 Mio habituels sur ce type de SoC, la marge permet d’embarquer dropbear + uhttpd + un store de config propre sans arbitrage mémoire. Le dump flash complet tient aussi en RAM d’un seul tenant.
:::

- **OpenWrt / LEDE** : non — pas de target RTL8881A, pas de pilote WiFi libre pour ce SoC intégré.
- **NetBSD / BSD, mainline + rtw89** : non — pas de portage, `rtw89` ne couvre pas ce SoC MIPS.
- **Voie réaliste** : **reconstruction complète depuis la source GPL**, toolchain `rsdk-1.5.5` fournie → portage « quasi-libre ».

Cible du portage (dépropriétarisation) :

1. Recompiler kernel + userspace + driver WiFi (reproductibilité byte-level), table **8881AN**.
2. Supprimer le cloud Lenovo : `reachit`, `sslclient`, TR-069 (`cwmp`), OTA (ne pas les embarquer).
3. Remplacer :
    - telnet → dropbear
    - Boa → uhttpd
4. Garder uniquement le microcode radio (incontournable).

**Port du driver rtl8192cd vers OpenWrt moderne** : non viable — le driver est couplé au framework propriétaire net80211 (iwpriv), incompatible avec mac80211/nl80211 d’OpenWrt. La source est nécessaire mais pas suffisante : ce serait une réécriture mac80211 + un target SoC RTL8881A à créer, pas un portage. La source du WiFi sert au *rebuild depuis le SDK* (audit, patch, recompile), pas à un portage OpenWrt.

## Ordre d’attaque

1. **Dump flash** (RCE `find_files` ou telnet `root:root`) → mapper `/proc/mtd`, backup, lire la variante radio (`/proc/wlan0/mib_rf`).
2. **Build toolchain `rsdk-1.5.5`** → recompiler le code source GPL et valider la reproductibilité.
3. **Repack** avec `squashfs-tools` recompilé, en retirant le cloud.

---

*Le routeur est entièrement ouvert : root trivial, source GPL complète, driver WiFi en `.c`. Le seul front restant est le microcode radio — structurel, comme partout. Tout le reste est identifié, documenté et de difficulté bornée.*
