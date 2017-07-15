Title: Roland UA-22 DUO-CAPTURE EX
Date: 2015-03-12 03:49
Author: admin
Category: Audio, GNU/Linux, Hardware, Teardowns
Tags: alsa, audio, DUO-CAPTURE EX, Linux, MIDI, Roland, UA-22, USB
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
  
[Here they are:  
  
[0002-UA-22-MIDI-fixup  
  
](http://raphael.doursenaud.fr/wp-content/uploads/0002-UA-22-MIDI-fixup.patch)[0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22  
  
](http://raphael.doursenaud.fr/wp-content/uploads/0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22.patch)Hope
these will get pushed upstream
soon!]{style="text-decoration: line-through;"}

Update:
The [patch](http://permalink.gmane.org/gmane.linux.alsa.devel/135432)
has been [merged
upstream.](http://permalink.gmane.org/gmane.linux.alsa.devel/135436) Thanks
Daniel!

Oh, and if you're an hardware freak like me, you'll love seeing what's
in its guts.  
  
[Here are the photos of the
teardown.](https://plus.google.com/photos/103261928464197839037/albums/6125160886026017681)
