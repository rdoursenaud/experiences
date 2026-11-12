---
abbreviations:
  CSP: Chip Scale Package
  DRAM: Dynamic Random Access Memory
  mDP: mini Display Port
  QLC: Quad-Level Cell
  SLC: Single-Level Cell
  TLC: Triple-Level Cell
  TB: Thunderbolt
date: '2026-11-03'
keywords:
  - 'Thunderbolt SSD'
  - 'TB SSD'
  - 'USB SSD'
  - 'Portable SSD'
  - 'Rugged SSD'
subject: 'Informatique • IT'
tags:
  - 'Layer: Hardware'
  - 'Démontage'
  - 'Teardown'
  - 'Thunderbolt'
  - 'USB 3.0'
  - 'Storage'
  - 'LaCie'
---
# LaCie Rugged Thunderbolt USB 3.0

:::{figure} /images/2026-11-03_lacie_hero.jpg
:alt: LaCie Rugged Thunderbolt USB 3.0 hero shot
:width: 80%
:::
## Discovery

### Thunderbolt

```sh
dmesg
[14198.008005] thunderbolt 0-101: new device found, vendor=0x3 device=0xc
[14198.008008] thunderbolt 0-101: LaCie Rugged THB USB3
```

#### Authorization

```{figure} /images/2026-11-03_lacie_thunderbolt.png
:alt: LaCie Rugged connected over Thunderbolt
:width: 60%
Authorized over Thunderbolt using [my Thunderbolt applet for Cosmic](https://github.com/rdoursenaud/cosmic-ext-thunderbolt).
```

```{tip} CLI
You can also authorize the device using `boltctl`.
```

#### Kernel messages

