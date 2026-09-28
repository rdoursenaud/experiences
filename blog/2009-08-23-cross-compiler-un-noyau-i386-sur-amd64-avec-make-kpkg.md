---
title: Cross-compiler un noyau i386 sur amd64 avec make-kpkg
date: '2009-08-23'
subject: Informatique // IT
tags:
  - Informatique
  - IT
  - GNU/Linux
  - Debian
  - Ubuntu
  - UbuntuStudio
---

## Configurer

`setarch i386 make xconfig`

## Nettoyer

`make-kpkg clean`

## Compiler

`` DEB_HOST_ARCH=i386 make-kpkg --arch i386 --cross-compile - --rootcmd fakeroot --revision 2.6.X --append-to-version -VERSION-`date +%Y%m%d`-1 linux-image ``

Remplacer la révision et la version par ce qui est voulu.

Je peux enfin compiler un noyau pour eee PC à une vitesse convenable !
