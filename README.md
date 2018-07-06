# giiker

```
$ bluetoothctl
[bluetooth]# scan on
...
Discovery started
[CHG] Controller ... Discovering: yes
...
[NEW] Device C2:DD:1F:F8:CB:DA GiC41183
...
[bluetooth]# connect C2:DD:1F:F8:CB:DA
Attempting to connect to C2:DD:1F:F8:CB:DA
[CHG] Device C2:DD:1F:F8:CB:DA Connected: yes
Connection successful
[bluetooth]# trust C2:DD:1F:F8:CB:DA
[bluetooth]# pair C2:DD:1F:F8:CB:DA

[CHG] Device C2:DD:1F:F8:CB:DA Trusted: yes
[CHG] Device C2:DD:1F:F8:CB:DA Connected: yes
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0008
	00001801-0000-1000-8000-00805f9b34fb
	Generic Attribute Profile
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0009
	0000180a-0000-1000-8000-00805f9b34fb
	Device Information
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0009/char000a
	00002a29-0000-1000-8000-00805f9b34fb
	Manufacturer Name String
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0010
	0000aadb-0000-1000-8000-00805f9b34fb
	Unknown
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0010/char0011
	0000aadc-0000-1000-8000-00805f9b34fb
	Unknown
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0010/char0011/desc0013
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0014
	0000aaaa-0000-1000-8000-00805f9b34fb
	Unknown
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0014/char0015
	0000aaab-0000-1000-8000-00805f9b34fb
	Unknown
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0014/char0015/desc0017
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service0014/char0018
	0000aaac-0000-1000-8000-00805f9b34fb
	Unknown
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service001a
	00001530-1212-efde-1523-785feabcd123
	Vendor specific
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service001a/char001b
	00001532-1212-efde-1523-785feabcd123
	Vendor specific
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service001a/char001d
	00001531-1212-efde-1523-785feabcd123
	Vendor specific
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service001a/char001d/desc001f
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DD_1F_F8_CB_DA/service001a/char0020
	00001534-1212-efde-1523-785feabcd123
	Vendor specific
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 00001530-1212-efde-1523-785feabcd123
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 00001800-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 00001801-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 0000180a-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 0000180f-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 0000aaaa-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA UUIDs: 0000aadb-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DD:1F:F8:CB:DA ServicesResolved: yes
```

Pairing might not work, but trust + connect does?

```
[bluetooth]# info C2:DD:1F:F8:CB:DA
Device C2:DD:1F:F8:CB:DA (random)
	Name: GiC41183
	Alias: GiC41183
	Paired: no
	Trusted: yes
	Blocked: no
	Connected: no
	LegacyPairing: no
	UUID: Vendor specific           (00001530-1212-efde-1523-785feabcd123)
	UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
	UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
	UUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)
	UUID: Battery Service           (0000180f-0000-1000-8000-00805f9b34fb)
	UUID: Unknown                   (0000aaaa-0000-1000-8000-00805f9b34fb)
	UUID: Unknown                   (0000aadb-0000-1000-8000-00805f9b34fb)
```

## Pythoning

https://elinux.org/RPi_Bluetooth_LE#Using_Bluetooth_LE_with_Python

```
$ sudo pacman -S gobject-introspection
$ wget https://raw.githubusercontent.com/xbmc/xbmc/master/tools/EventClients/lib/python/xbmcclient.py
```