```sh
dmesg
[   80.781761] pci 0000:0c:00.0: [8086:1549] type 01 class 0x060400 PCIe Switch Upstream Port
[   80.781897] pci 0000:0c:00.0: PCI bridge to [bus 0d-3c]
[   80.781944] pci 0000:0c:00.0:   bridge window [mem 0xd6100000-0xe9efffff]
[   80.781988] pci 0000:0c:00.0:   bridge window [mem 0x2fd2100000-0x2fe1ffffff 64bit pref]
[   80.782028] pci 0000:0c:00.0: enabling Extended Tags
[   80.782352] pci 0000:0c:00.0: supports D1 D2
[   80.782353] pci 0000:0c:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[   80.782814] pci 0000:0c:00.0: Adding to iommu group 20
[   80.783244] pci 0000:0d:00.0: [8086:1549] type 01 class 0x060400 PCIe Switch Downstream Port
[   80.783367] pci 0000:0d:00.0: PCI bridge to [bus 0e]
[   80.783399] pci 0000:0d:00.0:   bridge window [mem 0xd6100000-0xd80fffff]
[   80.783458] pci 0000:0d:00.0:   bridge window [mem 0x2fd2100000-0x2fd40fffff 64bit pref]
[   80.783533] pci 0000:0d:00.0: enabling Extended Tags
[   80.783850] pci 0000:0d:00.0: supports D1 D2
[   80.783850] pci 0000:0d:00.0: PME# supported from D0 D1 D2 D3hot D3cold
[   80.784324] pci 0000:0d:00.0: Adding to iommu group 20
[   80.784499] pci 0000:0c:00.0: PCI bridge to [bus 0d-3c]
[   80.784883] pci 0000:0e:00.0: [1b21:0612] type 00 class 0x010601 PCIe Legacy Endpoint
[   80.785103] pci 0000:0e:00.0: BAR 0 [io  0x0000-0x0007]
[   80.785109] pci 0000:0e:00.0: BAR 1 [io  0x0000-0x0003]
[   80.785115] pci 0000:0e:00.0: BAR 2 [io  0x0000-0x0007]
[   80.785121] pci 0000:0e:00.0: BAR 3 [io  0x0000-0x0003]
[   80.785127] pci 0000:0e:00.0: BAR 4 [io  0x0000-0x001f]
[   80.785133] pci 0000:0e:00.0: BAR 5 [mem 0xd6100000-0xd61001ff]
[   80.785139] pci 0000:0e:00.0: ROM [mem 0x00000000-0x0000ffff pref]
[   80.785718] pci 0000:0e:00.0: Adding to iommu group 20
[   80.785743] pci 0000:0d:00.0: PCI bridge to [bus 0e]
[   80.786041] pci_bus 0000:06: Allocating resources
[   80.786044] pcieport 0000:09:04.0: bridge window [io  size 0x1000]: can't claim; no address assigned
[   80.786061] pcieport 0000:06:02.0: bridge window [mem size 0x00200000 64bit pref]: can't claim; no address assigned
[   80.786185] pcieport 0000:06:02.0: bridge window [mem 0x00100000-0x000fffff 64bit pref] to [bus 3d] add_size 200000 add_align 100000
[   80.786191] pcieport 0000:06:02.0: bridge window [mem size 0x00200000 64bit pref]: can't assign; no space
[   80.786192] pcieport 0000:06:02.0: bridge window [mem size 0x00200000 64bit pref]: failed to assign
[   80.786194] pcieport 0000:06:02.0: bridge window [mem size 0x00200000 64bit pref]: can't assign; no space
[   80.786195] pcieport 0000:06:02.0: bridge window [mem size 0x00200000 64bit pref]: failed to assign
[   80.786197] pcieport 0000:09:04.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786198] pcieport 0000:09:04.0: bridge window [io  size 0x1000]: failed to assign
[   80.786199] pcieport 0000:09:04.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786200] pcieport 0000:09:04.0: bridge window [io  size 0x1000]: failed to assign
[   80.786202] pci 0000:0c:00.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786202] pci 0000:0c:00.0: bridge window [io  size 0x1000]: failed to assign
[   80.786203] pci 0000:0c:00.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786204] pci 0000:0c:00.0: bridge window [io  size 0x1000]: failed to assign
[   80.786205] pci 0000:0d:00.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786206] pci 0000:0d:00.0: bridge window [io  size 0x1000]: failed to assign
[   80.786207] pci 0000:0d:00.0: bridge window [io  size 0x1000]: can't assign; no space
[   80.786207] pci 0000:0d:00.0: bridge window [io  size 0x1000]: failed to assign
[   80.786209] pci 0000:0e:00.0: ROM [mem 0xd6110000-0xd611ffff pref]: assigned
[   80.786210] pci 0000:0e:00.0: BAR 4 [io  size 0x0020]: can't assign; no space
[   80.786211] pci 0000:0e:00.0: BAR 4 [io  size 0x0020]: failed to assign
[   80.786212] pci 0000:0e:00.0: BAR 0 [io  size 0x0008]: can't assign; no space
[   80.786213] pci 0000:0e:00.0: BAR 0 [io  size 0x0008]: failed to assign
[   80.786214] pci 0000:0e:00.0: BAR 2 [io  size 0x0008]: can't assign; no space
[   80.786214] pci 0000:0e:00.0: BAR 2 [io  size 0x0008]: failed to assign
[   80.786215] pci 0000:0e:00.0: BAR 1 [io  size 0x0004]: can't assign; no space
[   80.786216] pci 0000:0e:00.0: BAR 1 [io  size 0x0004]: failed to assign
[   80.786216] pci 0000:0e:00.0: BAR 3 [io  size 0x0004]: can't assign; no space
[   80.786217] pci 0000:0e:00.0: BAR 3 [io  size 0x0004]: failed to assign
[   80.786218] pci 0000:0e:00.0: BAR 4 [io  size 0x0020]: can't assign; no space
[   80.786219] pci 0000:0e:00.0: BAR 4 [io  size 0x0020]: failed to assign
[   80.786220] pci 0000:0e:00.0: BAR 0 [io  size 0x0008]: can't assign; no space
[   80.786220] pci 0000:0e:00.0: BAR 0 [io  size 0x0008]: failed to assign
[   80.786221] pci 0000:0e:00.0: BAR 2 [io  size 0x0008]: can't assign; no space
[   80.786222] pci 0000:0e:00.0: BAR 2 [io  size 0x0008]: failed to assign
[   80.786223] pci 0000:0e:00.0: BAR 1 [io  size 0x0004]: can't assign; no space
[   80.786223] pci 0000:0e:00.0: BAR 1 [io  size 0x0004]: failed to assign
[   80.786224] pci 0000:0e:00.0: BAR 3 [io  size 0x0004]: can't assign; no space
[   80.786225] pci 0000:0e:00.0: BAR 3 [io  size 0x0004]: failed to assign
[   80.786226] pci 0000:0d:00.0: PCI bridge to [bus 0e]
[   80.786243] pci 0000:0d:00.0:   bridge window [mem 0xd6100000-0xd80fffff]
[   80.786255] pci 0000:0d:00.0:   bridge window [mem 0x2fd2100000-0x2fd40fffff 64bit pref]
[   80.786279] pci 0000:0c:00.0: PCI bridge to [bus 0d-3c]
[   80.786296] pci 0000:0c:00.0:   bridge window [mem 0xd6100000-0xe9efffff]
[   80.786308] pci 0000:0c:00.0:   bridge window [mem 0x2fd2100000-0x2fe1ffffff 64bit pref]
[   80.786343] pcieport 0000:00:1c.4: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786358] pcieport 0000:05:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786372] pcieport 0000:06:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786386] thunderbolt 0000:07:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786400] pcieport 0000:06:01.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786425] pcieport 0000:08:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786453] pcieport 0000:09:01.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786484] nvidia 0000:0a:00.0: Max Payload Size set to  128/ 256 (was  128), Max Read Rq  128
[   80.786516] snd_hda_intel 0000:0a:00.1: Max Payload Size set to  128/ 256 (was  128), Max Read Rq  128
[   80.786548] xhci_hcd 0000:0a:00.2: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786579] nvidia-gpu 0000:0a:00.3: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786606] pcieport 0000:09:02.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786651] xhci_hcd 0000:0b:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786679] pcieport 0000:09:04.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786729] pci 0000:0c:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786792] pci 0000:0d:00.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.786851] pci 0000:0e:00.0: Max Payload Size set to  128/ 256 (was  128), Max Read Rq  128
[   80.786873] pcieport 0000:06:02.0: Max Payload Size set to  128/ 128 (was  128), Max Read Rq  128
[   80.788749] ahci 0000:0e:00.0: SSS flag set, parallel bus scan disabled
[   80.788875] ahci 0000:0e:00.0: AHCI vers 0001.0200, 32 command slots, 6 Gbps, SATA mode
[   80.788878] ahci 0000:0e:00.0: 2/2 ports implemented (port mask 0x3)
[   80.788880] ahci 0000:0e:00.0: flags: 64bit ncq sntf stag led clo pmp pio slum part ccc sxs
[   80.789232] scsi host4: ahci
[   80.789359] scsi host5: ahci
[   80.789451] ata5: SATA max UDMA/133 abar m512@0xd6100000 port 0xd6100100 irq 207 lpm-pol 1 ext
[   80.789458] ata6: SATA max UDMA/133 abar m512@0xd6100000 port 0xd6100180 irq 207 lpm-pol 1 ext
[   81.256916] ata5: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[   81.258336] ata5.00: Model 'CT2000BX500SSD1', rev 'M6CR030', applying quirks: nolpm
[   81.258339] ata5.00: ATA-10: CT2000BX500SSD1, M6CR030, max UDMA/133
[   81.260220] ata5.00: 3907029168 sectors, multi 1: LBA48 NCQ (depth 32), AA
[   81.266588] ata5.00: Features: Dev-Sleep DIPM
[   81.279065] ata5.00: configured for UDMA/133
[   81.281052] scsi 4:0:0:0: Direct-Access     ATA      CT2000BX500SSD1  030  PQ: 0 ANSI: 5
[   81.281388] sd 4:0:0:0: Attached scsi generic sg1 type 0
[   81.281398] sd 4:0:0:0: [sdb] 3907029168 512-byte logical blocks: (2.00 TB/1.82 TiB)
[   81.281404] sd 4:0:0:0: [sdb] Write Protect is off
[   81.281405] sd 4:0:0:0: [sdb] Mode Sense: 00 3a 00 00
[   81.281412] sd 4:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[   81.281428] sd 4:0:0:0: [sdb] Preferred minimum I/O size 512 bytes
[   81.296186]  sdb: sdb1 sdb2
[   81.296311] sd 4:0:0:0: [sdb] Attached SCSI disk
```

