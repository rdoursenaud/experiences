---
title: 'Lenovo ThinkPad Stack Assistant'
date: '2026-10-16'
tags:
  - Rétro-Ingénierie
  - Reverse Engineering
  - Lenovo
  - ThinkPad
  - Stack
  - Assistant
  - Router
  - Projector
  - Windows
  - iOS
  - Android
abbreviations:
  POST:
  MAC: Medium Access Control
  SSID: Service Set Identifier
  OTA: Over The Air
  JSON: JavaScript Object Notation
  ZIP:
  DES: Data Encryption Standard
  IV: Initialization Vector
  PDB: Program DataBase
  WPF: Windows Presentation Foundation
  mDNS: multicast DNS
---

# Lenovo ThinkPad Stack Assistant

> Analyse et rétro-ingénierie du protocole vers le routeur et le projecteur en vue d’un éventuel portage Linux.

:::{figure} /images/lenovo-thinkpad-stack-assistant.png
:alt: Lenovo ThinkPad Stack Assistant splash screen
Splash screen de la version Microsoft Windows.
:::

## Logiciel

*Configuration et mise à jour du routeur et/ou du projecteur.*

:::{warning} Attention
L’archive ZIP de la version Android distribuée par Lenovo est corrompue.
Voir ci-dessous pour une version complète conservée par archive.org.
:::

