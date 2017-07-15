Title: Cross-compiler un noyau i386 sur amd64 avec make-kpkg
Date: 2009-08-23 07:40
Author: admin
Category: Debian, GNU/Linux, Ubuntu, UbuntuStudio
Slug: cross-compiler-un-noyau-i386-sur-amd64-avec-make-kpkg
Status: published

**Configurer**

`setarch i386 make xconfig`

**Nettoyer**

`make-kpkg clean`

**Compiler**

`` DEB_HOST_ARCH=i386 make-kpkg --arch i386 --cross-compile - --rootcmd fakeroot --revision 2.6.X --append-to-version -VERSION-`date +%Y%m%d`-1 linux-image ``

Remplacer la révision et la version par ce qui est voulu.

Je peux enfin compiler un noyau pour eee PC à une vitesse convenable!
