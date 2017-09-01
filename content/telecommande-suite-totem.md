Title: Télécommande suite : Totem
Date: 2005-08-15 04:24
Category: Informatique
Tags: GNU/Linux, Ubuntu, lirc, totem
Slug: telecommande-suite-totem
Status: published

Après avoir configuré la télécommande pour tvtime, je me suis attaqué a
totem dont voici la configuration (tvtime inclus) :

```
#/etc/lirc/lircrc
# Global launcher
begin
prog = irexec
button = tv
mode = tvtime
config = tvtime &
end
begin
prog = irexec
button = dvd
mode = totem
config = totem &
end

# Software specific  
## Totem  
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
button = max_window  
config = totem --fullscreen  
end  
end totem

## tvtime  
begin tvtime  
begin  
prog = irexec  
button = power  
config = tvtime-command QUIT  
end  
begin  
prog = irexec  
button = e  
config = tvtime-command TOGGLE_INPUT  
end  
begin  
prog = irexec  
button = launch_setup  
config = tvtime-command DISPLAY_INFO  
end  
begin  
prog = irexec  
button = max_window  
config = tvtime-command TOGGLE_FULLSCREEN  
end  
begin  
prog = irexec  
button = mute  
config = tvtime-command TOGGLE_MUTE  
end  
begin  
prog = irexec  
button = up  
config = tvtime-command UP  
end  
begin  
prog = irexec  
button = down  
config = tvtime-command DOWN  
end  
begin  
prog = irexec  
button = right  
config = tvtime-command RIGHT  
end  
begin  
prog = irexec  
button = left  
config = tvtime-command LEFT  
end  
begin  
prog = irexec  
button = vol-up  
config = tvtime-command MIXER_UP  
repeat = 1  
end  
begin  
prog = irexec  
button = vol-down  
config = tvtime-command MIXER_DOWN  
repeat = 1  
end  
begin  
prog = irexec  
button = chan-up  
config = tvtime-command CHANNEL_UP  
end  
begin  
prog = irexec  
button = chan-down  
config = tvtime-command CHANNEL_DOWN  
end  
begin  
prog = irexec  
button = dvd-root_menu  
config = tvtime-command CHANNEL_JUMP  
end  
begin  
prog = irexec  
button = 1  
config = tvtime-command CHANNEL_1 ENTER  
end  
begin  
prog = irexec  
button = 2  
config = tvtime-command CHANNEL_2 ENTER  
end  
begin  
prog = irexec  
button = 3  
config = tvtime-command CHANNEL_3 ENTER  
end  
begin  
prog = irexec  
button = 4  
config = tvtime-command CHANNEL_4 ENTER  
end  
begin  
prog = irexec  
button = 5  
config = tvtime-command CHANNEL_5 ENTER  
end  
begin  
prog = irexec  
button = 6  
config = tvtime-command CHANNEL_6 ENTER  
end  
begin  
prog = irexec  
button = 7  
config = tvtime-command CHANNEL_7 ENTER  
end  
begin  
prog = irexec  
button = 8  
config = tvtime-command CHANNEL_8 ENTER  
end  
begin  
prog = irexec  
button = 9  
config = tvtime-command CHANNEL_9 ENTER  
end  
begin  
prog = irexec  
button = 0  
config = tvtime-command CHANNEL_0  
end  
begin  
prog = irexec  
button = ok  
config = tvtime-command ENTER  
end  
end tvtime  
```
