Title: Roland UA-22 DUO-CAPTURE EX
Date: 2015-03-12 03:49
Category: Informatique
Tags: Hardware, Teardown, Roland, UA-22, ALSA, Audio, DUO-CAPTURE EX, GNU/Linux, MIDI, USB
Slug: roland-ua-22-duo-capture-ex
Status: published

Just got myself this nice little USB audio and MIDI interface.

It works great!

Full support out of the box on Android on all modes using Audio
Evolution Mobile and USB Audio Recorder PRO from
[http://www.extreamsd.com](http://www.extreamsd.com/) and even native
support in Lollipop (5.0) in "TAB" mode.

On the Linux side of things, I was pleased to see full audio support
(fairly recent kernel 3.18.6) but MIDI was not working out of the box.  
  
Fortunately, I found that Daniel Mack (@zonque) had already cooked some
patches.  
  
~~Here they are:~~

- ~~[0002-UA-22-MIDI-fixup](files/0002-UA-22-MIDI-fixup.patch)~~
- ~~[0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22](files/0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22.patch)~~

~~Hope these will get pushed upstream soon!~~

Update:
The [patch](http://permalink.gmane.org/gmane.linux.alsa.devel/135432)
has been [merged
upstream.](http://permalink.gmane.org/gmane.linux.alsa.devel/135436) Thanks
Daniel!

Oh, and if you're an hardware freak like me, you'll love seeing what's
in its guts.  
  
[Here are the photos of the
teardown.](https://photos.app.goo.gl/8cYJhVcB2Lp6Mvmc9)
