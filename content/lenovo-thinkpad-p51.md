Title: Lenovo ThinkPad P51
Date: 2017-08-31 12:15
Modified: 2020-04-02 21:30
Category: Informatique
Slug: lenovo-thinkpad-p51
Tags: Hardware, Lenovo, ThinkPad, P51, GNU/Linux, Arch Linux
Status: published

### TODO

- Hardware features matrix (WIP)
- BTRFS maintenance: btrfs balance + mail results
- Backup HDD: cron btrfs send/receive
- Encrypt filesystems
- [Contribute DMI IDs](http://www.thinkwiki.org/wiki/List_of_DMI_IDs#Adding_entries):

```
|| LENOVO || 20HHCTO1WW || ThinkPad P51 || LENOVO || 20HHCTO1WW || SDK0J40697 WIN || LENOVO || None || LENOVO || N1UET72W (1.46 ) || 10/04/2018 
|| <nowiki></nowiki>
```

- Report thermal alarm while running Unigine Superposition:

```
thinkpad_acpi: unknown possible thermal alarm or keyboard event received
thinkpad_acpi: unhandled HKEY event 0x6031
thinkpad_acpi: please report the conditions when this event happened to ibm-acpi-devel@lists.sourceforge.net
```


### Hardware features


#### Matrix

| Device                                    | Model                                                           | Specs                                                                                                                                      | Status                                                                                         | Modules                    |
|-------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------|
| CPU                                       | [Intel Xeon E3-1535M v6][1]                                     | 3.1 GHz / 4.2 GHz 4 cores / 8 threads 8 MB SmartCache                                                                                      | Working                                                                                        | N.A.                       |
| Imaging Unit/Gaussian Mixture Model (GMM) | In CPU                                                          |                                                                                                                                            | ?                                                                                              | ?                          |
| ECC memory                                | [Samsung M474A2K43BB1-CRC][2]                                   | 260pin SODIMM DDR 4 2400MHz 16 GB (× 4 - 64 GB total)                                                                                      | Working                                                                                        | N.A.                       |
| Screen                                    | BOE NV156FHM-N42                                                | 15.6" 16:9 1920×1080 IPS LED                                                                                                               | Working                                                                                        | N.A.                       |
| Backlight control                         |                                                                 |                                                                                                                                            | Working                                                                                        | N.A.                       |
| GPU (Intel)                               | Intel HD Graphics P630 (CPU integrated)                         | 350 MHz / 1.10 GHz 1.7 GB DirectX 12 OpenGL 4.4 OpenCL 2.0                                                                                 | Working                                                                                        | i915                       |
| GPU (nVidia)                              | GM206GLM \[Quadro M2200 Mobile\]                                | 1024 CUDA cores 4 GB GDDR5 128-bit 55W OpenGL 4.5 DirectX 12 (Hardware Feature Level 12_1) Shader Model 5.0 DisplayPort 1.2 FP32 precision | Working                                                                                        | nvidia                     |
| HDMI                                      |                                                                 | 1.4b                                                                                                                                       | Working                                                                                        | nvhda (audio)              |
| Mini DisplayPort                          |                                                                 | 1.2a                                                                                                                                       | Working                                                                                        | thunderbolt                |
| Thunderbolt 3 / USB 3.1                   |                                                                 |                                                                                                                                            | Working                                                                                        | ?                          |
| LAN                                       | Intel I219-LM                                                   | 1 Gbs                                                                                                                                      | Working                                                                                        | e1000e                     |
| WLAN (Wi-Fi)                              | [Intel Wireless 8265][3]                                        | 802.11ac M.2                                                                                                                               | Working                                                                                        | iwlwifi                    |
| WWAN                                      | [Qualcomm Snapdragon X7 LTE-A][4] ([Sierra Wireless EM7455][5]) | 4G LTE-A M.2                                                                                                                               | Working                                                                                        | cdc_mbim                   |
| GPS                                       | In WWAN device                                                  | GNSS (GPS, GLONASS, Beidou, Galileo)                                                                                                       | TBD                                                                                            |                            |
| Bluetooth                                 | Intel Wireless 8265                                             | 4.2 (Maybe software limited to 4.1?)                                                                                                       | Working                                                                                        | btusb                      |
| Audio                                     | Intel ([Realtek ALC3268][6] codec)                              |                                                                                                                                            | Working                                                                                        | snd_hda_intel              |
| NVMe (M.2 SSD)                            | Samsung NVMe SSD Controller SM961/PM961                         | 1 TB (× 2)                                                                                                                                 | Working (Needs accessories)                                                                    |                            |
| SATA (HDD)                                | Western Digital WDC WD10SPCX-60K                                | 1 TB 2.5" wide 7mm high                                                                                                                    | Working (Needs accessories)                                                                    |                            |
| Keyboard                                  | Chicony                                                         |                                                                                                                                            | Working                                                                                        | atkbd                      |
| Function/Multimedia keys                  |                                                                 |                                                                                                                                            | Working                                                                                        | N.A.                       |
| TrackPoint                                | Chicony                                                         |                                                                                                                                            | Working                                                                                        | psmouse                    |
| Touchpad                                  | Synaptics                                                       | Mylar surface                                                                                                                              | Working                                                                                        | psmouse                    |
| Touchscreen                               | Wacom                                                           | Capacitive multi-touch 10-fingers                                                                                                          | Working                                                                                        | wacom                      |
| Active Pen                                | Wacom                                                           |                                                                                                                                            | Working                                                                                        | wacom                      |
| Webcam                                    | [SunplusIT controller?][7]                                      | 720p (1280×720) Fixed focus                                                                                                                | Working                                                                                        | uvcvideo                   |
| Media card                                |                                                                 | MMC, SD, SDHC, SDXC UHS-II                                                                                                                 | Working                                                                                        |                            |
| Express Card                              | Realtek RTS525A                                                 | /34                                                                                                                                        | Working                                                                                        | rtsx_pci                   |
| Smartcard Reader                          | [Alcor Micro AU9540][8]                                         |                                                                                                                                            | Working                                                                                        |                            |
| USB 3.0                                   |                                                                 |                                                                                                                                            | Working                                                                                        |                            |
| Power management                          |                                                                 |                                                                                                                                            | Working                                                                                        | thinkpad_acpi              |
| TPM                                       |                                                                 | 2.0                                                                                                                                        | Not Working (No TPM 2.0 toolchain on GNU/Linux just yet. See [James Bottomley's blog post][9]) | tpm                        |
| Fingerprint reader                        | Validity Sensors, Inc.                                          |                                                                                                                                            | Partially Working                                                                              | libfprint fork (See below) |
| Color calibrator                          | X-Rite Pantone Color Sensor                                     |                                                                                                                                            | Not Working                                                                                    |                            |
| UEFI flash                                |                                                                 |                                                                                                                                            | Not Working                                                                                    |                            |
| Suspend to RAM (Standby)                  |                                                                 |                                                                                                                                            | Working                                                                                        |                            |
| Suspend to disk (Hibernate)               |                                                                 |                                                                                                                                            | Working                                                                                        |                            |
| Battery                                   |                                                                 | 96 Wh                                                                                                                                      | Working                                                                                        |                            |

[1]: https://ark.intel.com/products/97468/Intel-Xeon-Processor-E3-1535M-v6-8M-Cache-3_10-GHz
[2]: http://www.samsung.com/semiconductor/products/dram/pc-dram/ddr4-sodimm/M474A2K43BB1?ia=2429
[3]: https://ark.intel.com/fr/products/94150/Intel-Dual-Band-Wireless-AC-8265
[4]: https://www.qualcomm.com/products/snapdragon/modems/4g-lte/x7
[5]: https://www.sierrawireless.com/products-and-solutions/embedded-solutions/products/em7455/
[6]: http://www.realtek.com.tw/products/productsView.aspx?Langid=1&PFid=27&Level=5&Conn=4&ProdID=140
[7]: http://www.sunplusit.com/english/products/pccamera/index.aspx
[8]: http://www.alcormicro.com/en_content/c_product/product_01b.php?CategoryID=4&IndexID=4
[9]: https://blog.hansenpartnership.com/tpm2-and-linux/


#### GPUs

Display management scripts and configuration repository available on [GitHub](https://github.com/rdoursenaud/lenovo-p51-display-management)


##### Optimus / Prime

`/etc/modprobe.d/nvidia_drm.conf`
```
options nvidia_drm modeset=1
```

`/boot/refind_linux.conf`
```
# drm.rnodes=1 Render nodes for multiple GPU and displays (PRIME)
# intel_iommu=1 Enable hardware virtualization
"Boot with standard options"  "rw root=UUID=b549d30f-939e-4d74-b39d-676856e9faca drm.rnodes=1 intel_iommu=1 quiet initrd=/intel-ucode.img initrd=/initramfs-linux.img"
```


##### Energy saving

`/etc/modprobe.d/i915.conf`
```
options i915 modeset=1
options i915 semaphores=1
options i915 enable_rc6=4
options i915 enable_dc=2
options i915 enable_fbc=1
```


##### HDMI audio

Build, install and enable the nvhda module from [this bug report](https://bugs.freedesktop.org/show_bug.cgi?id=75985#c27)


#### Touchscreen

`~/.xinitrc`
```sh
# Touchscreen
xinput --float Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Finger\ touch
xinput --float Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Pen\ stylus
xinput --float Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Pen\ eraser
        
# Map touchscreen and pen to laptop screen only
xinput map-to-output Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Finger\ touch eDP-1-1
xinput map-to-output Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Pen\ stylus eDP-1-1
xinput map-to-output Wacom\ Co.,Ltd.\ Pen\ and\ multitouch\ sensor\ Pen\ eraser eDP-1-1
```


#### Dock

Sound I/O not working.


##### Update 2018-08-28

Sound I/O is now working in Arch Linux.
Don't know which update brought support though…


#### Fans

`/etc/modprobe.d/thinkpad_acpi.conf`
```
options thinkpad_acpi fan_control=1
```


##### [ThinkFan](https://github.com/vmatare/thinkfan/)

`/etc/thinkfan.conf`
```yaml
sensors:
  - hwmon: /sys/devices/platform/coretemp.0/hwmon/hwmon0/temp1_input  # CPU Package
  - hwmon: /sys/devices/platform/coretemp.0/hwmon/hwmon0/temp2_input  # CPU Core 0
  - hwmon: /sys/devices/platform/coretemp.0/hwmon/hwmon0/temp3_input  # CPU Core 1
  - hwmon: /sys/devices/platform/coretemp.0/hwmon/hwmon0/temp4_input  # CPU Core 2
  - hwmon: /sys/devices/platform/coretemp.0/hwmon/hwmon0/temp5_input  # CPU Core 3
  - hwmon: /sys/devices/virtual/hwmon/hwmon2/temp1_input  # pch_skylake
  - hwmon: /sys/devices/virtual/hwmon/hwmon3/temp1_input  # acpitz (ACPI CPU)
#  - hwmon: /sys/devices/virtual/hwmon/hwmon4/temp1_input  # iwlwifi
  - nvidia: 01:00.0  # nVidia GPU
  - atasmart: /dev/sda  # HDD
    correction: [10]

fans:
  - tpacpi: /proc/acpi/ibm/fan

levels:
  - [0, 0,  40]
  - [1, 32, 55]
  - [2, 54, 66]
  - [3, 65, 76]
  - [4, 75, 80]
  - [5, 78, 85]
  - [6, 82, 88]
  - [7, 85, 32767]
```


###### FIXME
Virtual hwmon path can change upon reboot and prevent thinkfan from starting.
The order is determined by the modules loading order.
Workaround seem to be to load modules manually in a deterministic order.


#### Fingerprint reader

Not supported by fprint.


##### Update 2020-04-02

The libfprint fork at https://github.com/nmikhailov/Validity90 offers experimental support with ongoing reverse engineering.


### Install


#### Partitions

ESP: FAT32 1024 MiB (550 minimum [Source](http://www.rodsbooks.com/efi-bootloaders/principles.html))  
BTRFS 931,51 GiB (To match the backup HDD size)  
SWAP 21,36 GiB

RAID1 BTRFS SSDs  
ESP backup on second disk  
Second swap


#### Directories and subvolumes

```
toplevel
 +-- root subvolume (set-default) /
     +-- home directory
         +-- raph subvolume
  \-- snapshots directory
      +-- root directory
          +-- YYYY-MM-DDThh:mm:ss+02:00 (`date -Iseconds`) snapshot directory
          +-- …
      +-- raph directory
          +-- YYYY-MM-DDThh:mm:ss+02:00 (`date -Iseconds`) snapshot directory
          +-- …
```


### Firmware bugs?

TODO: report to Lenovo support.


#### Workstation dock long USB detection

Using the workstation dock, boot time is painfully slow as the EFI scans USB peripherals.  
Unfortunately, removing USB devices from the dock doesn't improve performance.


#### Disk lock and fingerprint

When using the fingerprint scanner on boot with disk lock enabled, the first disk sometimes does not unlock.


### Benchmarks


#### Geekbench


##### CPU

[Linux](http://browser.geekbench.com/v4/cpu/3884202)  
[Microsoft Windows 10](http://browser.geekbench.com/v4/cpu/3280047)


##### GPU compute

[Linux nVidia Quadro M2200 OpenCL](http://browser.geekbench.com/v4/compute/1074183)  
[Microsoft Windows 10 Intel HD Graphics P630](http://browser.geekbench.com/v4/compute/882924)  
[Microsoft Windows 10 nVidia Quadro M2200](http://browser.geekbench.com/v4/compute/882920)


#### Luxmark

[CPU+GPU](http://www.luxmark.info/node/4625)  
[GPU](http://luxmark.info/node/4624)


#### gtkperf

Launched from CLI  
Fullscreen window 1920x1080  
5 consecutive runs  


##### Intel modesetting
3.62-3.74


##### Intel
2.72-2.80


##### nVidia


###### Single laptop screen
2.70-2.74


###### 4 screens setup with Workstation Dock
screen 1 (DP-1): 4.11-4.67  
screen 2 (DP-2 rotated 90° right): 4.80-5.41  
screen 3 (DP-3):  4.91-5.69  
screen 4 (eDP-1-1): 4.52-5.27  