- Officiel : [Lenovo ThinkPad Stack Assistant](https://support.lenovo.com/us/en/solutions/ht102018)
- Alternative archivée : https://archive.org/details/lenovothinkpadstackdocumentation

### OS pris en charge

- Microsoft Windows
- iOS (*disparu de l’App Store*)
- Android (`com.lenovo.stackable`, *disparu du Play Store*, *corrompu sur le site offciel*)

### Dernière(s) version(s)

`2.0.6` (Mai/Juin 2017).

### Surface de rétro-ingénierie

- **Hotspot Wi-Fi** : SSID par défaut `StackProjector-XXXX` (XXXX = 4 derniers caractères du MAC), mot de passe affiché par défaut — vecteur d’accès local.
- **Serveur d’OTA** : l’app interroge un serveur de mise à jour interne (projecteur + routeur) — à capturer en trafic réseau.
- **Protocole de pilotage** : l’app pilote le projecteur à distance (Home/Settings, keystone, cast) via le Wi-Fi — à désosser (apktool/jadx).
- **Limite de conception** : projecteur en mono-utilisateur (le HDD tolère jusqu’à 5 connexions) — à lever côté port.

## Protocole

(résolu par désassemblage Android apk v2.0.6)

Découverte : mDNS/DNS-SD, browse `_http._tcp.`, filtre serviceName ∋ "StackProjector",
resolveService → host:port dynamique. IP projecteur statique connue : 192.168.33.100.

- Projecteur (pilotage) : socket TCP, payload JSON.
  Clés vues : keystone_status, keystone_level (String). Cast/settings = autres clés JSON à capturer.
  Timeout applicatif via setSoTimeout.
- Routeur (config + OTA) : HTTP, serveur Boa, gateway 192.168.33.254.
  OTA = POST multipart /boafrm/formUpload (Referer /upload.htm, cookie
  lenovo_user=admin; lenovo_password=<vide>, champ submit-url=/upload.htm)
  → GET /countDownPage.htm (reboot).
- SSH tunnel loopback : 127.0.0.1:2223 et :8988 = ports forwardés locaux,
  PAS la surface réseau du projecteur.
- Partage HDD : http://192.168.33.254/Share_page.html?file= (routeur-relais).

### JSON

Clés du `ReceivingThread` (v2.0.6)

#### Affichage / Projection
| Clé | Type (déduit) | Rôle |
|-----|---------------|------|
| `keystone_status` | String | État correction trapèze |
| `keystone_level` | String | Niveau correction trapèze |
| `bright` | String | Luminosité (ancienne ?) |
| `brightness` | String | Luminosité (nouvelle ?) |
| `input-source` | String | Source active (hdmi/usb/miracast…) |
| `hdmi` | String | État/port HDMI |
| `hdmi_audio` | String | Audio sur HDMI |

#### Audio
| Clé | Type | Rôle |
|-----|------|------|
| `speaker` | String | Volume/haut-parleur interne |
| `volumn` | String | ⚠️ **typo Lenovo** — volume (à reproduire à l’identique) |

#### Batterie / Powerbank
| Clé | Type | Rôle |
|-----|------|------|
| `powerbank` | String | Mode batterie externe |
| `battery-level` / `battery_level` | String | Niveau (%) — deux variantes de séparateur |
| `battery-status` / `battery_status` | String | État (charging/discharging/full) |
| `lowpower` | String | Alerte batterie faible |

#### Stockage / HDD
| Clé | Type | Rôle |
|-----|------|------|
| `hdd` | String | Présence HDD interne |
| `hddname` | String | Nom/volume |
| `hddnum` | String | Nombre partitions/disks |
| `hddtotalcapacity` | String | Capacité totale |
| `hddtype` | String | Type (SSD/HDD/…) |
| `usbhdd` | String | Présence USB |
| `usbhddpath` | String | Mountpoint |
| `usbhddsize` | String | Taille |

#### Cast / Média
| Clé | Type | Rôle |
|-----|------|------|
| `isMiracast` | String | Miracast actif |
| `isPlayer` | String | Lecteur multimédia actif |
| `multiCast` | String | Mode multi-écran |
| `path` | String | Chemin fichier en cours |

#### Réseau / Connectivité
| Clé | Type | Rôle |
|-----|------|------|
| `bluetooth` | String | État BT |
| `isAPState` | String | Mode point d’accès |
| `router` | String | État/rôle routeur |

#### Système / Device
| Clé | Type | Rôle |
|-----|------|------|
| `agent_version` | String | Version agent embarqué |
| `version` | String | Version firmware |
| `name` | String | Nom de l’appareil |
| `language` | String | Langue UI |
| `locale` / `localeid` | String | Locale |
| `country` | String | Pays |
| `accessbility` | String | ⚠️ **typo** — accessibilité |
| `allowNonMarket` | String | Sideloading autorisé |

#### Horloge
| Clé | Type | Rôle |
|-----|------|------|
| `year` `month` `day` `hour` `minute` | String | Date/heure (probablement en réponse à un `check`) |

#### Protocole / Contrôle
| Clé | Type | Rôle |
|-----|------|------|
| `check` | String | Requête de synchronisation d’état |
| `result` | String | Réponse générique |
| `ret` | String | Code retour |
| `Full` | String | ⚠️ majuscule — réponse complète ? |

## Windows — client .NET (`Stack.exe`)

*Version `0.2.0.6`, assembly WPF (`MahApps.Metro`). Rétro-ingénierie via
décompilation native (`ilspy-bin`), les symboles complets étant livrés avec le
binaire.*

:::{note} Symboles en production
`Stack.pdb` est packagé à côté de `Stack.exe`. Un décompilateur .NET reconstruit
donc un quasi-code source (noms de classes, méthodes, variables) sans
désassemblage aveugle — le `.pdb` n'a jamais été retiré du build livré.
:::

### Dépendances embarquées

| Composant | Binaire | Rôle |
| --- | --- | --- |
| SSH | `dropbear.exe`, `dbclient.exe`, `dropbearkey.exe` (+ `cygwin1.dll`) | tunnel/maintenance vers le device |
| Découverte réseau | `Interop.Bonjour.dll` | mDNS/DNS-SD (cf. protocole) |
| Bluetooth | `InTheHand.Net.Personal.dll` | appairage BT |
| QR Code | `ThoughtWorks.QRCode.dll` | provisioning / partage de config |
| Audio | `CoreAudioApi.dll` | sortie audio locale |

:::{warning} Clé SSH factice
`id_rsa.pub` contient une ligne de `1` (`1111…`). Un vrai `id_rsa.pub` commence
par `ssh-rsa AAAA…` (base64). Le fichier sert uniquement à ce que le code ne
plante pas sur une lecture de clé absente — l'authentification SSH n'est jamais
vérifiée.
:::

### Chaîne de chiffrement des fichiers

Deux blobs opaques dans `files/` sont déchiffrés par la classe
`stack.Helper.CSEncryptDecrypt`. Le code décompilé révèle un chiffrement
purement décoratif :

```csharp
public static void DecryptFile(string sInputFilename, string sOutputFilename, string sKey)
{
    DESCryptoServiceProvider DES = new DESCryptoServiceProvider();
    DES.Key = Encoding.ASCII.GetBytes(sKey);   // clé = la string en dur
    DES.IV  = Encoding.ASCII.GetBytes(sKey);   // IV = même string
    // … DES-CBC, padding PKCS7 implicite …
}
```

| Défaut | Constat |
| --- | --- |
| Algorithme | **DES** (1977), clé de 8 octets — cassable par brute-force |
| Clé | **`"ThinkPad"`** — `public const string FirmwareFileKey = "ThinkPad"` (8 caractères = taille exacte d'une clé DES) |
| IV | **égal à la clé** — annule tout l'intérêt du mode CBC |
| Rôle réel | Empêcher un `strings` sur le `.bin`, pas protéger un secret |

:::{note} Vérification par l'entropie
`gjzglx.txt` fait 808 octets = 101 × 8 → multiple de la taille de bloc DES,
cohérent avec du DES-CBC + padding. `binwalk` sur les deux blobs bruts est muet
(aucun magic) : c'est bien du chiffré, pas du compressé.
:::

### Déchiffrement

```python
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

key = b"ThinkPad"                       # IV = Key, comme dans le code
for f in ["files/gjzglx.txt", "files/Moser_rj_gj.bin"]:
    data = open(f, "rb").read()
    plain = unpad(DES.new(key, DES.MODE_CBC, iv=key).decrypt(data), 8)
    open(f.split("/")[-1] + ".dec", "wb").write(plain)
```

| Blob chiffré | Contenu en clair |
| --- | --- |
| `gjzglx.txt` | **Manifeste OTA** (JSON bilingue CN/EN) — `version`/`max-version` `1.1.1.8` + notes de version. Le nom en pinyin et l'extension `.txt` qui ment ne changent rien au contenu. |
| `Moser_rj_gj.bin` | **Conteneur firmware** — identique au `sw_fw.bin` du module routeur : header Realtek (10 264 o) → LZMA (kernel + initrd) → SquashFS v4.0 LZMA. Voir l'article *Routeur* pour l'extraction complète. |

:::{note} Le `.bin` est le recovery, pas l'OTA
`binwalk` sur le `.dec` sort un SquashFS daté **2038-07-18** (horloge RTC dégénérée
au build). C'est le firmware recovery embarqué dans l'installeur — pas la dernière
version OTA, malgré le `max-version` affiché par le manifeste.
:::

### Récapitulatif — sécurité décorative

| Couche | « Protection » |
| --- | --- |
| Clé SSH | `1111…` (factice) |
| Symboles | `.pdb` livré en prod |
| Chiffrement | DES (1977) |
| Clé | `"ThinkPad"` en `const string` |
| IV | Égal à la clé |

Le fil conducteur est le même que côté device (telnet `root:root`, CGI sans
auth, OTA signé MD5 seul) : chaque couche de sécurité existe pour décourager le
curieux, aucune pour arrêter un analyseur.

---

### Observations critiques pour le portage

1. **Typos à préserver** : `volumn` (pas volume), `accessbility` (pas accessibility). Le projecteur attend ces chaînes exactes.
2. **Doublons de séparateur** : `battery-level` / `battery_level`, `battery-status` / `battery_status`, `bright` / `brightness`. Deux générations de firmware coexistent dans le parser — le port doit accepter les deux ou trancher.
3. **Tout est String** (y compris ce qui devrait être Int/Boolean). Le `getInt`/`getBoolean` du grep lit probablement une *autre* classe (le `SendingThread` ou un handler séparé). Le `ReceivingThread` parse tout en String.
4. **`Full` avec majuscule** : probablement un flag de réponse complète vs incrémentale. À confirmer en écoutant le flux.
5. **Pas de clé `power` / `on` / `off`** : l’extinction passe peut-être par `result` ou par fermeture de socket. À vérifier.
