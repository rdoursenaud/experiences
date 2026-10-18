---
title: 'Lenovo ThinkPad Stack Mobile Projector'
date: '2026-10-16'
tags:
  - Rétro-Ingénierie
  - Reverse Engineering
  - Lenovo
  - ThinkPad
  - Stack
  - Projector
  - DLP
  - x86
  - Intel
  - Atom
abbreviations:
  OSINT: Open Source Intelligence
  FRU: Field Replaceable Unit
  FCC: Federal Communications Commission
  EU: European Union
  ID: Identifier
  IC: Integrated Circuit
  SoC: System on Chip
  EC: Embedded Controller
  DLP: Digital Light Processing
  SiP: System in Package
  SDIO: Secure Digital Input Output
  UART: Universal Asynchronous Receiver-Transmitter
  eMMC: embedded MultiMediaCard
  LPDDR: Low Power Dual Data Rate
  USI: Universal Scientific Industrial Co.,Ltd.
  NVRAM: Non Volatile Random Access Memory
---

# Lenovo ThinkPad Stack Mobile Projector

> Pré-rétro-ingénierie par OSINT — identification matérielle complète avant réception.

:::{figure} /images/lenovo-thinkpad-stack-mobile-projector-overview.jpg
:alt: Lenovo ThinkPad Stack Mobile Projecter overview
:::

:::{figure} /images/lenovo-thinkpad-stack-mobile-projector-connectors.jpg
:alt: Lenovo ThinkPad Stack Mobile Projecter overview
:::

## Identification

| Champ | Valeur |
| --- | --- |
| FRU | `03X7217` (variante EU) |
| FCC ID | `A5MM123` (IC : `5903G-M123`) |
| Grantee | `A5M` (Lenovo) |
| Product code | `M123` (ThinkPad Stack Projector) |
| Android codename | `pj_stack_acc` |

> Recherche FCC : https://www.fcc.gov/oet/ea/fccid

## Plateforme

| Composant | Référence | Notes |
| --- | --- | --- |
| SoC | Intel Cherry Trail `Z8550` (x86) | Atom x5 quad-core, sSpec `SR2KH` |
| GPU | Intel HD Graphics Gen8 | Pilotable par `i915` |
| RAM | 2 Go LPDDR3 1600 | Maximum Z8550 : 8 Go |
| Stockage | eMMC SanDisk 16 Go | Layout à déterminer |
| EC / puces support | ITE ×2 | À confirmer |

> https://www.intel.com/content/www/us/en/products/sku/93360/intel-atom-x5z8550-processor-2m-cache-up-to-2-40-ghz/specifications.html

### Radio

Module **USI `WM-BAC-BM-19`** basé sur un SiP Broadcom `BCM43455` (alias Cypress/Infineon `CYW43455`, nom de code « Cobra »).

| Fonction | Bus | Driver Linux | À dumper |
| --- | --- | --- | --- |
| Wi-Fi | SDIO | `brcmfmac` | `brcmfmac43455-sdio.bin` + `brcmfmac43455-sdio.txt` (NVRAM) |
| Bluetooth | UART | `hciattach` | `BCM4345C0.hcd` |

> ⚠️ Le NVRAM est propre à l’appareil (calibrage RF) : à extraire intact du dump.

- Fabricant radio : <https://www.usiglobal.com/tw>

### Affichage

**DLP : Texas Instruments Pico DLP**. Modèle exact à déterminer (logo DLP visible sur la puce, à l’opposé du module radio). C’est le seul composant sans pilote Linux natif à ma connaissance.

## Logiciel

Voir [Lenovo ThinkPad Stack Assistant](2026-10-16-lenovo-thinkpad-stack-assistant).

## Firmware 

*Depuis [archive.org](https://archive.org/details/lenovothinkpadstackdocumentation), à valider dès réception du produit*

 Champ | Valeur | Intérêt port |
| --- | --- | --- |
| Projector Model | `M123` | recoupe le FCC `A5MM123` |
| Kernel | `3.14.55x86_64` | **x86_64 confirmé** — branche alignée sur Android-x86 6.0 |
| Android | `6.0.1` | base à reproduire |
| System Version | `2.2.5` | référence OTA projecteur |
| Release | `g_pi_stack-user 6.0.1` | build user, non-root d’origine |
| Build | `majian@build.local`, 2017-08-09 | toolchain / date de compile |

> Le `3.14.55x86_64` valide la cible **Android-x86 Marshmallow** comme étant la plus proche.

## Cibles OS envisagées

- **LineageOS** — pas de branche x86 maintenue
- **Android-x86** — modernité + pilotes DLP/SST conservés nativement
- **Arch Linux** — DLP interne à porter

:::{note} Previous art
https://www.reddit.com/r/NixOS/comments/1ultoc5/booted_nixos_on_the_incredibly_obscure_thinkpad/
:::

---

*Le seul front ouvert est la référence exacte du contrôleur DLP TI. Tout le reste est identifié, documenté et de difficulté bornée.*
