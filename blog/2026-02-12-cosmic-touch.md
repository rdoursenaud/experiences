---
title: 'Cosmic DE: Map touch device to monitor'
subtitle: 'Gotta touch…'
subject: Informatique // IT
date: '2026-02-12'
tags:
  - COSMIC
  - touchscreen
---

:::{hint} Reference
Cosmic [Touchscreen support meta-issue](https://github.com/pop-os/cosmic-epoch/issues/241)
:::

## 1. Get the touch device name(s)

```sh
libinput list-devices
```

## 2. Get the monitor output name(s)

```sh
wrl-randr
```

## 3. Configure `cosmic-comp`

```sh
$EDITOR ~/.config/cosmic/com.system76.CosmicComp/v1/input_devices
```

### Sample config

```json
{
    "[Touch Device Name]": (
        state: Enabled,
        map_to_output: Some("Monitor-output-name")
        ),
}
```

:::{card}Example
Here's a working configuration for my ThinkPad P51 with an embedded Wacom touchscreen/pen and
an external ThinkVision T24t-20 touchscreen-enabled monitor connected to an nVidia eGPU:
```json
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
