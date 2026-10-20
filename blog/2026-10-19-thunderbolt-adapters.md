---
title: Thunderbolt 3 ↔ Thunderbolt 2 adapters
subtitle: Directionality, power, and the traps nobody documents
date: '2026-10-19'
subject: Informatique • IT
tags:
  - Informatique
  - IT
  - Matériel
  - Hardware
  - Thunderbolt
  - Thunderbolt 2
  - Thunderbolt 3
  - USB-C
  - Apple
  - StarTech
  - Audio
  - PreSonus
  - Quantum
abbreviations:
  BOM: Bill Of Materials
  TB: Thunderbolt
  mDP: Mini DisplayPort
---
### TL;DR

A Thunderbolt 3 ↔ Thunderbolt 2 adapter is **not** a passive cable. It is an
active, **directional** bridge that **never passes power**. Buy it for the wrong
direction and the device simply won't enumerate.

:::::{figure}
:align: center
::::{grid} 1 1 2 2
:::{figure} /images/apple-thunderbolt-adapter.jpg
:alt: Apple adapter
Apple
:::
:::{figure} /images/startech-thunderbolt-adapter.jpg
:alt: StarTech adapter
StarTech
:::
::::
Thunderbolt 3 ↔ Thunderbolt 2 adapters
:::::

### Why direction matters

A Thunderbolt link is asymmetric by nature: one end is the **host** (the
computer), the other end is the **device/peripheral**. An adapter is built to
convert in *one* canonical direction: its *"native"* direction.

| Term | Meaning |
|------|---------|
| TB3 → TB2/TB1 (native) | Host side is TB3 on USB-C, device side is TB2 or TB1 on mDP. The common case. |
| TB2/TB1 → TB3 (reverse) | Host side is TB2 or TB1 on mDP, device side is TB3/USB-C. Only works with a **bidirectional** adapter. |

:::{note} Thunderbolt 3 & USB-C
"USB-C" is a connector, "Thunderbolt 3" is a protocol that happens to share the same connector.
The adapters bridge Thunderbolt, not plain USB even though the connector is the same.
:::

:::{note} Thunderbolt 1/2 & Mini DisplayPort
"Mini DisplayPort" and "Thunderbolt 1/2" share the same physical connector but are
not the same protocol. A Thunderbolt 1/2 host port accepts a Mini DisplayPort display
(passive fallback), but a Mini DisplayPort port cannot carry Thunderbolt — and a
plain Mini DisplayPort cable is not a Thunderbolt cable. The TB1/TB2 end of these
adapters uses that connector shape, which is why it is so often mistaken for a
video output.
:::

:::{note} Thunderbolt 1 support
Thunderbolt 2 is natively backwards-compatible with Thunderbolt 1 (same
connector, same protocol lineage). These adapters therefore support Thunderbolt 1
devices too. On the StarTech this is even printed on the PCB:
`TBT3_LEGACY_ADAPTER` / `LEGACY THUNDERBOLT`.
:::

### Comparison

Only two vendors ever shipped an active Thunderbolt 3 ↔ Thunderbolt 2 adapter.

| Vendor | Model | Direction | Power passthrough | Audio[^audio] |
|---------|-----|-----------|-------------------|----------------|
| Apple | [Thunderbolt 3 (USB-C) to Thunderbolt 2][1] | **Bidirectional** | <span aria-hidden="true">❌</span><span class="sr-only">No</span> | <span aria-hidden="true">✅</span><span class="sr-only">Working</span> |
| StarTech | [TBT3TBTADAP][2] | **Unidirectional**<br/>(TB3 → TB2/TB1 *only*) | <span aria-hidden="true">❌</span><span class="sr-only">No</span> | <span aria-hidden="true">✅</span><span class="sr-only">Working</span> |

[^audio]: The `Audio` column reflects *my* test bench (PreSonus Quantum family). Other Thunderbolt audio interfaces may behave differently depending on their controller.

:::{tip} OS support
Despite being mainly advertised for macOS and Microsoft Windows, these adapters don't require any drivers and work with most hosts and devices including GNU/Linux!
You can even mix and match.
:::

:::{note} Reverse mode caveat
If you need support for a TB2 (or TB1) host → TB3 device,
**only the Apple adapter can do it**. Note that the reverse link is capped (TB1: 10 Gbps, TB2: 20 Gbps) by the host side. Devices needing full TB3 bandwidth (40 Gbps) may not work properly.
:::

### Power

No adapter carries power. A TB device behind one must have its **own** power
supply. Bus-powered TB devices will not work through the bridge.

### StarTech adapter Teardown

:::{figure} /images/startech-tbt3tbtadap-teardown.jpg
:alt: StarTech TBT3TBTADAP teardown
:::

Full teardown photo set available on
[Google Photos](https://photos.app.goo.gl/2REgMb8gFkeQJQsB8).

:::{card} Related article
[StarTech TBT3TBTADAP teardown](2026-10-19-startech-tbt3tbtadap) :
*Markings, BOM and component analysis*.
:::

### Going further (*Upcoming articles*)

This is the prerequisite for the rest of the series:

- Daisy-chaining multiple Thunderbolt devices through mixed adapters and protocol versions
- Thunderbolt device authorization (and my
  [Cosmic desktop applet](https://github.com/rdoursenaud/cosmic-ext-applet-thunderbolt))
- Wordclock synchronization across chained interfaces
- Helping write the missing Linux driver for the PreSonus Quantum Thunderbolt Interfaces

[1]: https://www.apple.com/shop/product/myh93am/a/thunderbolt-3-usb%E2%80%91c-to-thunderbolt-2-adapter
% French market: https://www.apple.com/fr/shop/product/myh93zm/a/adaptateur-thunderbolt-3-usb-c-vers-thunderbolt-2

[2]: https://www.startech.com/en-us/usb-hubs/tbt3tbtadap
% French market: https://www.startech.com/fr-fr/hubs-usb/tbt3tbtadap