#### PCI devices

```sh
lspci
0c:00.0 PCI bridge: Intel Corporation DSL2210 Thunderbolt Controller [Port Ridge 1C 2011]
0d:00.0 PCI bridge: Intel Corporation DSL2210 Thunderbolt Controller [Port Ridge 1C 2011]
0e:00.0 SATA controller: ASMedia Technology Inc. ASM1061/ASM1062 Serial ATA Controller (rev 01)
```

### USB

#### Kernel messages

```sh
dmesg
[ 1629.734675] usb 2-6: new SuperSpeed USB device number 2 using xhci_hcd
[ 1629.745896] usb 2-6: New USB device found, idVendor=059f, idProduct=1075, bcdDevice= 0.01
[ 1629.746317] usb 2-6: New USB device strings: Mfr=2, Product=3, SerialNumber=1
[ 1629.746318] usb 2-6: Product: Rugged THB USB 3.0
[ 1629.746319] usb 2-6: Manufacturer: LaCie
[ 1629.746320] usb 2-6: SerialNumber: 0000NL6B05HS
[ 1629.796099] usbcore: registered new interface driver usb-storage
[ 1629.804363] scsi host4: uas
[ 1629.804481] usbcore: registered new interface driver uas
[ 1629.804967] scsi 4:0:0:0: Direct-Access     LaCie    Rugged THB USB3  1153 PQ: 0 ANSI: 6
[ 1629.806807] sd 4:0:0:0: Attached scsi generic sg1 type 0
[ 1629.807122] sd 4:0:0:0: [sdb] Spinning up disk...
[ 1630.822634] ..ready
[ 1631.853233] sd 4:0:0:0: [sdb] 3907029168 512-byte logical blocks: (2.00 TB/1.82 TiB)
[ 1631.853351] sd 4:0:0:0: [sdb] Write Protect is off
[ 1631.853353] sd 4:0:0:0: [sdb] Mode Sense: 43 00 00 00
[ 1631.853507] sd 4:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[ 1631.877781] sd 4:0:0:0: [sdb] Preferred minimum I/O size 512 bytes
[ 1631.877784] sd 4:0:0:0: [sdb] Optimal transfer size 33553920 bytes
[ 1631.898160]  sdb: sdb1 sdb2
[ 1631.898263] sd 4:0:0:0: [sdb] Attached SCSI disk
```

