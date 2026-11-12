---
date: '2026-02-12'
keywords:
  - 'Linux'
  - 'Écran tactile'
  - 'Moniteur tactile'
  - 'Tactile screen'
  - 'Tactile monitor'
  - 'Touchscreen'
  - 'Touch monitor'
short_title: 'COSMIC touch monitor'
subject: 'Informatique • IT'
subtitle: 'Gotta touch…'
tags:
  - 'GNU/Linux'
  - 'COSMIC'
  - 'Touchscreen'
---
# Cosmic DE: Map touch device to monitor

:::{hint} Reference
Cosmic [Touchscreen support meta-issue](https://github.com/pop-os/cosmic-epoch/issues/241)
:::

## 1. Get the touch device name(s)

```sh
libinput list-devices
```

## 2. Get the monitor output name(s)

```sh
wlr-randr
```

## 3. Configure `cosmic-comp`

```sh
$EDITOR ~/.config/cosmic/com.system76.CosmicComp/v1/input_devices
```

### Sample config

```rust
{
    "[Touch Device Name]": (
        state: Enabled,
        map_to_output: Some("Monitor-output-name")
        ),
}
```

:::{card} Example
Here's a working configuration for my ThinkPad P51 with an embedded Wacom touchscreen/pen and
an external ThinkVision T24t-20 touchscreen-enabled monitor connected to an nVidia eGPU:
```rust
{
    "Wacom Pen and multitouch sensor Finger": (
        state: Enabled,
        map_to_output: Some("eDP-1")
        ),
    "Wacom Pen and multitouch sensor Pen": (
        state: Enabled,
        map_to_output: Some("eDP-1")
        ),
    "Melfas LGDisplay Incell Touch": (
        state: Enabled,
        map_to_output: Some("Unknown-1")
        ),
}
```
:::
