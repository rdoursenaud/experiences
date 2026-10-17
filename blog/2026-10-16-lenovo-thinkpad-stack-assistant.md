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

---

### Observations critiques pour le portage

1. **Typos à préserver** : `volumn` (pas volume), `accessbility` (pas accessibility). Le projecteur attend ces chaînes exactes.
2. **Doublons de séparateur** : `battery-level` / `battery_level`, `battery-status` / `battery_status`, `bright` / `brightness`. Deux générations de firmware coexistent dans le parser — le port doit accepter les deux ou trancher.
3. **Tout est String** (y compris ce qui devrait être Int/Boolean). Le `getInt`/`getBoolean` du grep lit probablement une *autre* classe (le `SendingThread` ou un handler séparé). Le `ReceivingThread` parse tout en String.
4. **`Full` avec majuscule** : probablement un flag de réponse complète vs incrémentale. À confirmer en écoutant le flux.
5. **Pas de clé `power` / `on` / `off`** : l’extinction passe peut-être par `result` ou par fermeture de socket. À vérifier.
