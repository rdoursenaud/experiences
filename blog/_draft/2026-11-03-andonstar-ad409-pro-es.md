---
subject: 'Électronique • Electronics'
---
# Andonstar AD409 Pro-ES

https://andonstar.com

## Provider

[BatterFly](https://www.batterfly.com/shop/fr/andonstar-ad409-pro-es)
Price: 348€ /wo VAT

## Downloads

https://andonstar.com/download/

- User manual of AD409 Pro (PDF)
- User manual of Endoscope (JPG)

## Software version

% TODO: insert photo

```
AD400.23111690.V44-DUAL10
LD-4G
```

## Interfaces

### HDMI

#### Lenovo Stack Mobile Projector

- QHD: KO (Flickering)
- FHD: KO (No display)
- HD: KO (No display)

#### Lenovo ThinkVision T24t-20

OK but shuts down the integrated monitor.

% TODO: insert photo

Fixed resolution: 1920×1080@60
Regardless of the video resolution or global frequency (50/60 Hz) settings.

### USB

- With supplied cable:
  - Power: OK
  - Data: KO (*Update: probably a PEBCAK, it now works properly!*)
- With standard USB-C <-> USB-A cable: OK
  - Mass storage
  - PC Camera

## Linux support

USB
Wi-Fi: TODO

### Mass storage mode

```sh
dmesg
[ 1775.401721] usb 1-5: new high-speed USB device number 13 using xhci_hcd
[ 1775.524760] usb 1-5: New USB device found, idVendor=0603, idProduct=8611, bcdDevice= 1.00
[ 1775.525008] usb 1-5: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[ 1775.525009] usb 1-5: Product: USB Camera
[ 1775.525010] usb 1-5: Manufacturer: NOVATEK
[ 1775.525011] usb 1-5: SerialNumber: 966110000000100
[ 1775.572964] usb-storage 1-5:1.0: USB Mass Storage device detected
[ 1775.573084] usb-storage 1-5:1.0: Quirks match for vid 0603 pid 8611: 4000
[ 1775.573110] scsi host4: usb-storage 1-5:1.0
[ 1775.573219] usbcore: registered new interface driver usb-storage
[ 1775.579990] usbcore: registered new interface driver uas
[ 1776.602991] scsi 4:0:0:0: Direct-Access     NOVATEKN vt-DSC                PQ: 0 ANSI: 5
[ 1776.603167] sd 4:0:0:0: Attached scsi generic sg1 type 0
[ 1776.603428] sd 4:0:0:0: [sdb] Media removed, stopped polling
[ 1776.606905] sd 4:0:0:0: [sdb] Attached SCSI removable disk
```

```sh
lsusb
Bus 001 Device 013: ID 0603:8611 Novatek Microelectronics Corp. NTK96550-based camera (mass storage mode)
```

```sh
lsblk /dev/sdb
NAME MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sdb    8:16   1    0B  0 disk
```

> Only exposes the micro-SD slot. No internal storage.

### PC Camera mode

```sh
[ 2005.592133] usb 1-5: new high-speed USB device number 14 using xhci_hcd
[ 2005.715165] usb 1-5: New USB device found, idVendor=0603, idProduct=8612, bcdDevice= 0.10
[ 2005.715586] usb 1-5: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 2005.715587] usb 1-5: Product: USB Camera
[ 2005.715588] usb 1-5: Manufacturer: NOVATEK
[ 2005.717927] uvcvideo 1-5:1.0: Found UVC 1.00 device USB Camera (0603:8612)
[ 2005.718043] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2005.753206] usb 1-5: Warning! Unlikely small volume range (=99), linear volume or custom curve?
[ 2005.753209] usb 1-5: [3] FU [Mic Capture Volume] ch = 1, val = 1/100/1
[ 2006.798567] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.810903] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.826044] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.838396] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.851697] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.866490] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.878898] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.891631] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
[ 2006.907521] uvcvideo 1-5:1.1: UVC non compliance: Reducing max payload transfer size (3145730) to fit endpoint limit (2048).
```

```sh
lsusb
Bus 001 Device 010: ID 0603:8612 Novatek Microelectronics Corp. NTK96550-based camera (webcam mode)
```

Standard UVC (USB Video Class) camera.

> Didn’t manage to get the endoscope working however.

```sh
v4l2-ctl --list-formats-ext -d /dev/video2
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'H264' (H.264, compressed)
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
	[1]: 'MJPG' (Motion-JPEG, compressed)
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
```

```sh
v4l2-ctl --list-formats-ext -d /dev/video3
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture
```

## Wi-Fi

SSID: `Andonstar-88492d18e45d`
WPA2: `12345678`

MAC: `88:49:2D:18:E4:5D`
Client IP: `192.168.1.33`
Host IP: `192.168.1.254`

### nmap

```sh
sudo nmap 192.168.1.254
Starting Nmap 7.993 ( https://nmap.org ) at 2026-11-03 16:26 +0100
Unable to determine any DNS servers. . Falling back to --system-dns. Specify valid servers with --dns-servers
Nmap scan report for _gateway (192.168.1.254)
Host is up (0.016s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
3333/tcp open  dec-notes
8192/tcp open  sophos
MAC Address: 88:49:2D:18:E4:5D (Shenzhen Bilian Electronic，LTD)

Nmap done: 1 IP address (1 host up) scanned in 0.32 seconds
```

```sh
sudo nmap -A -T4 192.168.1.254
Starting Nmap 7.993 ( https://nmap.org ) at 2026-11-03 16:29 +0100
Unable to determine any DNS servers. . Falling back to --system-dns. Specify valid servers with --dns-servers
Nmap scan report for _gateway (192.168.1.254)
Host is up (0.0022s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
80/tcp   open  http       hfs/1.00.000
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: hfs/1.00.000
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 200 OK
|     Server: hfs/1.00.000
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Accept-Ranges: bytes
|     Content-Length: 128
|     Content-Type: text/html
|     Connection: close
|     <html>
|     <head><title>Page Not found</title></head>
|     <body><h2>The requested URL was not found on this server.</h2></body>
|     </html>
|   GetRequest:
|     HTTP/1.1 200 OK
|     Server: hfs/1.00.000
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Accept-Ranges: bytes
|     Content-Length: 596
|     Content-Type: text/html
|     Connection: close
|     <html>
|     <body>
|     <div id=folderlabel>folder</div>
|     <div id=folder></div>
|     <div id=body>
|     <table cellpadding=5>
|     <th>Filename
|     <th>Filesize
|     <th>Filetime
|     <tr><td colspan="4"><hr size=1 noshade align=top></td></tr></table>
|     <form name=frm action="" method=post enctype="multipart/form-data"><input name=fileupload1 size=70 type=file><br/><input name=upbtn type=submit value="Upload files"></form><form name=frm2 action="?custom=1" method=post enctype="multipart/form-data"><input name=fileupload2 size=70 type=file><br/><input name=upbtn type=submit value="Upload Custom files"></form></div>
|     </body>
|_    </html>
443/tcp  open  ssl/https?
| ssl-cert: Subject: commonName=192.168.1.254/organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=AU
| Not valid before: 2016-12-23T08:28:51
|_Not valid after:  2025-03-11T08:28:51
3333/tcp open  dec-notes?
8192/tcp open  sophos?
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.1 200 OK
|     Server: eCos/1.0
|     Connection: close
|     Cache-Control: no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0
|     Pragma: no-cache
|     Content-Type: multipart/x-mixed-replace;boundary=arflebarfle
|     --arflebarfle
|     Content-Type: image/jpeg
|     Content-Length: 33646
|     '92<;8276?FZL?BUC67NjOU]`efe=KnvmbuZcea
|     .a@7@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
|     $3br
|     %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|_    &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port80-TCP:V=7.993%I=7%D=11/3%Time=6AE9FDCE%P=x86_64-pc-linux-gnu%r(Get
SF:Request,31A,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20hfs/1\.00\.000\r\nCac
SF:he-Control:\x20no-store,\x20no-cache,\x20must-revalidate\r\nPragma:\x20
SF:no-cache\r\nAccept-Ranges:\x20bytes\r\nContent-Length:\x20596\r\nConten
SF:t-Type:\x20text/html\r\nConnection:\x20close\r\n\r\n<html>\n<body>\n<di
SF:v\x20id=folderlabel>folder</div>\n<div\x20id=folder></div>\n<div\x20id=
SF:body>\n<table\x20cellpadding=5>\n<th>Filename\n<th>Filesize\n<th>Fileti
SF:me\n<tr><td\x20colspan=\"4\"><hr\x20size=1\x20noshade\x20align=top></td
SF:></tr></table>\n<form\x20name=frm\x20action=\"\"\x20method=post\x20enct
SF:ype=\"multipart/form-data\"><input\x20name=fileupload1\x20size=70\x20ty
SF:pe=file><br/><input\x20name=upbtn\x20type=submit\x20value=\"Upload\x20f
SF:iles\"></form><form\x20name=frm2\x20action=\"\?custom=1\"\x20method=pos
SF:t\x20enctype=\"multipart/form-data\"><input\x20name=fileupload2\x20size
SF:=70\x20type=file><br/><input\x20name=upbtn\x20type=submit\x20value=\"Up
SF:load\x20Custom\x20files\"></form></div>\n</body>\n</html>\n")%r(FourOhF
SF:ourRequest,146,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20hfs/1\.00\.000\r\n
SF:Cache-Control:\x20no-store,\x20no-cache,\x20must-revalidate\r\nPragma:\
SF:x20no-cache\r\nAccept-Ranges:\x20bytes\r\nContent-Length:\x20128\r\nCon
SF:tent-Type:\x20text/html\r\nConnection:\x20close\r\n\r\n<html>\n<head><t
SF:itle>Page\x20Not\x20found</title></head>\n<body><h2>The\x20requested\x2
SF:0URL\x20was\x20not\x20found\x20on\x20this\x20server\.</h2></body>\n</ht
SF:ml>\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8192-TCP:V=7.993%I=7%D=11/3%Time=6AE9FDCE%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,4504,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20eCos/1\.0\r\nConne
SF:ction:\x20close\r\nCache-Control:\x20no-store,\x20no-cache,\x20must-rev
SF:alidate,\x20pre-check=0,\x20post-check=0,\x20max-age=0\r\nPragma:\x20no
SF:-cache\r\nContent-Type:\x20multipart/x-mixed-replace;boundary=arflebarf
SF:le\r\n\r\n--arflebarfle\r\nContent-Type:\x20image/jpeg\r\nContent-Lengt
SF:h:\x2033646\r\n\r\n\xff\xd8\xff\xdb\0\x84\0\x10\x0b\x0c\x0e\x0c\n\x10\x
SF:0e\r\x0e\x12\x11\x10\x13\x17'\x19\x17\x15\x15\x170\"\$\x1c'92<;8276\?FZ
SF:L\?BUC67NjOU\]`efe=KnvmbuZcea\x01\x11\x12\x12\x17\x15\x17\.\x19\x19\.a@
SF:7@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xff\xc0\0\x11\x08\
SF:x01p\x02\x80\x03\x01\"\0\x02\x11\x01\x03\x11\x01\xff\xc4\x01\xa2\0\0\x0
SF:1\x05\x01\x01\x01\x01\x01\x01\0\0\0\0\0\0\0\0\x01\x02\x03\x04\x05\x06\x
SF:07\x08\t\n\x0b\x10\0\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\0\0\x0
SF:1}\x01\x02\x03\0\x04\x11\x05\x12!1A\x06\x13Qa\x07\"q\x142\x81\x91\xa1\x
SF:08#B\xb1\xc1\x15R\xd1\xf0\$3br\x82\t\n\x16\x17\x18\x19\x1a%&'\(\)\*4567
SF:89:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92
SF:\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb
SF:2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\x
SF:d2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\
SF:xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\x01\0\x03\x01\x01\x01\x01\x
SF:01\x01\x01\x01\x01\0\0\0\0\0\0\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\
SF:x11\0\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\0\x01\x02w\0\x01\x02\
SF:x03\x11\x04\x05!1\x06\x12AQ\x07aq\x13\"2\x81\x08\x14B\x91\xa1\xb1\xc1\t
SF:#3R\xf0\x15br\xd1\n\x16\$4\xe1%\xf1\x17\x18\x19\x1a&'\(\)\*56789:CDEFGH
SF:IJSTUVWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\
SF:x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3
SF:\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd
SF:3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\x
SF:f3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\0\x0c\x03\x01\0\x02\x11\x03\x11\
SF:0\?\0\xe2\(\xa2\x8a\0\(\xa2\x8a\0\(\xa2\x8a\0\(\xa2\x8a\0J\)");
MAC Address: 88:49:2D:18:E4:5D (Shenzhen Bilian Electronic，LTD)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.993%E=4%D=11/3%OT=80%CT=1%CU=30706%PV=Y%DS=1%DC=D%G=Y%M=88492D%
OS:TM=6AE9FEAC%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=104%TI=I%CI=I%TS=
OS:7)SEQ(SP=104%GCD=1%ISR=106%TI=I%CI=I%TS=7)SEQ(SP=F7%GCD=1%ISR=F8%TI=I%CI
OS:=I%II=I%SS=S%TS=7)SEQ(SP=F7%GCD=1%ISR=FF%TI=I%CI=I%TS=7)SEQ(SP=FF%GCD=1%
OS:ISR=10B%TI=I%CI=I%TS=7)OPS(O1=M5B4NW0NNT11%O2=M5B4NW0NNT11%O3=M5B4NW0NNT
OS:11%O4=M5B4NW0NNT11%O5=M5B4NW0NNT11%O6=M5B4NNT11)WIN(W1=CBA0%W2=C89C%W3=C
OS:928%W4=C92C%W5=C898%W6=C89F)ECN(R=Y%DF=Y%T=40%W=CD50%O=M5B4NW0%CC=N%Q=)T
OS:1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=Y%DF=Y%T=40%W=C89F%S=O
OS:%A=S+%F=AS%O=M5B4NW0NNT11%RD=0%Q=)T4(R=Y%DF=N%T=40%W=0%S=A%A=Z%F=R%O=%RD
OS:=0%Q=)T5(R=Y%DF=N%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=N%T=40%W=0
OS:%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=N%T=40%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)U1(
OS:R=Y%DF=N%T=40%IPL=38%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=0%RUD=G)IE(R=N)IE(R=
OS:Y%DFI=S%T=40%CD=S)

Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   2.17 ms _gateway (192.168.1.254)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 229.19 seconds
```

```sh
nmap -sV -p 80 --script http-enum,http-title,http-methods,http-server-header 192.168.1.254
Starting Nmap 7.993 ( https://nmap.org ) at 2026-11-03 16:55 +0100
Unable to determine any DNS servers. . Falling back to --system-dns. Specify valid servers with --dns-servers
Nmap scan report for _gateway (192.168.1.254)
Host is up (0.0041s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    hfs/1.00.000
|_http-title: Site doesn't have a title (text/html).
| http-methods:
|_  Supported Methods: GET HEAD
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 200 OK
|     Server: hfs/1.00.000
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Accept-Ranges: bytes
|     Content-Length: 128
|     Content-Type: text/html
|     Connection: close
|     <html>
|     <head><title>Page Not found</title></head>
|     <body><h2>The requested URL was not found on this server.</h2></body>
|     </html>
|   GetRequest:
|     HTTP/1.1 200 OK
|     Server: hfs/1.00.000
|     Cache-Control: no-store, no-cache, must-revalidate
|     Pragma: no-cache
|     Accept-Ranges: bytes
|     Content-Length: 596
|     Content-Type: text/html
|     Connection: close
|     <html>
|     <body>
|     <div id=folderlabel>folder</div>
|     <div id=folder></div>
|     <div id=body>
|     <table cellpadding=5>
|     <th>Filename
|     <th>Filesize
|     <th>Filetime
|     <tr><td colspan="4"><hr size=1 noshade align=top></td></tr></table>
|     <form name=frm action="" method=post enctype="multipart/form-data"><input name=fileupload1 size=70 type=file><br/><input name=upbtn type=submit value="Upload files"></form><form name=frm2 action="?custom=1" method=post enctype="multipart/form-data"><input name=fileupload2 size=70 type=file><br/><input name=upbtn type=submit value="Upload Custom files"></form></div>
|     </body>
|_    </html>
|_http-server-header: hfs/1.00.000
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.993%I=7%D=11/3%Time=6AEA03E3%P=x86_64-pc-linux-gnu%r(Get
SF:Request,31A,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20hfs/1\.00\.000\r\nCac
SF:he-Control:\x20no-store,\x20no-cache,\x20must-revalidate\r\nPragma:\x20
SF:no-cache\r\nAccept-Ranges:\x20bytes\r\nContent-Length:\x20596\r\nConten
SF:t-Type:\x20text/html\r\nConnection:\x20close\r\n\r\n<html>\n<body>\n<di
SF:v\x20id=folderlabel>folder</div>\n<div\x20id=folder></div>\n<div\x20id=
SF:body>\n<table\x20cellpadding=5>\n<th>Filename\n<th>Filesize\n<th>Fileti
SF:me\n<tr><td\x20colspan=\"4\"><hr\x20size=1\x20noshade\x20align=top></td
SF:></tr></table>\n<form\x20name=frm\x20action=\"\"\x20method=post\x20enct
SF:ype=\"multipart/form-data\"><input\x20name=fileupload1\x20size=70\x20ty
SF:pe=file><br/><input\x20name=upbtn\x20type=submit\x20value=\"Upload\x20f
SF:iles\"></form><form\x20name=frm2\x20action=\"\?custom=1\"\x20method=pos
SF:t\x20enctype=\"multipart/form-data\"><input\x20name=fileupload2\x20size
SF:=70\x20type=file><br/><input\x20name=upbtn\x20type=submit\x20value=\"Up
SF:load\x20Custom\x20files\"></form></div>\n</body>\n</html>\n")%r(FourOhF
SF:ourRequest,146,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20hfs/1\.00\.000\r\n
SF:Cache-Control:\x20no-store,\x20no-cache,\x20must-revalidate\r\nPragma:\
SF:x20no-cache\r\nAccept-Ranges:\x20bytes\r\nContent-Length:\x20128\r\nCon
SF:tent-Type:\x20text/html\r\nConnection:\x20close\r\n\r\n<html>\n<head><t
SF:itle>Page\x20Not\x20found</title></head>\n<body><h2>The\x20requested\x2
SF:0URL\x20was\x20not\x20found\x20on\x20this\x20server\.</h2></body>\n</ht
SF:ml>\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 160.22 seconds
```

```sh
curl -s "http://192.168.1.254/?custom=1&cmd=3001"   # active preview, confirme l'API vivante
<?xml version="1.0" encoding="UTF-8" ?>
<Function>
<Cmd>3001</Cmd>
<Status>-21</Status>
</Function>%                                                                               ```

```sh
curl -s "http://192.168.1.254/?custom=1&cmd=2000"   # dump config système (réso, freq, wifi)
<?xml version="1.0" encoding="UTF-8" ?>
<Function>
<Cmd>2000</Cmd>
<Status>-256</Status>
</Function>%                                                                               ```

```sh
curl -s "http://192.168.1.254/?custom=1&cmd=4000"   # listing SD
<?xml version="1.0" encoding="UTF-8" ?>
<Function>
<Cmd>4000</Cmd>
<Status>-256</Status>
</Function>%   
```

% TODO: Fuzz API commands
```sh
for c in $(seq 2000 4100); do
  s=$(curl -s --max-time 2 "http://192.168.1.254/?custom=1&cmd=$c" \
      | sed -n 's:.*<Status>\(-\?[0-9]*\)</Status>.*:\1:p')
  [ "$s" != "-256" ] && printf "cmd=%-5s status=%s\n" "$c" "$s"
done
```
-> Crash

```sh
# 1. Une seule connexion à la fois, petite cadence, sur une sous-plage
for c in $(seq 2000 2050); do
  s=$(curl -s --max-time 2 "http://192.168.1.254/?custom=1&cmd=$c" \
      | sed -n 's:.*<Status>\(-\?[0-9]*\)</Status>.*:\1:p')
  echo "cmd=$c status=${s:-TIMEOUT/CRASH}"
  sleep 0.3
done
```

## GitHub Resource

% TODO: Explore

https://github.com/rsphysics/ascope
https://github.com/sdawans/andonstar-open-viewer-android
https://github.com/francescodalsavio/andonstar-bridge
https://github.com/therealdreg/AndonstarOSWV
https://github.com/cloudspotter-Eng/MeasureView-WiScope-AD409

## Reverse Engineering

% TODO

SoC: Novatek NTK96550 (https://www.novatek.com.tw)
Wi-Fi: Shenzhen Bilian Electronic (From MAC address)
% TODO: identify exact model (Realtek RTL8188/8189 ?)

% TODO: Explore UART (A17/B16 pins)
% TODO: Explore JTAG/GPIO (R17/N14/P17/P18/P19 pins)

OS: eCos/1.0 (nmap fingerprint)
https://www.ecoscentric.com/ecos
https://ecos.sourceware.org/

### Commands

```
Wi-Fi Command strings for Andonstar AD409 microscope (uses a Novatek camera and chipset) some found from online sources, others by probing it with Wireshark and browser.  example command - http://192.168.1.254/?custom=1&cmd=2001&par=0  entered into browser address bar. Note microscope buttons are disabled when connected to Wi-Fi. 
Preview streaming  is started by http://192.168.1.254:8192, this is a  low res MJpeg stream ( 640x380 in vid mode and 640x 480 photo mode at ~ 10-30 fps) is active when a device is listening on that port, it hogs 75% of the Wi-Fi bandwidth so downloading files from SD whilst this is active is far slower. To use photo snapshot - (jpg)  or record video- (mp4 format) will need to insert quality class 10 SD card, there is no way to stream the full resolution video live over Wi-Fi using the current microscope firmware . One way to achieve this would be by using small local pc or raspberry-pi 4/5 with HDMI capture dongle fed from the Scopes HDMI output (this disables the scopes own screen so would need another local display if that was needed).
notes 1 :
No direct way to query mode status of scope over WiFi but workaround is first check and/or stop any video recording cmd=2001 , we can then use video snapshot cmd (cmd=2017) (since not recording it wont take a snapshot) that will  return a status value that can tell us what mode AD409 is currently in .
The firmware isn't that good and has many quirks and glitches (e.g., can't delete files that have spaces in the names and many others) that needed workarounds to get smooth Wi-Fi control, Maybe this was why Andonstar declared Wi-fi as an 'experimental' feature.
notes 2 :  Some Wi-Fi commands, e.g., record movie to SD card (cmd=2001par=0 or 1), sometimes take immediate effect when the command is typed in a browser but not yet entered with the return key. 
  
example format of a Wi Fi command packet sent by browser-       HTTP	GET /?custom=1&cmd=2001&par=0 HTTP/1.1  par=0 stop or par=1 start recording to SD.
 List of uncovered commands . 
  cmd=          par=           function
 1001           0,1...       Takes a photo returns photo name , works only when in photo mode (3001 par=0),  will use resolution set by cmd 1002.
 1002        0...10          Photo resolution 0=24M 1=20M 2=16M 3=12M 4=10M 5=8M 6=2592x1944 7=2048x1536 8=(1920 x 1080 16:9) 9=640x480 10=1280x960  can be changed in any mode.
 1003                        Return <value>= freepic space number countdown

 2001           1,0          record movie to SD on/off (Res will be whatever Resolution was set at scope unless overridden) <status =2 means already off ?>
 2002     0,1,5,6,8,9,10     Set video  Resolution  0= 2880 X 2160 (24fps), 1 = 2560 x 1440 (30fps) , 5= 1920 x 1080  (60fps), 6= 1920 x 1080 (30fps) ,8 = 1280x 720 (120fps) , 9= 1280 x 720 (60fps) , 10=1280 x 720 (30fps) , can only be changed when in video mode. 
 2003                         loop record 0=off , 3 = 3min , 4 = 5min, 5 = 10minute
 2004           0,1          contrast/brightness ? only seems to be 2 settings.  ? set hdr ?
 2005           1-12         Exposure 0 is lightest 12 darkest - default = 6
 2006           1,0          set Motion detect  on/off starts recording for 10 seconds when the image moves 
 2007                        No obvious function  .status no change . (is audio on/off on webcams)
 2008           1,0          Set date watermark on/off
 2009                        returns <value> max recording time with current bitrate ?
 0210                        ? movie live view size ?  returns <-256> error status
 2012           1,0          Set wifi AutoRecording on/off this doesn't seem to have any visible effect .
 2013                       Crashes scope ?  movie record bitrate kb/s ?
 2014                       Crashes scope ? movie liveview bitrate kb/s ? 
 2015           1,0         ? start/stop liveview ? no effect 
 2016,3016                  start and end of streamed frames ? shows current movie record time in sec ?
 2017                       Take/save video Snapshot  par doesn't matter  (1980 x 1024 max res), must be currently recording to SD (cmd2001) for this to work .statuses returned 0,1 taken ok , -13 failed not currently recording , -22 failed not in video mode 
 2018                       No obvious effect returns blank screen ? get raw movie, or save snapshot file ?
 2019                       returns a liveviewinglink address always to ip:8192 ?
 2020          0,1,2,3,4    Camera brightness or contrast I believe (this has 4 settings contrast has 3 settings exposure has ~10)
 2021            0           No change in status or effect noticeable 
 2023          0,1,2,3       1= flip image horizontally , 2= flip  vertically, 3= rotate image 180
 2024          0,1,2,3,4    Set video Resolution  0 = 1920 X 1080 (60fps), 1 = 1280 X 738 (30fps), 2 = 864 x 480 (30fps), 3= 640x480 (30fps 4:3), 4= 320x240 (30fps) .Any video Snapshots will be caught at same res as movie.
 2025                       No obvious function ? bitrate control ?
 2026                       No obvious effect ? rtsp audio stream control on webcams ?


3001           0,1,2        scope modes- 0 photo (res set by 1002), 1 video (also snapshot when recording) , 2 view files (this mode stops the preview stream),  (in photo mode 2017 2001 don't  work)
3002                        list of possible cmd's
3003                        Crashed scope (par0) ? set ssid ? 
3004                        Crashed scope (par0)  ? set passphrase ?
3005                        set date   str=date    yy-mm-dd
3006                        set time   str=time    hh-mm-ss
3007                        Turns on a auto power down after being on for a set period 
3008          0...6         Language Setting 0= English 
3009                         Frequency 50/60 hz ?
3010           0,1          FORMATS SD card (without warning) (par=1)
3011                        Reset to factory Default settings 
3012                        Returns string=scope model family and scope version
3013          0,1           Firmware Update! returns <status -15> ?   
3014                        Returns a list of some commands and statuses .         ?    
3015                        returns file list in movies dir (when in video mode) or all files when in in other modes 
3016                        ? ping camera ?
3017                        Returns two long <values> ? get sd card space ?
3018       0,1              Wifi off/on  
3019                        No noticeable function returns <value=5>, ? battery state on webcams ?
3020                        no noticeable effect returns <status> -256 ? socket port 3333 error status ?
3021                        No obvious function ? save all settings to sd card  ?
3022                        No obvious function ? get HW capacity ?
3023                        No obvious function ? remove last user for some web cams ?
3024                        No obvious function ? get SD card status .<Value> 0=none 1=ins 2=locked
3025                        Returns   <String>http://115.29.201.46:8020/download/filedesc.xml 
3026                        Returns   <String>http://192.168.1.254/FWAD400A.BIN</String>
3027                        upload file to SD card
3028       0,1,2            freezes/unfreeze display, this has no effect on recording/snapshot, status cycles 0-2 every time written to  
3029                        return wifi SSID and Password .
3030                        returns a list of video mode screen resolutions and frame rates and types .
3031                        str=all      ? return more cmnds ?
3032                        Froze scope ? set up microscope for wifi client mode SSID:psw  ? e.g., http://192.168.1.254/?custom=1&cmd=3032&str=SSID:PASSWORD
3033                        Not tried yet, turn on client mode (Default is A.P/Server mode), restart wifi using 3018 st=0 ?
3034                        No noticable so function unknown

3037                        No noticeable so function unknown
3038          0,1           Returns a list of scanned wifi networks available.

4001                        display files/thumbnail ?
4002                         ? file path string  get screen preview ?
4003                        str=file name   delete 1 file
4004                        delete all files 
5001                        displays a version of previous cmd output with an encoding error message ? upload file for some webcams ?.  

8003                        Returns message 'no A:\test.htm file'  , 
8004                        Returns list of information about scope and versions info sdk mac address etc .
8008                        no obvious function, returns <status>=256 
8072                        No obvious function
8073                                     ?
```
