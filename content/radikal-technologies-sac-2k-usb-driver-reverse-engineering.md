Title: Radikal Technologies SAC-2K USB driver reverse engineering
Date: 2010-10-13 12:29
Category: Blog
Tags: Hardware, Reverse Engineering, GNU/Linux, MIDI, qemu, Radikal Technologies, SAC-2K, SysEx, USB, usbmon, wireshark
Slug: radikal-technologies-sac-2k-usb-driver-reverse-engineering
Status: published

I've started reverse engineering the windows USB driver using qemu,
wireshark and the linux usbmon interface in order to hopefully write a
Linux driver for this device.

Here's the commented out first sniffed traffic :

    No. Time Source Destination Protocol Info  
      
    3 0.013662 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 3 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cdb4ad40  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 40  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 4\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 28 00 00 00 00 00 00 00 00 00 ......(.........  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    4 0.025242 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 4 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cdb4ad40  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 3\]  
      
    \[Time from request: 0.011580000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    9 31.068508 9.1 host USB URB\_INTERRUPT
    
    Frame 9 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800560b4380  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: No such file or directory (-ENOENT) (-2)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    30 36.381704 host 0.0 USB SET ADDRESS Request
    
    Frame 30 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 31\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    32 36.591698 host 0.0 USB SET ADDRESS Request
    
    Frame 32 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 33\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    56 36.969618 host 0.0 USB SET ADDRESS Request
    
    Frame 56 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 57\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    64 37.180637 host 0.0 USB SET ADDRESS Request
    
    Frame 64 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 65\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    84 37.468553 host 0.0 USB SET ADDRESS Request
    
    Frame 84 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 85\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    92 37.678633 host 0.0 USB SET ADDRESS Request
    
    Frame 92 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800df96a840  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 93\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    110 37.965467 host 0.0 USB SET ADDRESS Request
    
    Frame 110 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 111\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    114 37.983618 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 114 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 115\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 08 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    115 37.991450 9.0 host USB GET DESCRIPTOR Response DEVICE\[Malformed
    Packet\]
    
    Frame 115 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 114\]  
      
    \[Time from request: 0.007832000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    \[Malformed Packet: USB\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................
    
    No. Time Source Destination Protocol Info  
      
    116 37.993447 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 116 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 117\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    117 38.007447 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 117 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 116\]  
      
    \[Time from request: 0.014000000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    118 38.007456 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 118 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd97f900  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 87 Data length \[bytes\]: 0
    \[Response in: 122\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 80 06 00 02 00 00 57 00 00 00 00 00 00 00 00 00
    ......W......... 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 122 38.046440 9.0 host USB GET DESCRIPTOR
    Response CONFIGURATION Frame 122 (111 bytes on wire, 111 bytes captured)
    USB URB URB id: 0xffff8800cd97f900 URB type: URB\_COMPLETE ('C') URB
    transfer type: URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Success (0) URB length \[bytes\]: 87 Data length \[bytes\]: 87 \[Request
    in: 118\] \[Time from request: 0.038984000 seconds\] \[bInterfaceClass:
    VENDOR\_SPECIFIC (0xff)\] CONFIGURATION DESCRIPTOR bLength: 9
    bDescriptorType: CONFIGURATION (2) wTotalLength: 87 bNumInterfaces: 3
    bConfigurationValue: 1 iConfiguration: 4 Configuration bmAttributes:
    0xc0 SELF-POWERED NO REMOTE-WAKEUP bMaxPower: 0 (0mA) INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 0
    bAlternateSetting: 0 bNumEndpoints: 0 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 0
    INTERFACE DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4)
    bInterfaceNumber: 1 bAlternateSetting: 0 bNumEndpoints: 0
    bInterfaceClass: VENDOR\_SPECIFIC (0xff) bInterfaceSubClass: 0xff
    bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT DESCRIPTOR bLength: 7
    bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x81 IN Endpoint:1
    bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 ENDPOINT DESCRIPTOR
    bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x01 OUT
    Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 2
    bAlternateSetting: 0 bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 6
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x81 IN Endpoint:1 bmAttributes: 0x03 wMaxPacketSize:
    8 bInterval: 1 ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT
    (5) bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x03
    wMaxPacketSize: 8 bInterval: 1 INTERFACE DESCRIPTOR bLength: 9
    bDescriptorType: INTERFACE (4) bInterfaceNumber: 2 bAlternateSetting: 1
    bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC (0xff)
    bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT
    DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress:
    0x81 IN Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x02 wMaxPacketSize:
    8 bInterval: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0
    ..........W..... 0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff
    ................ 0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00
    ................ 0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00
    ................ 0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00
    ................ 0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01
    ............... No. Time Source Destination Protocol Info 123 38.046449
    host 9.0 USB SET CONFIGURATION Request Frame 123 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800cd97f900 URB type: URB\_SUBMIT
    ('S') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB
    bus id: 8 Device setup request: present (0) Data: present (0) URB
    status: Operation now in progress (-EINPROGRESS) (-115) URB length
    \[bytes\]: 0 Data length \[bytes\]: 0 \[Response in: 127\]
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB setup 0000 00 09 01 00
    00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00
    00 00 00 ........ No. Time Source Destination Protocol Info 127
    38.060439 9.0 host USB SET CONFIGURATION Response Frame 127 (24 bytes on
    wire, 24 bytes captured) USB URB URB id: 0xffff8800cd97f900 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 123\]  
      
    \[Time from request: 0.013990000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    146 43.113675 host 0.0 USB SET ADDRESS Request
    
    Frame 146 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800b5bdd2c0  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 147\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    148 43.132616 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 148 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800b5bdd2c0  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 149\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    149 43.145663 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 149 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800b5bdd2c0  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 148\]  
      
    \[Time from request: 0.013047000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    150 43.145670 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 150 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800b5bdd2c0  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 87 Data length \[bytes\]: 0
    \[Response in: 151\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 80 06 00 02 00 00 57 00 00 00 00 00 00 00 00 00
    ......W......... 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 151 43.184658 9.0 host USB GET DESCRIPTOR
    Response CONFIGURATION Frame 151 (111 bytes on wire, 111 bytes captured)
    USB URB URB id: 0xffff8800b5bdd2c0 URB type: URB\_COMPLETE ('C') URB
    transfer type: URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Success (0) URB length \[bytes\]: 87 Data length \[bytes\]: 87 \[Request
    in: 150\] \[Time from request: 0.038988000 seconds\] \[bInterfaceClass:
    VENDOR\_SPECIFIC (0xff)\] CONFIGURATION DESCRIPTOR bLength: 9
    bDescriptorType: CONFIGURATION (2) wTotalLength: 87 bNumInterfaces: 3
    bConfigurationValue: 1 iConfiguration: 4 Configuration bmAttributes:
    0xc0 SELF-POWERED NO REMOTE-WAKEUP bMaxPower: 0 (0mA) INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 0
    bAlternateSetting: 0 bNumEndpoints: 0 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 0
    INTERFACE DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4)
    bInterfaceNumber: 1 bAlternateSetting: 0 bNumEndpoints: 0
    bInterfaceClass: VENDOR\_SPECIFIC (0xff) bInterfaceSubClass: 0xff
    bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT DESCRIPTOR bLength: 7
    bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x81 IN Endpoint:1
    bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 ENDPOINT DESCRIPTOR
    bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x01 OUT
    Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 2
    bAlternateSetting: 0 bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 6
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x81 IN Endpoint:1 bmAttributes: 0x03 wMaxPacketSize:
    8 bInterval: 1 ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT
    (5) bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x03
    wMaxPacketSize: 8 bInterval: 1 INTERFACE DESCRIPTOR bLength: 9
    bDescriptorType: INTERFACE (4) bInterfaceNumber: 2 bAlternateSetting: 1
    bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC (0xff)
    bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT
    DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress:
    0x81 IN Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x02 wMaxPacketSize:
    8 bInterval: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0
    ..........W..... 0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff
    ................ 0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00
    ................ 0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00
    ................ 0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00
    ................ 0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01
    ............... No. Time Source Destination Protocol Info 152 43.184668
    host 9.0 USB SET CONFIGURATION Request Frame 152 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800b5bdd2c0 URB type: URB\_SUBMIT
    ('S') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB
    bus id: 8 Device setup request: present (0) Data: present (0) URB
    status: Operation now in progress (-EINPROGRESS) (-115) URB length
    \[bytes\]: 0 Data length \[bytes\]: 0 \[Response in: 153\]
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB setup 0000 00 09 01 00
    00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00
    00 00 00 ........ No. Time Source Destination Protocol Info 153
    43.193655 9.0 host USB SET CONFIGURATION Response Frame 153 (24 bytes on
    wire, 24 bytes captured) USB URB URB id: 0xffff8800b5bdd2c0 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 152\]  
      
    \[Time from request: 0.008987000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    172 44.161522 host 0.0 USB SET ADDRESS Request
    
    Frame 172 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 173\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    174 44.179616 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 174 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 175\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    175 44.193505 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 175 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 174\]  
      
    \[Time from request: 0.013889000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    176 44.193514 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 176 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 87 Data length \[bytes\]: 0
    \[Response in: 177\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 80 06 00 02 00 00 57 00 00 00 00 00 00 00 00 00
    ......W......... 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 177 44.232503 9.0 host USB GET DESCRIPTOR
    Response CONFIGURATION Frame 177 (111 bytes on wire, 111 bytes captured)
    USB URB URB id: 0xffff8800c3360680 URB type: URB\_COMPLETE ('C') URB
    transfer type: URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Success (0) URB length \[bytes\]: 87 Data length \[bytes\]: 87 \[Request
    in: 176\] \[Time from request: 0.038989000 seconds\] \[bInterfaceClass:
    VENDOR\_SPECIFIC (0xff)\] CONFIGURATION DESCRIPTOR bLength: 9
    bDescriptorType: CONFIGURATION (2) wTotalLength: 87 bNumInterfaces: 3
    bConfigurationValue: 1 iConfiguration: 4 Configuration bmAttributes:
    0xc0 SELF-POWERED NO REMOTE-WAKEUP bMaxPower: 0 (0mA) INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 0
    bAlternateSetting: 0 bNumEndpoints: 0 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 0
    INTERFACE DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4)
    bInterfaceNumber: 1 bAlternateSetting: 0 bNumEndpoints: 0
    bInterfaceClass: VENDOR\_SPECIFIC (0xff) bInterfaceSubClass: 0xff
    bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT DESCRIPTOR bLength: 7
    bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x81 IN Endpoint:1
    bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 ENDPOINT DESCRIPTOR
    bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x01 OUT
    Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 2
    bAlternateSetting: 0 bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 6
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x81 IN Endpoint:1 bmAttributes: 0x03 wMaxPacketSize:
    8 bInterval: 1 ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT
    (5) bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x03
    wMaxPacketSize: 8 bInterval: 1 INTERFACE DESCRIPTOR bLength: 9
    bDescriptorType: INTERFACE (4) bInterfaceNumber: 2 bAlternateSetting: 1
    bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC (0xff)
    bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT
    DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress:
    0x81 IN Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x02 wMaxPacketSize:
    8 bInterval: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0
    ..........W..... 0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff
    ................ 0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00
    ................ 0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00
    ................ 0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00
    ................ 0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01
    ............... No. Time Source Destination Protocol Info 178 44.232515
    host 9.0 USB SET CONFIGURATION Request Frame 178 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800c3360680 URB type: URB\_SUBMIT
    ('S') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB
    bus id: 8 Device setup request: present (0) Data: present (0) URB
    status: Operation now in progress (-EINPROGRESS) (-115) URB length
    \[bytes\]: 0 Data length \[bytes\]: 0 \[Response in: 179\]
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB setup 0000 00 09 01 00
    00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00
    00 00 00 ........ No. Time Source Destination Protocol Info 179
    44.241496 9.0 host USB SET CONFIGURATION Response Frame 179 (24 bytes on
    wire, 24 bytes captured) USB URB URB id: 0xffff8800c3360680 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 178\]  
      
    \[Time from request: 0.008981000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    180 44.511896 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 180 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 64  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 181\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 40 00 00 00 00 00 00 00 00 00 ......@.........  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    181 44.524464 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 181 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 180\]  
      
    \[Time from request: 0.012568000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    200 44.695437 host 0.0 USB SET ADDRESS Request
    
    Frame 200 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 201\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    202 44.904614 host 0.0 USB SET ADDRESS Request
    
    Frame 202 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 203\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    226 45.278345 host 0.0 USB SET ADDRESS Request
    
    Frame 226 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 0  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 227\]  
      
    \[bInterfaceClass: Unknown (0xffff)\]  
      
    URB setup
    
    0000 00 05 09 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    228 45.296625 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 228 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 229\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    229 45.309333 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 229 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 228\]  
      
    \[Time from request: 0.012708000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    230 45.309339 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 230 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 87 Data length \[bytes\]: 0
    \[Response in: 237\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 80 06 00 02 00 00 57 00 00 00 00 00 00 00 00 00
    ......W......... 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 237 45.357325 9.0 host USB GET DESCRIPTOR
    Response CONFIGURATION Frame 237 (111 bytes on wire, 111 bytes captured)
    USB URB URB id: 0xffff8800c3360680 URB type: URB\_COMPLETE ('C') URB
    transfer type: URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Success (0) URB length \[bytes\]: 87 Data length \[bytes\]: 87 \[Request
    in: 230\] \[Time from request: 0.047986000 seconds\] \[bInterfaceClass:
    VENDOR\_SPECIFIC (0xff)\] CONFIGURATION DESCRIPTOR bLength: 9
    bDescriptorType: CONFIGURATION (2) wTotalLength: 87 bNumInterfaces: 3
    bConfigurationValue: 1 iConfiguration: 4 Configuration bmAttributes:
    0xc0 SELF-POWERED NO REMOTE-WAKEUP bMaxPower: 0 (0mA) INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 0
    bAlternateSetting: 0 bNumEndpoints: 0 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 0
    INTERFACE DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4)
    bInterfaceNumber: 1 bAlternateSetting: 0 bNumEndpoints: 0
    bInterfaceClass: VENDOR\_SPECIFIC (0xff) bInterfaceSubClass: 0xff
    bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT DESCRIPTOR bLength: 7
    bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x81 IN Endpoint:1
    bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 ENDPOINT DESCRIPTOR
    bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x01 OUT
    Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 2
    bAlternateSetting: 0 bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 6
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x81 IN Endpoint:1 bmAttributes: 0x03 wMaxPacketSize:
    8 bInterval: 1 ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT
    (5) bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x03
    wMaxPacketSize: 8 bInterval: 1 INTERFACE DESCRIPTOR bLength: 9
    bDescriptorType: INTERFACE (4) bInterfaceNumber: 2 bAlternateSetting: 1
    bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC (0xff)
    bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT
    DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress:
    0x81 IN Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x02 wMaxPacketSize:
    8 bInterval: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0
    ..........W..... 0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff
    ................ 0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00
    ................ 0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00
    ................ 0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00
    ................ 0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01
    ............... No. Time Source Destination Protocol Info 238 45.357333
    host 9.0 USB SET CONFIGURATION Request Frame 238 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800c3360680 URB type: URB\_SUBMIT
    ('S') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB
    bus id: 8 Device setup request: present (0) Data: present (0) URB
    status: Operation now in progress (-EINPROGRESS) (-115) URB length
    \[bytes\]: 0 Data length \[bytes\]: 0 \[Response in: 239\]
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB setup 0000 00 09 01 00
    00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00
    00 00 00 ........ No. Time Source Destination Protocol Info 239
    45.367323 9.0 host USB SET CONFIGURATION Response Frame 239 (24 bytes on
    wire, 24 bytes captured) USB URB URB id: 0xffff8800c3360680 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 238\]  
      
    \[Time from request: 0.009990000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    240 45.479655 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 240 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 241\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    241 45.491316 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 241 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 240\]  
      
    \[Time from request: 0.011661000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    242 45.498031 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 242 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 9  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 243\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 02 00 00 09 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    243 45.505311 9.0 host USB GET DESCRIPTOR Response CONFIGURATION
    
    Frame 243 (33 bytes on wire, 33 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 9  
      
    Data length \[bytes\]: 9  
      
    \[Request in: 242\]  
      
    \[Time from request: 0.007280000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    CONFIGURATION DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: CONFIGURATION (2)  
      
    wTotalLength: 87  
      
    bNumInterfaces: 3  
      
    bConfigurationValue: 1  
      
    iConfiguration: 4  
      
    Configuration bmAttributes: 0xc0 SELF-POWERED NO REMOTE-WAKEUP  
      
    bMaxPower: 0 (0mA)
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0 ..........W.....  
      
    0020 00 .
    
    No. Time Source Destination Protocol Info  
      
    244 45.511259 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 244 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 255  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 245\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 02 00 00 ff 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    245 45.546300 9.0 host USB GET DESCRIPTOR Response CONFIGURATION
    
    Frame 245 (111 bytes on wire, 111 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 87  
      
    Data length \[bytes\]: 87  
      
    \[Request in: 244\]  
      
    \[Time from request: 0.035041000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    CONFIGURATION DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: CONFIGURATION (2)  
      
    wTotalLength: 87  
      
    bNumInterfaces: 3  
      
    bConfigurationValue: 1  
      
    iConfiguration: 4  
      
    Configuration bmAttributes: 0xc0 SELF-POWERED NO REMOTE-WAKEUP  
      
    bMaxPower: 0 (0mA)  
      
    INTERFACE DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: INTERFACE (4)  
      
    bInterfaceNumber: 0  
      
    bAlternateSetting: 0  
      
    bNumEndpoints: 0  
      
    bInterfaceClass: VENDOR\_SPECIFIC (0xff)  
      
    bInterfaceSubClass: 0xff  
      
    bInterfaceProtocol: 0x00  
      
    iInterface: 0  
      
    INTERFACE DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: INTERFACE (4)  
      
    bInterfaceNumber: 1  
      
    bAlternateSetting: 0  
      
    bNumEndpoints: 0  
      
    bInterfaceClass: VENDOR\_SPECIFIC (0xff)  
      
    bInterfaceSubClass: 0xff  
      
    bInterfaceProtocol: 0x00  
      
    iInterface: 5  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x81 IN Endpoint:1  
      
    bmAttributes: 0x02  
      
    wMaxPacketSize: 8  
      
    bInterval: 1  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x01 OUT Endpoint:1  
      
    bmAttributes: 0x02  
      
    wMaxPacketSize: 8  
      
    bInterval: 1  
      
    INTERFACE DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: INTERFACE (4)  
      
    bInterfaceNumber: 2  
      
    bAlternateSetting: 0  
      
    bNumEndpoints: 2  
      
    bInterfaceClass: VENDOR\_SPECIFIC (0xff)  
      
    bInterfaceSubClass: 0xff  
      
    bInterfaceProtocol: 0x00  
      
    iInterface: 6  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x81 IN Endpoint:1  
      
    bmAttributes: 0x03  
      
    wMaxPacketSize: 8  
      
    bInterval: 1  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x01 OUT Endpoint:1  
      
    bmAttributes: 0x03  
      
    wMaxPacketSize: 8  
      
    bInterval: 1  
      
    INTERFACE DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: INTERFACE (4)  
      
    bInterfaceNumber: 2  
      
    bAlternateSetting: 1  
      
    bNumEndpoints: 2  
      
    bInterfaceClass: VENDOR\_SPECIFIC (0xff)  
      
    bInterfaceSubClass: 0xff  
      
    bInterfaceProtocol: 0x00  
      
    iInterface: 5  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x81 IN Endpoint:1  
      
    bmAttributes: 0x02  
      
    wMaxPacketSize: 8  
      
    bInterval: 1  
      
    ENDPOINT DESCRIPTOR  
      
    bLength: 7  
      
    bDescriptorType: ENDPOINT (5)  
      
    bEndpointAddress: 0x01 OUT Endpoint:1  
      
    bmAttributes: 0x02  
      
    wMaxPacketSize: 8  
      
    bInterval: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0 ..........W.....  
      
    0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff ................  
      
    0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00 ................  
      
    0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00 ................  
      
    0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00 ................  
      
    0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01 ...............
    
    No. Time Source Destination Protocol Info  
      
    246 45.563202 host 9.0 USB GET DESCRIPTOR Request STRING
    
    Frame 246 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 255  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 247\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 03 00 00 ff 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    247 45.569297 9.0 host USB GET DESCRIPTOR Response STRING
    
    Frame 247 (28 bytes on wire, 28 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 4  
      
    Data length \[bytes\]: 4  
      
    \[Request in: 246\]  
      
    \[Time from request: 0.006095000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    STRING DESCRIPTOR  
      
    bLength: 4  
      
    bDescriptorType: STRING (3)  
      
    wLANGID: English (United States) (0x0409)
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 04 03 09 04 ............
    
    No. Time Source Destination Protocol Info  
      
    248 45.574438 host 9.0 USB GET DESCRIPTOR Request STRING
    
    Frame 248 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 255  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 249\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 02 03 09 04 ff 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    249 45.603291 9.0 host USB GET DESCRIPTOR Response STRING
    
    Frame 249 (94 bytes on wire, 94 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 70  
      
    Data length \[bytes\]: 70  
      
    \[Request in: 248\]  
      
    \[Time from request: 0.028853000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    STRING DESCRIPTOR  
      
    bLength: 70  
      
    bDescriptorType: STRING (3)  
      
    bString: SAC - Software Assigned Controller
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 46 03 53 00 41 00 43 00 ........F.S.A.C.  
      
    0020 20 00 2d 00 20 00 53 00 6f 00 66 00 74 00 77 00 .-. .S.o.f.t.w.  
      
    0030 61 00 72 00 65 00 20 00 41 00 73 00 73 00 69 00 a.r.e. .A.s.s.i.  
      
    0040 67 00 6e 00 65 00 64 00 20 00 43 00 6f 00 6e 00 g.n.e.d. .C.o.n.  
      
    0050 74 00 72 00 6f 00 6c 00 6c 00 65 00 72 00 t.r.o.l.l.e.r.
    
    No. Time Source Destination Protocol Info  
      
    250 45.617274 host 9.0 USB GET DESCRIPTOR Request STRING
    
    Frame 250 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 255  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 251\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 03 00 00 ff 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    251 45.624287 9.0 host USB GET DESCRIPTOR Response STRING
    
    Frame 251 (28 bytes on wire, 28 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 4  
      
    Data length \[bytes\]: 4  
      
    \[Request in: 250\]  
      
    \[Time from request: 0.007013000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    STRING DESCRIPTOR  
      
    bLength: 4  
      
    bDescriptorType: STRING (3)  
      
    wLANGID: English (United States) (0x0409)
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 04 03 09 04 ............
    
    No. Time Source Destination Protocol Info  
      
    252 45.629572 host 9.0 USB GET DESCRIPTOR Request STRING
    
    Frame 252 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 255  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 253\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 02 03 09 04 ff 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    253 45.658282 9.0 host USB GET DESCRIPTOR Response STRING
    
    Frame 253 (94 bytes on wire, 94 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 70  
      
    Data length \[bytes\]: 70  
      
    \[Request in: 252\]  
      
    \[Time from request: 0.028710000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    STRING DESCRIPTOR  
      
    bLength: 70  
      
    bDescriptorType: STRING (3)  
      
    bString: SAC - Software Assigned Controller
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 46 03 53 00 41 00 43 00 ........F.S.A.C.  
      
    0020 20 00 2d 00 20 00 53 00 6f 00 66 00 74 00 77 00 .-. .S.o.f.t.w.  
      
    0030 61 00 72 00 65 00 20 00 41 00 73 00 73 00 69 00 a.r.e. .A.s.s.i.  
      
    0040 67 00 6e 00 65 00 64 00 20 00 43 00 6f 00 6e 00 g.n.e.d. .C.o.n.  
      
    0050 74 00 72 00 6f 00 6c 00 6c 00 65 00 72 00 t.r.o.l.l.e.r.
    
    No. Time Source Destination Protocol Info  
      
    254 45.684797 host 9.0 USB GET DESCRIPTOR Request DEVICE
    
    Frame 254 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 255\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 01 00 00 12 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    255 45.696277 9.0 host USB GET DESCRIPTOR Response DEVICE
    
    Frame 255 (42 bytes on wire, 42 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 18  
      
    Data length \[bytes\]: 18  
      
    \[Request in: 254\]  
      
    \[Time from request: 0.011480000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    DEVICE DESCRIPTOR  
      
    bLength: 18  
      
    bDescriptorType: DEVICE (1)  
      
    bcdUSB: 0x0100  
      
    bDeviceClass: 255  
      
    bDeviceSubClass: 0  
      
    bDeviceProtocol: 255  
      
    bMaxPacketSize0: 8  
      
    idVendor: 0x0a35  
      
    idProduct: 0x002a  
      
    bcdDevice: 0x0200  
      
    iManufacturer: 1  
      
    iProduct: 2  
      
    iSerialNumber: 0  
      
    bNumConfigurations: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 12 01 00 01 ff 00 ff 08 ................  
      
    0020 35 0a 2a 00 00 02 01 02 00 01 5.\*.......
    
    No. Time Source Destination Protocol Info  
      
    256 45.705223 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 256 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 9  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 257\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 06 00 02 00 00 09 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    257 45.713273 9.0 host USB GET DESCRIPTOR Response CONFIGURATION
    
    Frame 257 (33 bytes on wire, 33 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 9  
      
    Data length \[bytes\]: 9  
      
    \[Request in: 256\]  
      
    \[Time from request: 0.008050000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    CONFIGURATION DESCRIPTOR  
      
    bLength: 9  
      
    bDescriptorType: CONFIGURATION (2)  
      
    wTotalLength: 87  
      
    bNumInterfaces: 3  
      
    bConfigurationValue: 1  
      
    iConfiguration: 4  
      
    Configuration bmAttributes: 0xc0 SELF-POWERED NO REMOTE-WAKEUP  
      
    bMaxPower: 0 (0mA)
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0 ..........W.....  
      
    0020 00 .
    
    No. Time Source Destination Protocol Info  
      
    258 45.718465 host 9.0 USB GET DESCRIPTOR Request CONFIGURATION
    
    Frame 258 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 87 Data length \[bytes\]: 0
    \[Response in: 259\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 80 06 00 02 00 00 57 00 00 00 00 00 00 00 00 00
    ......W......... 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 259 45.752268 9.0 host USB GET DESCRIPTOR
    Response CONFIGURATION Frame 259 (111 bytes on wire, 111 bytes captured)
    USB URB URB id: 0xffff8800c3360680 URB type: URB\_COMPLETE ('C') URB
    transfer type: URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Success (0) URB length \[bytes\]: 87 Data length \[bytes\]: 87 \[Request
    in: 258\] \[Time from request: 0.033803000 seconds\] \[bInterfaceClass:
    VENDOR\_SPECIFIC (0xff)\] CONFIGURATION DESCRIPTOR bLength: 9
    bDescriptorType: CONFIGURATION (2) wTotalLength: 87 bNumInterfaces: 3
    bConfigurationValue: 1 iConfiguration: 4 Configuration bmAttributes:
    0xc0 SELF-POWERED NO REMOTE-WAKEUP bMaxPower: 0 (0mA) INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 0
    bAlternateSetting: 0 bNumEndpoints: 0 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 0
    INTERFACE DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4)
    bInterfaceNumber: 1 bAlternateSetting: 0 bNumEndpoints: 0
    bInterfaceClass: VENDOR\_SPECIFIC (0xff) bInterfaceSubClass: 0xff
    bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT DESCRIPTOR bLength: 7
    bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x81 IN Endpoint:1
    bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 ENDPOINT DESCRIPTOR
    bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress: 0x01 OUT
    Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1 INTERFACE
    DESCRIPTOR bLength: 9 bDescriptorType: INTERFACE (4) bInterfaceNumber: 2
    bAlternateSetting: 0 bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC
    (0xff) bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 6
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x81 IN Endpoint:1 bmAttributes: 0x03 wMaxPacketSize:
    8 bInterval: 1 ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT
    (5) bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x03
    wMaxPacketSize: 8 bInterval: 1 INTERFACE DESCRIPTOR bLength: 9
    bDescriptorType: INTERFACE (4) bInterfaceNumber: 2 bAlternateSetting: 1
    bNumEndpoints: 2 bInterfaceClass: VENDOR\_SPECIFIC (0xff)
    bInterfaceSubClass: 0xff bInterfaceProtocol: 0x00 iInterface: 5 ENDPOINT
    DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5) bEndpointAddress:
    0x81 IN Endpoint:1 bmAttributes: 0x02 wMaxPacketSize: 8 bInterval: 1
    ENDPOINT DESCRIPTOR bLength: 7 bDescriptorType: ENDPOINT (5)
    bEndpointAddress: 0x01 OUT Endpoint:1 bmAttributes: 0x02 wMaxPacketSize:
    8 bInterval: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 09 02 57 00 03 01 04 c0
    ..........W..... 0020 00 09 04 00 00 00 ff ff 00 00 09 04 01 00 00 ff
    ................ 0030 ff 00 05 07 05 81 02 08 00 01 07 05 01 02 08 00
    ................ 0040 01 09 04 02 00 02 ff ff 00 06 07 05 81 03 08 00
    ................ 0050 01 07 05 01 03 08 00 01 09 04 02 01 02 ff ff 00
    ................ 0060 05 07 05 81 02 08 00 01 07 05 01 02 08 00 01
    ............... No. Time Source Destination Protocol Info 260 45.768543
    host 9.0 USB SET CONFIGURATION Request Frame 260 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800cd9b80c0 URB type: URB\_SUBMIT
    ('S') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB
    bus id: 8 Device setup request: present (0) Data: present (0) URB
    status: Operation now in progress (-EINPROGRESS) (-115) URB length
    \[bytes\]: 0 Data length \[bytes\]: 0 \[Response in: 261\]
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB setup 0000 00 09 01 00
    00 00 00 00 00 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00
    00 00 00 ........ No. Time Source Destination Protocol Info 261
    45.774263 9.0 host USB SET CONFIGURATION Response Frame 261 (24 bytes on
    wire, 24 bytes captured) USB URB URB id: 0xffff8800cd9b80c0 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_CONTROL (2) Endpoint: 0x00
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 260\]  
      
    \[Time from request: 0.005720000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    262 45.777499 host 9.0 USB SET INTERFACE Request
    
    Frame 262 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 263\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 01 0b 00 00 02 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    263 45.782263 9.0 host USB SET INTERFACE Response
    
    Frame 263 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x00  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 262\]  
      
    \[Time from request: 0.004764000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    264 45.782285 host 9.0 USB GET CONFIGURATION Request
    
    Frame 264 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 265\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 08 00 00 00 00 01 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    265 45.788264 9.0 host USB GET CONFIGURATION Response
    
    Frame 265 (25 bytes on wire, 25 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 1  
      
    \[Request in: 264\]  
      
    \[Time from request: 0.005979000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    bConfigurationValue: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 .........
    
    No. Time Source Destination Protocol Info  
      
    266 45.788272 host 9.0 USB GET INTERFACE Request
    
    Frame 266 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 267\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 81 0a 00 00 02 00 01 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    267 45.795259 9.0 host USB GET INTERFACE Response
    
    Frame 267 (25 bytes on wire, 25 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 1  
      
    \[Request in: 266\]  
      
    \[Time from request: 0.006987000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    bAlternateSetting: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 .........
    
    No. Time Source Destination Protocol Info  
      
    268 45.795277 host 9.0 USB GET INTERFACE Request
    
    Frame 268 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 1 Data length \[bytes\]: 0
    \[Response in: 269\] \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\] URB
    setup 0000 81 0a 00 00 02 00 01 00 00 00 00 00 00 00 00 00
    ................ 0010 00 02 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 269 45.799261 9.0 host USB GET INTERFACE
    Response Frame 269 (25 bytes on wire, 25 bytes captured) USB URB URB id:
    0xffff8800cd9b8d80 URB type: URB\_COMPLETE ('C') URB transfer type:
    URB\_CONTROL (2) Endpoint: 0x80 Device: 9 URB bus id: 8 Device setup
    request: not present ('-') Data: present (0) URB status: Success (0) URB
    length \[bytes\]: 1 Data length \[bytes\]: 1 \[Request in: 268\] \[Time
    from request: 0.003984000 seconds\] \[bInterfaceClass: VENDOR\_SPECIFIC
    (0xff)\] bAlternateSetting: 1 0000 00 00 00 00 00 00 00 00 00 00 00 00
    00 00 00 00 ................ 0010 00 02 00 00 00 00 00 00 01 .........
    No. Time Source Destination Protocol Info 270 46.358019 host 9.0 USB SET
    INTERFACE Request Frame 270 (24 bytes on wire, 24 bytes captured) USB
    URB URB id: 0xffff8800c3360680 URB type: URB\_SUBMIT ('S') URB transfer
    type: URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB bus id: 8 Device
    setup request: present (0) Data: present (0) URB status: Operation now
    in progress (-EINPROGRESS) (-115) URB length \[bytes\]: 0 Data length
    \[bytes\]: 0 \[Response in: 271\] \[bInterfaceClass: VENDOR\_SPECIFIC
    (0xff)\] URB setup 0000 01 0b 00 00 02 00 00 00 00 00 00 00 00 00 00 00
    ................ 0010 00 00 00 00 00 00 00 00 ........ No. Time Source
    Destination Protocol Info 271 46.362174 9.0 host USB SET INTERFACE
    Response Frame 271 (24 bytes on wire, 24 bytes captured) USB URB URB id:
    0xffff8800c3360680 URB type: URB\_COMPLETE ('C') URB transfer type:
    URB\_CONTROL (2) Endpoint: 0x00 Device: 9 URB bus id: 8 Device setup
    request: not present ('-') Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 0  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 270\]  
      
    \[Time from request: 0.004155000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    272 46.362190 host 9.0 USB GET CONFIGURATION Request
    
    Frame 272 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 273\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 80 08 00 00 00 00 01 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    273 46.369173 9.0 host USB GET CONFIGURATION Response
    
    Frame 273 (25 bytes on wire, 25 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 1  
      
    \[Request in: 272\]  
      
    \[Time from request: 0.006983000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    bConfigurationValue: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 .........
    
    No. Time Source Destination Protocol Info  
      
    274 46.369182 host 9.0 USB GET INTERFACE Request
    
    Frame 274 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 275\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 81 0a 00 00 02 00 01 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    275 46.376173 9.0 host USB GET INTERFACE Response
    
    Frame 275 (25 bytes on wire, 25 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 1  
      
    \[Request in: 274\]  
      
    \[Time from request: 0.006991000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    bAlternateSetting: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 .........
    
    No. Time Source Destination Protocol Info  
      
    276 46.376192 host 9.0 USB GET INTERFACE Request
    
    Frame 276 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: present (0)  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 277\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    URB setup
    
    0000 81 0a 00 00 02 00 01 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    277 46.383172 9.0 host USB GET INTERFACE Response
    
    Frame 277 (25 bytes on wire, 25 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800c3360680  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_CONTROL (2)  
      
    Endpoint: 0x80  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 1  
      
    Data length \[bytes\]: 1  
      
    \[Request in: 276\]  
      
    \[Time from request: 0.006980000 seconds\]  
      
    \[bInterfaceClass: VENDOR\_SPECIFIC (0xff)\]  
      
    bAlternateSetting: 1
    
    0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 .........
    
    No. Time Source Destination Protocol Info  
      
    278 47.401967 host 9.1 USB URB\_INTERRUPT
    
    Frame 278 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 0
    \[Response in: 279\] 0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00
    00 ................ 0010 00 02 00 00 00 00 00 00 ........ No. Time
    Source Destination Protocol Info 279 47.403015 9.1 host USB
    URB\_INTERRUPT Frame 279 (24 bytes on wire, 24 bytes captured) USB URB
    URB id: 0xffff8800cd913e00 URB type: URB\_COMPLETE ('C') URB transfer
    type: URB\_INTERRUPT (1) Endpoint: 0x81 Device: 9 URB bus id: 8 Device
    setup request: not present ('-') Data: present (0) URB status: Success
    (0) URB length \[bytes\]: 0 Data length \[bytes\]: 0 \[Request in: 278\]
    \[Time from request: 0.001048000 seconds\] 0000 00 00 00 00 00 00 00 00
    01 00 00 00 00 00 00 00 ................ 0010 00 02 00 00 00 00 00 00
    ........ No. Time Source Destination Protocol Info 280 47.404010 host
    9.1 USB URB\_INTERRUPT Frame 280 (32 bytes on wire, 32 bytes captured)
    USB URB URB id: 0xffff8800cd913e00 URB type: URB\_SUBMIT ('S') URB
    transfer type: URB\_INTERRUPT (1) Endpoint: 0x01 Device: 9 URB bus id: 8
    Device setup request: not present ('-') Data: present (0) URB status:
    Operation now in progress (-EINPROGRESS) (-115) URB length \[bytes\]: 8
    Data length \[bytes\]: 8 \[Response in: 281\] Application Data:
    F07E7F0601F7FFFF // SysEx "Identity Request" 0000 00 00 00 00 00 00 00
    00 01 00 00 00 00 00 00 00 ................ 0010 00 00 00 00 00 00 00 00
    f0 7e 7f 06 01 f7 ff ff .........\~...... No. Time Source Destination
    Protocol Info 281 47.405011 9.1 host USB URB\_INTERRUPT Frame 281 (24
    bytes on wire, 24 bytes captured) USB URB URB id: 0xffff8800cd913e00 URB
    type: URB\_COMPLETE ('C') URB transfer type: URB\_INTERRUPT (1)
    Endpoint: 0x01 Device: 9 URB bus id: 8 Device setup request: not present
    ('-') Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 280\]  
      
    \[Time from request: 0.001001000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    282 47.405026 host 9.1 USB URB\_INTERRUPT
    
    Frame 282 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 0
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................
    0010 00 02 00 00 00 00 00 00 ........ No. Time Source Destination
    Protocol Info 283 47.409086 host 9.1 USB URB\_INTERRUPT Frame 283 (32
    bytes on wire, 32 bytes captured) USB URB URB id: 0xffff8800cd9b8d80 URB
    type: URB\_SUBMIT ('S') URB transfer type: URB\_INTERRUPT (1) Endpoint:
    0x01 Device: 9 URB bus id: 8 Device setup request: not present ('-')
    Data: present (0) URB status: Operation now in progress (-EINPROGRESS)
    (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 8 \[Response in:
    284\] Application Data: F07E7F0601F7FFFF // SysEx "Identity Request"
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................
    0010 00 00 00 00 00 00 00 00 f0 7e 7f 06 01 f7 ff ff .........\~......
    No. Time Source Destination Protocol Info 284 47.411011 9.1 host USB
    URB\_INTERRUPT Frame 284 (24 bytes on wire, 24 bytes captured) USB URB
    URB id: 0xffff8800cd9b8d80 URB type: URB\_COMPLETE ('C') URB transfer
    type: URB\_INTERRUPT (1) Endpoint: 0x01 Device: 9 URB bus id: 8 Device
    setup request: not present ('-') Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 283\]  
      
    \[Time from request: 0.001925000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    285 47.414181 host 9.1 USB URB\_INTERRUPT
    
    Frame 285 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 287\]  
      
    Application Data: F00001362A7F4400 // SysEx "Global System
    Configuration" (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 f0 00 01 36 2a 7f 44 00 ...........6\*.D.
    
    No. Time Source Destination Protocol Info  
      
    286 47.416013 9.1 host USB URB\_INTERRUPT
    
    Frame 286 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 285\]  
      
    \[Time from request: 0.001832000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    287 47.418010 9.1 host USB URB\_INTERRUPT
    
    Frame 287 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 285\]  
      
    \[Time from request: 0.003829000 seconds\]  
      
    Application Data: F501F07E0F060200 // SysEx "Reply to Identity Request"
    (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 f5 01 f0 7e 0f 06 02 00 ...........\~....
    
    No. Time Source Destination Protocol Info  
      
    288 47.418316 host 9.1 USB URB\_INTERRUPT
    
    Frame 288 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 289\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    289 47.421009 9.1 host USB URB\_INTERRUPT
    
    Frame 289 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 288\]  
      
    \[Time from request: 0.002693000 seconds\]  
      
    Application Data: 01362A000000332E // SysEx "Reply to Identity Request"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 36 2a 00 00 00 33 2e .........6\*...3.
    
    No. Time Source Destination Protocol Info  
      
    290 47.421368 host 9.1 USB URB\_INTERRUPT
    
    Frame 290 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    Application Data: 000040F7FFFFFFFF // SysEx "Global System
    Configuration" mode 0x40 Slave ? (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 00 00 40 f7 ff ff ff ff ..........@.....
    
    No. Time Source Destination Protocol Info  
      
    291 47.421378 host 9.1 USB URB\_INTERRUPT
    
    Frame 291 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 292\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    292 47.423008 9.1 host USB URB\_INTERRUPT
    
    Frame 292 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 291\]  
      
    \[Time from request: 0.001630000 seconds\]  
      
    Application Data: 3038F7FFFFFFFFFF // SysEx "Reply to Identity Request"
    : "3.08" (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 30 38 f7 ff ff ff ff ff ........08......
    
    No. Time Source Destination Protocol Info  
      
    293 47.424423 host 9.1 USB URB\_INTERRUPT
    
    Frame 293 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 0
    \[Response in: 294\] 0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00
    00 ................ 0010 00 02 00 00 00 00 00 00 ........ No. Time
    Source Destination Protocol Info 294 47.427008 9.1 host USB
    URB\_INTERRUPT Frame 294 (24 bytes on wire, 24 bytes captured) USB URB
    URB id: 0xffff8800cd913e00 URB type: URB\_COMPLETE ('C') URB transfer
    type: URB\_INTERRUPT (1) Endpoint: 0x01 Device: 9 URB bus id: 8 Device
    setup request: not present ('-') Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 293\]  
      
    \[Time from request: 0.002585000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    295 47.430521 host 9.1 USB URB\_INTERRUPT
    
    Frame 295 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 296\]  
      
    Application Data: F00001362A7F4470 // SysEx "Send Display Text" (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 f0 00 01 36 2a 7f 44 70 ...........6\*.Dp
    
    No. Time Source Destination Protocol Info  
      
    296 47.432008 9.1 host USB URB\_INTERRUPT
    
    Frame 296 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 295\]  
      
    \[Time from request: 0.001487000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    297 47.435813 host 9.1 USB URB\_INTERRUPT
    
    Frame 297 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 298\]  
      
    Application Data: 00000D496E697469 // SysEx "Send Display Text" Clear
    display (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 00 00 0d 49 6e 69 74 69 ...........Initi
    
    No. Time Source Destination Protocol Info  
      
    298 47.437023 9.1 host USB URB\_INTERRUPT
    
    Frame 298 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 297\]  
      
    \[Time from request: 0.001210000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    299 47.440911 host 9.1 USB URB\_INTERRUPT
    
    Frame 299 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 300\]  
      
    Application Data: 616C697A696E6720 // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 61 6c 69 7a 69 6e 67 20 ........alizing
    
    No. Time Source Destination Protocol Info  
      
    300 47.442007 9.1 host USB URB\_INTERRUPT
    
    Frame 300 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 299\]  
      
    \[Time from request: 0.001096000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    301 47.446008 host 9.1 USB URB\_INTERRUPT
    
    Frame 301 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 302\]  
      
    Application Data: 55534220436F6E6E // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 55 53 42 20 43 6f 6e 6e ........USB Conn
    
    No. Time Source Destination Protocol Info  
      
    302 47.448006 9.1 host USB URB\_INTERRUPT
    
    Frame 302 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 301\]  
      
    \[Time from request: 0.001998000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    303 47.451145 host 9.1 USB URB\_INTERRUPT
    
    Frame 303 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 304\]  
      
    Application Data: 656374696F6E2E2E // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 65 63 74 69 6f 6e 2e 2e ........ection..
    
    No. Time Source Destination Protocol Info  
      
    304 47.453005 9.1 host USB URB\_INTERRUPT
    
    Frame 304 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 303\]  
      
    \[Time from request: 0.001860000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    305 47.456236 host 9.1 USB URB\_INTERRUPT
    
    Frame 305 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 306\]  
      
    Application Data: 2EF7FFFFFFFFFFFF // SysEx "Send Display Text" :
    "Initializing USB Connection..." (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 2e f7 ff ff ff ff ff ff ................
    
    No. Time Source Destination Protocol Info  
      
    306 47.458005 9.1 host USB URB\_INTERRUPT
    
    Frame 306 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 305\]  
      
    \[Time from request: 0.001769000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    307 47.460559 host 9.1 USB URB\_INTERRUPT
    
    Frame 307 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 309\]  
      
    Application Data: F07E7F0601F7FFFF // SysEx "Identity Request"
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 f0 7e 7f 06 01 f7 ff ff .........\~......
    
    No. Time Source Destination Protocol Info  
      
    308 47.462003 9.1 host USB URB\_INTERRUPT
    
    Frame 308 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 307\]  
      
    \[Time from request: 0.001444000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    309 47.490001 9.1 host USB URB\_INTERRUPT
    
    Frame 309 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 307\]  
      
    \[Time from request: 0.029442000 seconds\]  
      
    Application Data: F501F07E0F060200 // SysEx "Reply to Identity Request"
    (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 f5 01 f0 7e 0f 06 02 00 ...........\~....
    
    No. Time Source Destination Protocol Info  
      
    310 47.490116 host 9.1 USB URB\_INTERRUPT
    
    Frame 310 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 311\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    311 47.493000 9.1 host USB URB\_INTERRUPT
    
    Frame 311 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 310\]  
      
    \[Time from request: 0.002884000 seconds\]  
      
    Application Data: 01362A000000332E // SysEx "Reply to Identity Request"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 36 2a 00 00 00 33 2e .........6\*...3.
    
    No. Time Source Destination Protocol Info  
      
    312 47.493178 host 9.1 USB URB\_INTERRUPT
    
    Frame 312 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 313\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    313 47.494996 9.1 host USB URB\_INTERRUPT
    
    Frame 313 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 312\]  
      
    \[Time from request: 0.001818000 seconds\]  
      
    Application Data: 3038F7FFFFFFFFFF // SysEx "Reply to Identity Request"
    : "3.08" (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 30 38 f7 ff ff ff ff ff ........08......
    
    No. Time Source Destination Protocol Info  
      
    314 47.495236 host 9.1 USB URB\_INTERRUPT
    
    Frame 314 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 0
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................
    0010 00 02 00 00 00 00 00 00 ........ No. Time Source Destination
    Protocol Info 315 47.499301 host 9.1 USB URB\_INTERRUPT Frame 315 (32
    bytes on wire, 32 bytes captured) USB URB URB id: 0xffff8800cd913e00 URB
    type: URB\_SUBMIT ('S') URB transfer type: URB\_INTERRUPT (1) Endpoint:
    0x01 Device: 9 URB bus id: 8 Device setup request: not present ('-')
    Data: present (0) URB status: Operation now in progress (-EINPROGRESS)
    (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 8 \[Response in:
    316\] Application Data: F00001362A7F4470 // SysEx "Send Display Text"
    (start) 0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00
    ................ 0010 00 00 00 00 00 00 00 00 f0 00 01 36 2a 7f 44 70
    ...........6\*.Dp No. Time Source Destination Protocol Info 316
    47.500998 9.1 host USB URB\_INTERRUPT Frame 316 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800cd913e00 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_INTERRUPT (1) Endpoint: 0x01
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 315\]  
      
    \[Time from request: 0.001697000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    317 47.504417 host 9.1 USB URB\_INTERRUPT
    
    Frame 317 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 318\]  
      
    Application Data: 004056657273696F // SysEx "Send Display Text" :
    Display 0 Line 1 (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 00 40 56 65 72 73 69 6f .........@Versio
    
    No. Time Source Destination Protocol Info  
      
    318 47.505996 9.1 host USB URB\_INTERRUPT
    
    Frame 318 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 317\]  
      
    \[Time from request: 0.001579000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    319 47.509511 host 9.1 USB URB\_INTERRUPT
    
    Frame 319 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 320\]  
      
    Application Data: 6E20333038F7FFFF // SysEx "Send Display Text" :
    "Version 308" (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 6e 20 33 30 38 f7 ff ff ........n 308...
    
    No. Time Source Destination Protocol Info  
      
    320 47.510997 9.1 host USB URB\_INTERRUPT
    
    Frame 320 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 319\]  
      
    \[Time from request: 0.001486000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    321 47.514727 host 9.1 USB URB\_INTERRUPT
    
    Frame 321 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 322\]  
      
    Application Data: F00001362A7F5201 // SysEx "Request System Parameter"
    (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 f0 00 01 36 2a 7f 52 01 ...........6\*.R.
    
    No. Time Source Destination Protocol Info  
      
    322 47.515995 9.1 host USB URB\_INTERRUPT
    
    Frame 322 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 321\]  
      
    \[Time from request: 0.001268000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    323 47.519824 host 9.1 USB URB\_INTERRUPT
    
    Frame 323 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 325\]  
      
    Application Data: 01000001F7FFFFFF // SysEx "Request System Parameter"
    Address 010100 Length 0001 ID ? (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 01 00 00 01 f7 ff ff ff ................
    
    No. Time Source Destination Protocol Info  
      
    324 47.520994 9.1 host USB URB\_INTERRUPT
    
    Frame 324 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 323\]  
      
    \[Time from request: 0.001170000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    325 47.553990 9.1 host USB URB\_INTERRUPT
    
    Frame 325 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 323\]  
      
    \[Time from request: 0.034166000 seconds\]  
      
    Application Data: F00001362A0F4401 // SysEx "Reply System Parameter"
    (start)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 f0 00 01 36 2a 0f 44 01 ...........6\*.D.
    
    No. Time Source Destination Protocol Info  
      
    326 47.554437 host 9.1 USB URB\_INTERRUPT
    
    Frame 326 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;')  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Response in: 327\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    327 47.556989 9.1 host USB URB\_INTERRUPT
    
    Frame 327 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Request in: 326\]  
      
    \[Time from request: 0.002552000 seconds\]  
      
    Application Data: 010000F7FFFFFFFF // SysEx "Reply System Parameter" ID
    0 (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 02 00 00 00 00 00 00 01 00 00 f7 ff ff ff ff ................
    
    No. Time Source Destination Protocol Info  
      
    328 47.557497 host 9.1 USB URB\_INTERRUPT
    
    Frame 328 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd9b8d80  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x81  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&lt;') URB status: Operation now in progress
    (-EINPROGRESS) (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 0
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................
    0010 00 02 00 00 00 00 00 00 ........ No. Time Source Destination
    Protocol Info 329 47.668498 host 9.1 USB URB\_INTERRUPT Frame 329 (32
    bytes on wire, 32 bytes captured) USB URB URB id: 0xffff8800cd913e00 URB
    type: URB\_SUBMIT ('S') URB transfer type: URB\_INTERRUPT (1) Endpoint:
    0x01 Device: 9 URB bus id: 8 Device setup request: not present ('-')
    Data: present (0) URB status: Operation now in progress (-EINPROGRESS)
    (-115) URB length \[bytes\]: 8 Data length \[bytes\]: 8 \[Response in:
    330\] Application Data: F00001362A7F4470 // SysEx "Send Display Text"
    (start) 0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00
    ................ 0010 00 00 00 00 00 00 00 00 f0 00 01 36 2a 7f 44 70
    ...........6\*.Dp No. Time Source Destination Protocol Info 330
    47.669972 9.1 host USB URB\_INTERRUPT Frame 330 (24 bytes on wire, 24
    bytes captured) USB URB URB id: 0xffff8800cd913e00 URB type:
    URB\_COMPLETE ('C') URB transfer type: URB\_INTERRUPT (1) Endpoint: 0x01
    Device: 9 URB bus id: 8 Device setup request: not present ('-') Data:
    not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 329\]  
      
    \[Time from request: 0.001474000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    331 47.673598 host 9.1 USB URB\_INTERRUPT
    
    Frame 331 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 332\]  
      
    Application Data: 00000D4669726D77 // SysEx "Send Display Text" Clear
    display (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 00 00 0d 46 69 72 6d 77 ...........Firmw
    
    No. Time Source Destination Protocol Info  
      
    332 47.674970 9.1 host USB URB\_INTERRUPT
    
    Frame 332 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 331\]  
      
    \[Time from request: 0.001372000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    333 47.678712 host 9.1 USB URB\_INTERRUPT
    
    Frame 333 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 334\]  
      
    Application Data: 6172652056332E30 // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 61 72 65 20 56 33 2e 30 ........are V3.0
    
    No. Time Source Destination Protocol Info  
      
    334 47.679970 9.1 host USB URB\_INTERRUPT
    
    Frame 334 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 333\]  
      
    \[Time from request: 0.001258000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    335 47.683820 host 9.1 USB URB\_INTERRUPT
    
    Frame 335 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 336\]  
      
    Application Data: 382C204944203020 // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 38 2c 20 49 44 20 30 20 ........8, ID 0
    
    No. Time Source Destination Protocol Info  
      
    336 47.684969 9.1 host USB URB\_INTERRUPT
    
    Frame 336 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 335\]  
      
    \[Time from request: 0.001149000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    337 47.688903 host 9.1 USB URB\_INTERRUPT
    
    Frame 337 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 338\]  
      
    Application Data: 5B4D41535445525D // SysEx "Send Display Text"
    (continued)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 5b 4d 41 53 54 45 52 5d ........\[MASTER\]
    
    No. Time Source Destination Protocol Info  
      
    338 47.689969 9.1 host USB URB\_INTERRUPT
    
    Frame 338 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 337\]  
      
    \[Time from request: 0.001066000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........
    
    No. Time Source Destination Protocol Info  
      
    339 47.693989 host 9.1 USB URB\_INTERRUPT
    
    Frame 339 (32 bytes on wire, 32 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_SUBMIT ('S')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: present (0)  
      
    URB status: Operation now in progress (-EINPROGRESS) (-115)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 8  
      
    \[Response in: 340\]  
      
    Application Data: F7FFFFFFFFFFFFFF // SysEx "Send Display Text" :
    "Firmware V3.08, ID 0 \[MASTER\]" (end)
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 f7 ff ff ff ff ff ff ff ................
    
    No. Time Source Destination Protocol Info  
      
    340 47.695968 9.1 host USB URB\_INTERRUPT
    
    Frame 340 (24 bytes on wire, 24 bytes captured)  
      
    USB URB  
      
    URB id: 0xffff8800cd913e00  
      
    URB type: URB\_COMPLETE ('C')  
      
    URB transfer type: URB\_INTERRUPT (1)  
      
    Endpoint: 0x01  
      
    Device: 9  
      
    URB bus id: 8  
      
    Device setup request: not present ('-')  
      
    Data: not present ('&gt;')  
      
    URB status: Success (0)  
      
    URB length \[bytes\]: 8  
      
    Data length \[bytes\]: 0  
      
    \[Request in: 339\]  
      
    \[Time from request: 0.001979000 seconds\]
    
    0000 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 ................  
      
    0010 00 00 00 00 00 00 00 00 ........

Another sniffing taught me that the midi port number is given at the
start of the message both from and to the SAC in the form :

`F5 pn`

where pn is the port number (01 to 06 being respectively SAC Control,
MIDI port, Inst. 3, Inst. 4, Inst 5 and Config).

It's not sent by the host for the SAC Control.

And last but not least, it seems that data is sent from the host on
endpoint 0x01 and received from 0x81