#### USB device

```sh
lsusb
Bus 002 Device 002: ID 059f:1075 LaCie, Ltd Rugged THB USB 3.0
```

### Partitions

```{figure} /images/2026-11-03_lacie_partitions.png
:alt: Partition layout of the LaCie Rugged drive
:width: 100%
Partition layout.
```

### SMART

#### All

```sh
sudo smartctl -a /dev/sdb
smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.2.15-rt3-arch1-1-rt] (local build)
Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Crucial/Micron Client SSDs
Device Model:     CT2000BX500SSD1
Serial Number:    1943E224BEDD
LU WWN Device Id: 5 00a075 1e224bedd
Firmware Version: M6CR030
User Capacity:    2 000 398 934 016 bytes [2,00 TB]
Sector Size:      512 bytes logical/physical
Rotation Rate:    Solid State Device
Form Factor:      2.5 inches
TRIM Command:     Available
Device is:        In smartctl database 7.5/5706
ATA Version is:   ACS-3 T13/2161-D revision 4
SATA Version is:  SATA 3.3, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Tue Nov  3 19:14:05 2026 CET
SMART support is: Available - device has SMART capability.
SMART support is: Enabled

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
Total time to complete Offline
data collection: 		(  120) seconds.
Offline data collection
capabilities: 			 (0x11) SMART execute Offline immediate.
					No Auto Offline data collection support.
					Suspend Offline collection upon new
					command.
					No Offline surface scan supported.
					Self-test supported.
					No Conveyance Self-test supported.
					No Selective Self-test supported.
SMART capabilities:            (0x0002)	Does not save SMART data before
					entering power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 (  10) minutes.

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAG     VALUE WORST THRESH TYPE      UPDATED  WHEN_FAILED RAW_VALUE
  1 Raw_Read_Error_Rate     0x002f   100   100   000    Pre-fail  Always       -       0
  5 Reallocate_NAND_Blk_Cnt 0x0032   100   100   010    Old_age   Always       -       0
  9 Power_On_Hours          0x0032   100   100   000    Old_age   Always       -       42890
 12 Power_Cycle_Count       0x0032   100   100   000    Old_age   Always       -       109
171 Program_Fail_Count      0x0032   100   100   000    Old_age   Always       -       0
172 Erase_Fail_Count        0x0032   100   100   000    Old_age   Always       -       0
173 Ave_Block-Erase_Count   0x0032   099   099   000    Old_age   Always       -       18
174 Unexpect_Power_Loss_Ct  0x0032   100   100   000    Old_age   Always       -       46
180 Unused_Reserve_NAND_Blk 0x0033   100   100   000    Pre-fail  Always       -       3
183 SATA_Interfac_Downshift 0x0032   100   100   000    Old_age   Always       -       0
184 Error_Correction_Count  0x0032   100   100   000    Old_age   Always       -       0
187 Reported_Uncorrect      0x0032   100   100   000    Old_age   Always       -       0
194 Temperature_Celsius     0x0022   069   041   000    Old_age   Always       -       31 (Min/Max 20/59)
196 Reallocated_Event_Count 0x0032   100   100   000    Old_age   Always       -       0
197 Current_Pending_ECC_Cnt 0x0032   100   100   000    Old_age   Always       -       0
198 Offline_Uncorrectable   0x0030   100   100   000    Old_age   Offline      -       0
199 UDMA_CRC_Error_Count    0x0032   100   100   000    Old_age   Always       -       8
202 Percent_Lifetime_Remain 0x0030   099   099   001    Old_age   Offline      -       1
206 Write_Error_Rate        0x000e   100   100   000    Old_age   Always       -       0
210 Success_RAIN_Recov_Cnt  0x0032   100   100   000    Old_age   Always       -       0
246 Total_LBAs_Written      0x0032   100   100   000    Old_age   Always       -       20297159885
247 Host_Program_Page_Count 0x0032   100   100   000    Old_age   Always       -       634286246
248 FTL_Program_Page_Count  0x0032   100   100   000    Old_age   Always       -       1443889152
249 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       0
250 Read_Error_Retry_Rate   0x0032   100   100   000    Old_age   Always       -       1697991
251 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       0
252 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       0
253 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       171
254 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       684
223 Unkn_CrucialMicron_Attr 0x0032   100   100   000    Old_age   Always       -       21

SMART Error Log Version: 1
Warning: ATA error count 0 inconsistent with error log index 4
No Errors Logged

SMART Self-test log structure revision number 1
No self-tests have been logged.  [To run self-tests, use: smartctl -t]

Selective Self-tests/Logging not supported

The above only provides legacy SMART information - try 'smartctl -x' for more
```

