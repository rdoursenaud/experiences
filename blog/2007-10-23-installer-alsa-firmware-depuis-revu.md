---
date: '2007-10-23'
short_title: 'REVU ALSA Firmware'
subject: 'Informatique • IT'
tags:
  - 'GNU/Linux'
  - 'Ubuntu'
  - 'UbuntuStudio'
  - 'ALSA'
---
# Installer alsa-firmware depuis REVU

:::{attention}
Page obsolète, lien mort.  
Conservée pour la postérité ;)
:::

```sh
dget -x http://revu.tauware.de/revu1-incoming/alsa-firmware-0708231740/alsa-firmware_1.0.14rc4+dfsg1-0ubuntu1.dsc
cd alsa-firmware-1.0.14rc4+dfsg1/
fakeroot dpkg-buildpackage
cd ..
sudo dpkg -i alsa-firmware*.deb
```
