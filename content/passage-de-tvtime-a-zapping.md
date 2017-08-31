Title: Passage de tvtime à zapping
Date: 2005-09-19 18:47
Category: Blog
Tags: GNU/Linux, Ubuntu
Slug: passage-de-tvtime-a-zapping
Status: published

Je viens de découvrir [Zapping](http://zapping.sf.net); tout comme
tvtime il permet de regarder la TV cependant il s'intègre beaucoup mieux
à Gnome et j'y obtiens une qualité supérieure! Le télétexte est aussi
intégré!

Afin de faire la transition, j'ai été obligé de me pencher sur le
contrôle lirc de zapping. Leur site n'est apparemment pas à jour de ce
côté là mais j'ai réussi à me faire un petit lircrc :D

`#/etc/lirc/lircrc # Global launcher begin     prog = irexec     button = tv     mode = zapping     config = zapping & end begin     prog = irexec     button = dvd     mode = totem     config = totem & end`

\# Software specific  
\#\# Totem  
begin totem  
begin  
prog = irexec  
button = power  
config = totem --quit  
end  
begin  
prog = irexec  
button = play  
config = totem --play  
end  
begin  
prog = irexec  
button = pause  
config = totem --pause  
end  
begin  
prog = irexec  
button = stop  
config = totem --pause  
end  
begin  
prog = irexec  
button = chan-up  
config = totem --next  
end  
begin  
prog = irexec  
button = chan-down  
config = totem --previous  
end  
begin  
prog = irexec  
button = forward  
config = totem --seek-fwd  
repeat = 1  
end  
begin  
prog = irexec  
button = rewind  
config = totem --seek-bwd  
repeat = 1  
end  
begin  
prog = irexec  
button = vol-up  
config = totem --volume-up  
repeat = 1  
end  
begin  
prog = irexec  
button = vol-down  
config = totem --volume-down  
repeat = 1  
end  
begin  
prog = irexec  
button = max\_window  
config = totem --fullscreen  
end  
end totem

\#\# zapping  
begin zapping  
begin  
prog = irexec  
button = power  
config = zapping\_remote "zapping.quit()"  
end  
begin  
prog = irexec  
button = dvd-root\_menu  
config = zapping\_remote "zapping.toggle\_mode('teletext')"  
end  
begin  
prog = irexec  
button = max\_window  
config = zapping\_remote "zapping.switch\_mode('fullscreen')"  
end  
begin  
prog = irexec  
button = mute  
config = zapping\_remote "zapping.mute(toggle)"  
end  
begin  
prog = irexec  
button = up  
config = zapping\_remote "zapping.ttx\_page\_incr(1)"  
end  
begin  
prog = irexec  
button = down  
config = zapping\_remote "zapping.ttx\_page\_incr(-1)"  
end  
begin  
prog = irexec  
button = vol-up  
config = zapping\_remote "zapping.control\_incr('volume')"  
repeat = 1  
end  
begin  
prog = irexec  
button = vol-down  
config = zapping\_remote "zapping.control\_incr('volume', -1)"  
repeat = 1  
end  
begin  
prog = irexec  
button = chan-up  
config = zapping\_remote "zapping.channel\_up()"  
end  
begin  
prog = irexec  
button = chan-down  
config = zapping\_remote "zapping.channel\_down()"  
end  
begin  
prog = irexec  
button = 1  
config = zapping\_remote "zapping.set\_channel(1)"  
end  
begin  
prog = irexec  
button = 2  
config = zapping\_remote "zapping.set\_channel(2)"  
end  
begin  
prog = irexec  
button = 3  
config = zapping\_remote "zapping.set\_channel(3)"  
end  
begin  
prog = irexec  
button = 4  
config = zapping\_remote "zapping.set\_channel(4)"  
end  
begin  
prog = irexec  
button = 5  
config = zapping\_remote "zapping.set\_channel(5)"  
end  
begin  
prog = irexec  
button = 6  
config = zapping\_remote "zapping.set\_channel(6)"  
end  
begin  
prog = irexec  
button = 7  
config = zapping\_remote "zapping.set\_channel(7)"  
end  
begin  
prog = irexec  
button = 8  
config = zapping\_remote "zapping.set\_channel(8)"  
end  
begin  
prog = irexec  
button = 9  
config = zapping\_remote "zapping.set\_channel(9)"  
end  
begin  
prog = irexec  
button = 0  
config = zapping\_remote "zapping.set\_channel(0)"  
end  
end zapping</code>
