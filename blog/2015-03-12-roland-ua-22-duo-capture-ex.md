---
date: '2015-03-12'
downloads:
  - file: /files/0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22.patch
    title: '0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22'
  - file: /files/0002-UA-22-MIDI-fixup.patch
    title: '0002-UA-22-MIDI-fixup'
keywords:
  - 'Audio interface'
short_title: 'Roland UA-22'
subject: 'Techno. Audio • Audio Tech.'
tags:
  - 'Layer: Hardware'
  - 'Démontage'
  - 'Teardown'
  - 'Roland'
  - 'UA-22'
  - 'DUO-CAPTURE EX'
  - 'GNU/Linux'
  - 'ALSA'
  - 'Audio'
  - 'MIDI'
  - 'USB'
---
# Roland UA-22 DUO-CAPTURE EX

Just got myself this nice little USB audio and MIDI interface.

It works great!

Full support out of the box on Android on all modes using Audio
Evolution Mobile and USB Audio Recorder PRO from
[www.extreamsd.com](https://www.extreamsd.com) and even native
support in Lollipop (5.0) in "TAB" mode.

On the Linux side of things, I was pleased to see full audio support
(fairly recent kernel 3.18.6) but MIDI was not working out of the box.  
  
Fortunately, I found that Daniel Mack (\@zonque) had already cooked some
patches.  
  
{del}`Here they are:`

- {del}`[0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22](
/files/0001-ALSA-snd-usb-add-quirks-for-Roland-UA-22.patch)`
- {del}`[0002-UA-22-MIDI-fixup](/files/0002-UA-22-MIDI-fixup.patch)`


{del}`Hope these will get pushed upstream soon!`

:::{hint} Update

The [patch](https://mailman.alsa-project.org/pipermail/alsa-devel/2015-March/089034.html)
has been
[merged upstream.](https://mailman.alsa-project.org/pipermail/alsa-devel/2015-March/089038.html)
% Original URLs:
% - http://permalink.gmane.org/gmane.linux.alsa.devel/135432
% - http://permalink.gmane.org/gmane.linux.alsa.devel/135436

Thanks Daniel!

:::

Oh, and if you're an hardware freak like me, you'll love seeing what's
in its guts.  
  
[Here are the photos of the
teardown.](https://photos.app.goo.gl/8cYJhVcB2Lp6Mvmc9)