#### Extra

```sh
sudo smartctl -x /dev/sdb
smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.2.15-rt3-arch1-1-rt] (local build)
Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org

=== START OF INFORMATION SECTION ===
Model Family:     Crucial/Micron Client SSDs
Device Model:     CT2000BX500SSD1
Serial Number:    1943E224BEDD
LU WWN Device Id: 5 00a075 1e224bedd
Firmware Version: M6CR030
User Capacity:    2 000 398 934 016 bytes [2,00 TB]
Sector Size:      512 bytes logical/physical
Rotation Rate:    Solid State Device
Form Factor:      2.5 inches
TRIM Command:     Available
Device is:        In smartctl database 7.5/5706
ATA Version is:   ACS-3 T13/2161-D revision 4
SATA Version is:  SATA 3.3, 6.0 Gb/s (current: 6.0 Gb/s)
Local Time is:    Tue Nov  3 19:15:28 2026 CET
SMART support is: Available - device has SMART capability.
SMART support is: Enabled
AAM feature is:   Unavailable
APM feature is:   Unavailable
Rd look-ahead is: Enabled
Write cache is:   Enabled
DSN feature is:   Unavailable
ATA Security is:  Disabled, NOT FROZEN [SEC1]

=== START OF READ SMART DATA SECTION ===
SMART overall-health self-assessment test result: PASSED

General SMART Values:
Offline data collection status:  (0x00)	Offline data collection activity
					was never started.
					Auto Offline Data Collection: Disabled.
Self-test execution status:      (   0)	The previous self-test routine completed
					without error or no self-test has ever
					been run.
Total time to complete Offline
data collection: 		(  120) seconds.
Offline data collection
capabilities: 			 (0x11) SMART execute Offline immediate.
					No Auto Offline data collection support.
					Suspend Offline collection upon new
					command.
					No Offline surface scan supported.
					Self-test supported.
					No Conveyance Self-test supported.
					No Selective Self-test supported.
SMART capabilities:            (0x0002)	Does not save SMART data before
					entering power-saving mode.
					Supports SMART auto save timer.
Error logging capability:        (0x01)	Error logging supported.
					General Purpose Logging supported.
Short self-test routine
recommended polling time: 	 (   2) minutes.
Extended self-test routine
recommended polling time: 	 (  10) minutes.

SMART Attributes Data Structure revision number: 16
Vendor Specific SMART Attributes with Thresholds:
ID# ATTRIBUTE_NAME          FLAGS    VALUE WORST THRESH FAIL RAW_VALUE
  1 Raw_Read_Error_Rate     POSR-K   100   100   000    -    0
  5 Reallocate_NAND_Blk_Cnt -O--CK   100   100   010    -    0
  9 Power_On_Hours          -O--CK   100   100   000    -    42890
 12 Power_Cycle_Count       -O--CK   100   100   000    -    109
171 Program_Fail_Count      -O--CK   100   100   000    -    0
172 Erase_Fail_Count        -O--CK   100   100   000    -    0
173 Ave_Block-Erase_Count   -O--CK   099   099   000    -    18
174 Unexpect_Power_Loss_Ct  -O--CK   100   100   000    -    46
180 Unused_Reserve_NAND_Blk PO--CK   100   100   000    -    3
183 SATA_Interfac_Downshift -O--CK   100   100   000    -    0
184 Error_Correction_Count  -O--CK   100   100   000    -    0
187 Reported_Uncorrect      -O--CK   100   100   000    -    0
194 Temperature_Celsius     -O---K   069   041   000    -    31 (Min/Max 20/59)
196 Reallocated_Event_Count -O--CK   100   100   000    -    0
197 Current_Pending_ECC_Cnt -O--CK   100   100   000    -    0
198 Offline_Uncorrectable   ----CK   100   100   000    -    0
199 UDMA_CRC_Error_Count    -O--CK   100   100   000    -    8
202 Percent_Lifetime_Remain ----CK   099   099   001    -    1
206 Write_Error_Rate        -OSR--   100   100   000    -    0
210 Success_RAIN_Recov_Cnt  -O--CK   100   100   000    -    0
246 Total_LBAs_Written      -O--CK   100   100   000    -    20297159885
247 Host_Program_Page_Count -O--CK   100   100   000    -    634286246
248 FTL_Program_Page_Count  -O--CK   100   100   000    -    1443889152
249 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    0
250 Read_Error_Retry_Rate   -O--CK   100   100   000    -    1697992
251 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    0
252 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    0
253 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    171
254 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    684
223 Unkn_CrucialMicron_Attr -O--CK   100   100   000    -    21
                            ||||||_ K auto-keep
                            |||||__ C event count
                            ||||___ R error rate
                            |||____ S speed/performance
                            ||_____ O updated online
                            |______ P prefailure warning

General Purpose Log Directory Version 1
SMART           Log Directory Version 1 [multi-sector log support]
Address    Access  R/W   Size  Description
0x00       GPL,SL  R/O      1  Log Directory
0x01           SL  R/O      1  Summary SMART error log
0x02           SL  R/O      1  Comprehensive SMART error log
0x03       GPL     R/O      1  Ext. Comprehensive SMART error log
0x04       GPL,SL  R/O      8  Device Statistics log
0x06           SL  R/O      1  SMART self-test log
0x07       GPL     R/O      1  Extended self-test log
0x10       GPL     R/O      1  NCQ Command Error log
0x11       GPL     R/O      1  SATA Phy Event Counters log
0x24       GPL     R/O     88  Current Device Internal Status Data log
0x30       GPL,SL  R/O      9  IDENTIFY DEVICE data log
0x80-0x9f  GPL,SL  R/W     16  Host vendor specific log

SMART Extended Comprehensive Error Log Version: 1 (1 sectors)
Device Error Count: 9 (device log contains only the most recent 4 errors)
	CR     = Command Register
	FEATR  = Features Register
	COUNT  = Count (was: Sector Count) Register
	LBA_48 = Upper bytes of LBA High/Mid/Low Registers ]  ATA-8
	LH     = LBA High (was: Cylinder High) Register    ]   LBA
	LM     = LBA Mid (was: Cylinder Low) Register      ] Register
	LL     = LBA Low (was: Sector Number) Register     ]
	DV     = Device (was: Device/Head) Register
	DC     = Device Control Register
	ER     = Error register
	ST     = Status register
Powered_Up_Time is measured from power on, and printed as
DDd+hh:mm:SS.sss where DD=days, hh=hours, mm=minutes,
SS=sec, and sss=millisec. It "wraps" after 49.710 days.

Error 9 [0] log entry is empty
Error 8 [3] log entry is empty
Error 7 [2] log entry is empty
Error 6 [1] occurred at disk power-on lifetime: 0 hours (0 days + 0 hours)
  When the command that caused the error occurred, the device was active or idle.

  After command completion occurred, registers were:
  ER -- ST COUNT  LBA_48  LH LM LL DV DC
  -- -- -- == -- == == == -- -- -- -- --
  00 -- 00 93 00 00 00 00 00 00 00 00 00

  Commands leading to the command that caused the error were:
  CR FEATR COUNT  LBA_48  LH LM LL DV DC  Powered_Up_Time  Command/Feature_Name
  -- == -- == -- == == == -- -- -- -- --  ---------------  --------------------
  b0 00 d1 01 01 00 00 4f 00 c2 01 00 08     00:00:00.000  SMART READ ATTRIBUTE THRESHOLDS [OBS-4]
  b0 00 d0 01 01 00 00 4f 00 c2 00 00 08     00:00:00.000  SMART READ DATA
  ec 00 00 01 01 00 00 00 00 00 00 00 08     00:00:00.000  IDENTIFY DEVICE
  ec 00 00 01 01 00 00 00 00 00 00 00 08     00:00:00.000  IDENTIFY DEVICE
  b0 00 da 00 00 00 00 4f 00 c2 00 00 08     00:00:00.000  SMART RETURN STATUS

SMART Extended Self-test Log Version: 1 (1 sectors)
No self-tests have been logged.  [To run self-tests, use: smartctl -t]

Selective Self-tests/Logging not supported

SCT Commands not supported

Device Statistics (GP Log 0x04)
Page  Offset Size        Value Flags Description
0x01  =====  =               =  ===  == General Statistics (rev 1) ==
0x01  0x008  4             109  ---  Lifetime Power-On Resets
0x01  0x010  4           42890  ---  Power-on Hours
0x01  0x018  6      3117290701  ---  Logical Sectors Written
0x01  0x020  6           20000  ---  Number of Write Commands
0x01  0x028  6        13717922  ---  Logical Sectors Read
0x01  0x030  6           21368  ---  Number of Read Commands
0x07  =====  =               =  ===  == Solid State Device Statistics (rev 1) ==
0x07  0x008  1               2  ---  Percentage Used Endurance Indicator
                                |||_ C monitored condition met
                                ||__ D supports DSN
                                |___ N normalized value

Pending Defects log (GP Log 0x0c) not supported

SATA Phy Event Counters (GP Log 0x11)
ID      Size     Value  Description
0x0001  4            0  Command failed due to ICRC error
0x0002  4            0  R_ERR response for data FIS
0x0005  4            0  R_ERR response for non-data FIS
0x000a  4            2  Device-to-host register FISes sent due to a COMRESET
```

