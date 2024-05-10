Title: Peterson BBS-1 MIDI SysEx format
Date: 2012-08-24 18:57
Category: Informatique // IT
Tags: Matériel, Hardware, Reverse Engineering, MIDI, Peterson, BBS-1
Slug: peterson-bbs-1-midi-sysex-format
Status: published
Lang: en

I just received my brand new metronome and began tinkering with it.  
  
  
The device revolves around an ARM Cortex-M3 platform from ST Electronics
(the STM32F103) and a wireless chip from Microchip (the MRF24J40MA).  
  
  
The USB mode is fortunately class compliant and is seen as a standard
MIDI device.  
  
  
The proprietary BodyBeatSync software emits and receives SysEx data to
the device's MIDI ports.  
  
  
3 startup modes are available:

-   Documented
    -   *Normal* starts the metronome
    -   *Firmware Update* starts in mode waiting for a firmware update
        (press *TEMPO* while powering up or plugging USB)
-   Undocumented
    -   *LCD test* displays the full custom LCD (press *PRESET/MIDI*
        while powering up)

The ultimate goal is to make an application that will run on most FOSS
OSes to load MIDI tempo maps without using the proprietary sync software
(which runs fine in Wine BTW).  
  
  
Here's the data I've been able to collect so far :  

    Normal mode init
    -> F0 00 40 70 01 02 00 20 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 21 F7
    -> F0 00 40 70 01 02 00 22 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 23 00 F7
    -> F0 00 40 70 01 02 00 15 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 16 00 00 00 00 01 00 03 00 02 F7
    -> F0 00 40 70 01 02 00 13 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 14 00 00 00 00 01 00 00 00 00 F7
    -> F0 00 40 70 01 02 00 17 00 00 00 00 F7
    <- F0 00 40 70 01 02 00 18 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    -> F0 00 40 70 01 02 00 04 7F 7F 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 00 00 00 00 42 42 53 01 03 3C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 04 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 23 19 00 05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7
    <- F0 00 40 70 01 02 19 7F 7F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F7

    Firmware update mode init
    -> F0 00 40 70 01 02 00 20 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 21 F7
    -> F0 00 40 70 01 02 00 22 00 00 00 00 F7
    -> F0 00 40 70 01 02 00 15 00 00 00 00 F7
    -> F0 00 40 70 01 02 00 13 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 23 01 F7
    <- F0 00 40 70 01 03 00 16 00 00 00 00 01 00 00 00 00 F7
    <- F0 00 40 70 01 03 00 14 00 00 00 00 01 00 00 00 00 F7

    Firmware update cmd 0
    -> F0 00 40 70 01 02 00 03 00 00 00 00 00 00 00 2D 0B 21 0F 71 54 F7
    Firmware tx
    -> F0 00 40 70 01 02 23 01 00 [ADDR 00-23] 00 00 [DATA] F7
    [...]
    -> F0 00 40 70 01 02 14 01 7F 7F 00 00 [CHECKSUM?] F7
    Firmware ack
    <- F0 00 40 70 01 03 00 02 7F 7F 00 00 F7
    Firmware update cmd 1
    -> F0 00 40 70 01 02 00 03 00 00 00 00 00 [N] 00 2D 0A 7B 78 5A 28 F7
    [loop until finished]

