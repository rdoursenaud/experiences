Title: Soundcraft Si Multi Digital Card
Date: 2014-05-02 09:20
Category: Blog
Tags: GNU/Linux, Hardware, Audio, Soundcraft, Si Multi Digital
Slug: soundcraft-si-multi-digital-card
Status: published

[Photos](https://plus.google.com/photos/103261928464197839037/albums/6149870533468472513?authkey=CIKBr4W_q_KKngE)

Once the firmware is flashed from a Windows or Mac OS machine, the
device is seen as USB class compliant.  
  
This means it doesn't need any drivers to work with Linux and works out
of the box with Android and maybe iOS USB recording software.  
  
Didn't try the Firewire part yet but its supposed to not need any driver
on Mac OS X, so I suspect it's also a standard implementation.  
  
Will report further experimentations later.

\[EDIT\] 2016-01-09  
  
Finally took the time to have another look.  
  
Firewire is not currently supported by FFADO.  
  
Will do my best to try and figure it out.  
  
Further informations will likely end up in my [GitHub
repo.](https://github.com/EMATech/Soundcraft_Digital)

\[EDIT\] 2016-01-14  
  
Takashi Sakamoto's doing an awesome job of figuring out the interface.  
  
Follow [this thread on the FFADO
mailing-list](http://sourceforge.net/p/ffado/mailman/ffado-devel/thread/CAKKsO5CYHVRvgo6AV%3D%3DZRJ2it53cF7UGHnnDyCLZY_jzJYHpSA%40mail.gmail.com/)
for live progress.  
  
Kudos to Takashi! He really knows his stuff.