## Performance

Tests performed using my good old trusty [Lenovo ThinkPad P51](/blog/2017-08-31-lenovo-thinkpad-p51).

### With Apple TB3 ↔ TB1/2 adapter

```{figure} /images/2026-11-03_lacie_apple.png
:alt: Benchmark through the Apple Thunderbolt adapter
:width: 100%
Apple adapter.
```

### With StarTech TB3 ↔ TB1/2 adapter

*Marginally slower!*

```{figure} /images/2026-11-03_lacie_startech.png
:alt: Benchmark through the StarTech Thunderbolt adapter
:width: 100%
StarTech adapter.
```

### Over USB

```{figure} /images/2026-11-03_lacie_usb.png
:alt: Benchmark over USB 3.0
:width: 100%
USB 3.0.
```

## Teardown

### Photos

{button}`Teardown photos album <https://photos.app.goo.gl/nMDd4uqHQMPVhT1u5>`

### External

The rubber bumper peels off first.
The external labels confirm the commercial identity: **model LRD0TU1** ("Rugged USB 3.0 Thunderbolt"), S/N NL6B05HS, 2019, assembled in Thailand. 
Six Phillips screws are exposed: two short ones on the flanks around the USB port, and four long ones on the underside.

### Insides

Inside, a bare **Crucial BX500** (`CT2000BX500SSD1`, FW `M6CR030`, SATA 6 Gb/s, assembled in Mexico) plugs directly onto a U-shaped SATA connector on the board.

