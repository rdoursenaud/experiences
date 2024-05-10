Title:  Canon's CAPT linux driver how-to for Debian
Date: 2005-09-17 12:00
Category: Informatique // IT
Tags: GNU/Linux, Debian, Imprimante, Printer, Canon, CAPT
Slug: canon-capt-linux-driver-how-to-for-debian
Status: published
Lang: en


A [free driver](http://www.boichat.ch/nicolas/capt/) is now available as an alternative for LBP-810 and LBP-1120.
-----------------------------------------------------------------------------------------------------------------

### Warning: the modifications described here maybe illegal due to stupid licence restrictions.

This driver is applicable for Canon LBP\* CAPT WinGDI-based USB
printers.

Files
-----

You need the driver file from Canon :  
` Linux-driver-capt-e-1.10.tar.gz `  
You can get this tarball from your usual Canon support website (Search
for linux).

The driver is published in rpm so you need alien to translate them to
the debian's deb package format :  
` # apt-get install alien `

It's a backend to CUPS so you also need it :  
` # apt-get install cupsys `

Finally you'll need fakeroot to alien the rpms :  
` # apt-get install fakeroot `

Untar
-----

Untar the tarball :  
` $ tar xvzf Linux-driver-capt-e-1.10.tar.gz `

Alien
-----

Alien the two rpms (you need to be root so use fakeroot):  
` $ cd CAPTlinux_1-1/rpms `  
` $ fakeroot alien cndrvcups*.rpm `

Install
-------

Install the two packages :  
` # dpkg -i cndrvcups*.deb `

Tweak
-----

The Alien tool seem to lose some parts of the original rpms during
translation, we'll need to make these manually.  
First, restart cups to load the ppds :  
` # /etc/init.d/cupsys stop `  
Make sure the daemon is stopped :  
` $ ps aux|grep cupsd `  
If it's not stopped, kill it :  
` # killall cupsd `  
Then finally start it again :  
` # /etc/init.d/cupsys start `  
These ugly steps are needed because the installation of the ccp backend
seems to sometime f\*ck up CUPS when it's running and prevents it from
stopping.

Then create the directories and fifos needed by the daemon (ccpd) and
the monitor (captmon) :  
` # mkdir /var/ccpd `  
` # mkdir /var/captmon `  
` # mkfifo /var/ccpd/fifo0 `  
You can make more fifos if you own more than one CAPT printer, naming
them fifo1, fifo2 ...

Add your printer to the CUPS spooler :  
` # /usr/sbin/lpadmin -p [NameOfPrinter] -m [PPDFILE.PPD] -v ccp:/var/ccpd/fifo0 -E `  
(/var/ccpd/fifo0, fifo1, fifo2 ... if multiple printers)  
Example for LBP1120 :  
` # /usr/sbin/lpadmin -p LBP1120 -m CNCUPSLBP1120CAPTJ.PPD -v ccp:/var/ccpd/fifo0 -E `

Setup ccpd to handle the printer :  
` # /usr/sbin/ccpdadmin -p NameOfPrinter -o /dev/usb/lp0 `  
(/dev/udb/lp0, lp1, lp2 if multiple printers)  
Example for LBP1120 :  
` # /usr/sbin/ccpdadmin -p LBP1120 -o /dev/usb/lp0 `

Create (or replace existing script by) a debian compliant ccpd daemon
script I made :  
(/etc/init.d/ccpd)

    #!/bin/sh
    #
    # ccpd      startup script for Canon Printer Daemon for CUPS
    #
    #       Modified for Debian GNU/Linux
    #       by Raphael Doursenaud <rdoursenaud@free.fr>.

    DAEMON=/usr/sbin/ccpd
    LOCKFILE=/var/lock/subsys/ccpd
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
    NAME=ccpd
    DESC="Canon Printer Daemon for CUPS"

    test -f $DAEMON || exit 0

    case $1 in
      start)
        echo -n "Starting $DESC: $NAME"
        start-stop-daemon --start --quiet --exec $DAEMON
        echo "."
        ;;
      stop)
        echo -n "Stopping $DESC: $NAME"
        start-stop-daemon --stop --quiet --oknodo --exec $DAEMON
        echo "."
        ;;
      status)
        echo "$DESC: $NAME:" `pidof $NAME`
        ;;
      restart)
        echo -n "Restarting $DESC: $NAME"
        start-stop-daemon --stop --quiet --oknodo --exec $DAEMON
        sleep 1
        start-stop-daemon --start --quiet --exec $DAEMON
        echo "."
        ;;
      *)
        echo "Usage: ccpd {start|stop|status}"
        exit 1
        ;;
    esac

    exit 0

Start the ccpd dameon.  
` # /etc/init.d/ccpd start `

You're done.

Tests
-----

First step :  
Simply issue the following command :  
` # ccpdamin `  
You should see your printer listed, with status.

Second step :  
Issue the following command :  
` $ captstatusui -P [NameOfPrinter] `  
Example for LBP1120  
` $ captstatusui -P LBP1120 `  
You should see "Ready to print".

If one test or another fails, please consider reinstalling the driver,
you may have missed something.

And now print!
--------------

TODO
----

\* Make startup script work at bootup  
*- Real Debian packages : NEW! Test packages available :
[cndrvcups-common\_1.10-2\_i386](files/cndrvcups-common_1.10-2_i386.deb)
[cndrvcups-capt\_1.10-2\_i386](files/cndrvcups-capt_1.10-2_i386.deb)*
\* Create symlinks for startup script at bootup  
\* Write an assistant for printer configuration  
\* Include french translations  
\* Tanslate /usr/share/captmon/msgtable.xml to french  
\* Make cngplp fr.po and statusui fr.po  
\* Rewrite this how-to for Ubuntu both in english and french and post it
to the respective WiKis
