---
title: StarTech TBT3TBTADAP teardown
subtitle: Markings, BOM and component analysis
date: '2026-10-19'
subject: Informatique • IT
tags:
  - Informatique
  - IT
  - Matériel
  - Hardware
  - Teardown
  - Thunderbolt
  - Thunderbolt 3
  - Thunderbolt 2
  - USB-C
  - StarTech
  - Lintes
  - BOM
abbreviations:
  OEM: Original Equipment Manufacturer
  BOM: Bill Of Materials
  MCU: Microcontroller Unit
  NVM: Non-Volatile Memory
  PCB: Printed Circuit Board
  TB: Thunderbolt
  mDP: Mini DisplayPort
  LDO: Low-Dropout Regulator
  eFuse: Electronic Fuse
  UL: Underwriters Laboratories
  TBT3TBTADAP: null
  SRAM: Static Random Access Memory
  FET: Field-Effect Transistor
  MOSFET: Metal-Oxide-Semiconductor Field-Effect Transistor
  PD: Power Delivery
  LQFP: Low-profile Quad Flat Package
  HVQFN: Heat-sink Very-thin Quad Flat No-leads
  WQFN: Thin Quad Flat No-leads
  VSON: Very-thin Small Outline No-leads
  TSSOP: Thin Shrink Small Outline Package
---

Product page: <https://www.startech.com/en-us/usb-hubs/tbt3tbtadap>

:::{figure} /images/startech-tbt3tbtadap-teardown.jpg
:align: center
StarTech TBT3TBTADAP, opened
:::

Full teardown photo set available on
[Google Photos](https://photos.app.goo.gl/2REgMb8gFkeQJQsB8).

:::{card} Related article
[Thunderbolt 3 ↔ Thunderbolt 2 adapters](2026-10-19-thunderbolt-adapters).
:::

## Markings

### Front

```text
TBT3_LEGACY_ADAPTER_MB_V1R1
LEGACY THUNDERBOLT
ADAPTER REV 3:2
Lintes technology.
```

OEM: [Lintes Technology Co., Ltd.](https://en.lintestech.com/)

> The `LEGACY THUNDERBOLT` / `TBT3_LEGACY_ADAPTER` silkscreen confirms Thunderbolt 1
support alongside Thunderbolt 2.

#### Logos

- **Intel** — top right corner
- **Thunderbolt** — bottom right corner

> Denotes an officially licensed Thunderbolt product.

### Back

```text
00007 94V-0
E157836
.1650 RU
```

- `94V-0`: PCB flammability category
- `E157836`: UL iQ Database entry →
  [ZPMV2 / E157836](https://productiq.ulprospector.com/en/profile/202510/zpmv2.e157836?term=ZPMV2&page=9),
  manufacturer [Mutual-Tek Industries Co., Ltd](https://www.mutualtek.com/)
- `.1650`: UL date code, 50th week of 2016

## BOM

### Front

- **CON1**: TB3 embedded host cable (male USB-C to custom connector)
  - [Lintes](https://en.lintestech.com) `1635`: [Slimluster](https://en.lintestech.com/slimluster-connector-and-cable/)?
- **D1, D2, D3**: MCU activity LEDs?
  - `D2`: power good
  - `D1`: USB-C? (blinks when connected to a USB3 port through an adapter, but
    stays lit on a mobile USB-C without Thunderbolt support)
  - `D3`: MCU boot?
- **J1**: MCU test pads?
  - `VCC3V3`, `RST#`, `SWCLK`, `SWDIO`, `GND`, 5 unmarked
- **J2**: [Lotes](https://www.lotes.cc) `1719` — mDP connector for TB2
- **Q1, Q2**: TI [CSD16323](https://www.ti.com/lit/gpn/CSD16323Q3) — N-Channel NexFET Power MOSFET
- **Q3**: Fairchild/onsemi [FDMC7678](https://www.onsemi.com/products/discrete-power-modules/mosfets/low-medium-voltage-mosfets/fdmc7678-l701) — N-Channel PowerTrench MOSFET, 30 V, 19.5 A, 5.3 mΩ
- **U1**: NVM for U2 (Intel firmware?)
  - [Winbond](https://www.winbond.com) `25Q80DVNIG`
    ([W25Q80DV](https://www.winbond.com/hq/support/documentation/downloadV2022.jsp?__locale=en&xmlPath=/support/resources/.content/item/DA00-W25Q80DV.html&level=1)):
    3 V, 8 M-bit serial flash with dual and quad SPI
- **U2**: USB-C controller
  - TI [TPS65982](https://www.ti.com/product/TPS65982) — USB Type-C™ and USB PD controller,
    power switch and high-speed multiplexer
- **U3**: MCU
  - NXP [LPC1114F](https://www.nxp.com/docs/en/data-sheet/LPC111X.pdf) — 32-bit ARM Cortex-M0.
    Package (LQFP48) and `/301` suffix identify the `LPC1114FBD48/301` variant:
    **32 kB flash, 8 kB SRAM**.
    Silkscreen:
    ```text
    LPC1114F
    Q /301
    Z 330.122
    ZSD163110
    ```
- **U4, U5, U7**: misc transistors?
  - Marking `H17K`???
- **U6**: LDO? — VSON-10?
  - Marking: `7UGH` / `397` (pin 1 dot, horizontal bar)
- **U8**: LDO? — WQFN-20
  - Marking: `MPGK` / `9184` / `798` (pin 1 dot, horizontal bar)
- **U9**: TB3 eFuse
  - TI [TPS25942A](https://www.ti.com/product/TPS25942A) — 2.7 V–18 V, 5 A eFuse power MUX with multiple protection modes

### Back

- **UB1**: TB2 eFuse
  - TI [TPS25942A](https://www.ti.com/product/TPS25942A) — 2.7 V–18 V, 5 A eFuse power MUX with multiple protection modes (near the TB2 port)
- **QB1, QB2, QB3, QB4, QB7**: misc transistors
- **QB5, QB6**: unpopulated
- **QB8, QB9**: 2× `7157` P-Channel MOSFET (SI7157DP, TrenchFET Gen III?)

:::{note} Open items
The `?` entries are guessed functions or models. The `???` entries are unresolved markings, not
guesses. The `LPC1114F` flash size is read from the package/suffix, not from a
bootloader query.
:::

## Going further (*Upcoming articles*)

- [Thunderbolt 3 ↔ Thunderbolt 2 adapters](2026-10-19-thunderbolt-adapters)
- Daisy-chaining multiple Thunderbolt devices through mixed adapters and protocol versions
- Thunderbolt device authorization (and my
  [Cosmic desktop applet](https://github.com/rdoursenaud/cosmic-ext-applet-thunderbolt))
- Wordclock synchronization across chained interfaces
- Helping write the missing Linux driver for the PreSonus Quantum Thunderbolt Interfaces