#### SSD

The **Crucial/Micron BX500** is a DRAM-less TLC SSD with a dynamic SLC cache.

Specs from Micron's website and PDF datasheet:
- General Tech Specs:
  - Interface: SATA (6Gb/s)
  - Total Density: 2TB
  - Form Factor: 2.5-inch (7mm)
  - Life Expectancy (MTTF): 1.5 million hours
  - SSD Endurance TBW: 720TB
- Speed & Timing (*Typical I/O performance numbers as measured using CrystalDiskMark® with a queue depth of 32 and write cache enabled. Fresh out-of-box (FOB) state is assumed. For
  performance measurement purposes, the SSD may be restored to FOB state using the secure erase command. System variations will affect measured results.*):
  - Sequential Write: 500 MB/s
  - Sequential Read: 540 MB/s
- Advanced Features
  - Multistep data integrity algorithm
  - Thermal monitoring
  - SLC write acceleration
  - Active garbage collection
  - TRIM support
  - Self-monitoring and reporting technology (SMART)
  - Error correction code (ECC)
- Operating Temperature: 0 °C to 70 °C

#### PCB

This SATA connector holds a tag on its side: Data Matrix ECC 200 (ISO/IEC 16022) 2D Code (Reads `SJ4200215` using a standard smartphone), `SJ4200215` (PCB serial number?), `FW:131030A12300` (Controllers firmware version?).
The bridge PCB is marked with:
```
HSB J
MV-1
94V-0
E89382
1844
```
logos
```
UL Recognized Component logo (Reversed UR)
```
and
```
EH2DP5
MAIN/BD
790CDP540B0E1
REV.B0
```

- Manufacturer according to [UL Product IQ](https://productiq.ulprospector.com/en/profile/204421/zpmv2.e89382): [HannStar Board Corp.](https://tw.hannstarboard.com/en/).
- Laminate flame-rating code: HannStar's `MV-1` (flame-retardant)
- Flammability rating: `94V-0`
- Manufacturing date: 44th week of 2018

#### Chips

The board is a **dual-path** design with two independent SATA bridges, one per interface:

| Designator | Block | Manufacturer | Model | Role |
|------------|-------|--------------|-------|------|
| U1 | Firmware (SATA/USB3 bridge) | Macronix International Co., Ltd. (MXIC) | **MX25L5121E** | 512K-BIT [x 1] CMOS SERIAL FLASH MEMORY |
| U2 | USB 3.0 → SATA | ASMedia | **ASM1153E** | USB3.0 to SATA Bridge Controller |
| U3 | Firmware (SATA/PCIe bridge) | Macronix International Co., Ltd. (MXIC) | **MX25L5121E** | 512K-BIT [x 1] CMOS SERIAL FLASH MEMORY |
| U4 | Thunderbolt (PCIe) → SATA | ASMedia | **ASM1061** | PCI Express 2.0 to SATA 6Gbps Controller |
| U5 | SATA switch | ASMedia | **ASM1456** | SATA 6G Mux/Demux Switch |
| U6 & U11 | ? | ? | ? | *Unpopulated*<br>Pinout: 5 pins (3 + 2), SOT-23-5 |
| U7 & U9 | Power | ? | ? | *Unidentified*<br>Markings: `AEH`<br>`J25`<br>`345`<br>Package: plastic, 12 contacts (5 + 5 on long edges, 1 + 1 on short edges) |
| U8 | Power | ? | ? | *Unidentified*<br>Markings: `91L6ZB` or `91L6Z8`<br>Package: CSP (bare-die flip-chip) |
| U10 | Power / protection | Monolithic Power Systems (MPS) | **MP1482DS** | rail regulation |
| U12 | ? | ? | ? | *Unidentified*<br>Package: plastic, 5 pins (3 + 2), SOT-23-5 |
| U13 | ? | ? | ? | *Unpopulated*<br>Pinout: 14 pins (7 + 7), SOIC-14 |
| Q9 | Power | ? | **Q9435** | Package: SOP-8<br>P-Channel Power MOSFET |
| X1 & X2 | Clock | ? | ? | 20 MHz quartz (controller reference clocks) |
| CON1 | TB Connector | ? | ? | Thunderbolt interface entry point to integrated miniDP cable |
| CON2 | USB Connector | ? | USB Micro-B SuperSpeed | USB 3.0 interface entry point |
| CON3 | ? | ? | ? | *Unpopulated*. 4 pins. Debug/UART for U13? |

### Comments

The copper tape under CON1 is only a mechanical strain relief for the fixed Thunderbolt cable. There is **no Thunderbolt controller on the board**. This is the key architectural point: Thunderbolt *is* native PCIe, so the ASM1061 plugs directly onto the Thunderbolt lane. The Thunderbolt-to-PCIe conversion happens host-side, not inside the enclosure.

So the two paths resolve to:

- **Thunderbolt** → CON1 (fixed mDP cable) → (PCIe 2.0 x1, 5GT/s) ASM1061 (SATA 6Gb/s) → ASM1456 → SATA
- **USB 3.0** → CON2 → (USB 3.0, 5Gb/s) ASM1153E (SATA 6Gb/s) → ASM1456 → SATA

This explains the throughput ceiling measured on both interfaces: the BX500 *is* the current bottleneck. However, the *theoretical ceiling* is set by the SATA bridges themselves on their outbound interfaces (ASM1061 capped at 5GT/s by its single PCIe 2.0 lane on the TB side, ASM1153E capped at 5Gb/s on the USB side), despite the drive negotiating a clean SATA 6Gb/s in both modes. Ultimately, the bridges' outbound interfaces set the limit to a *maximum effective speed* of **~500 MB/s**.

#### Upgrade

**When planning a drive upgrade, anything rated above 500 MB/s would be wasted.**

Serious candidates:
- Budget: **Micron/Crucial MX500** (up to 2TB) for its DRAM, providing better IOPS and sustained write performance;
- High-capacity: **Samsung 870 QVO** (up to 8TB) for its ample storage, though the QLC endurance and sustained-write performance drop (to ~160 MB/s) once the SLC cache is exhausted;
- High-end: **Samsung 870 EVO** (up to 2TB) for its DRAM + SLC cache, providing the best endurance and consistent performance.
