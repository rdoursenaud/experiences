---
subject: 'Informatique • IT'
---
https://www.acer.com/fr-fr/support/product-support/CB3-431

Chromebook ACER CB3 - 431 - C2WG
Manufacturing date : 2018/04/17
Google edgar

N1600
4G DDR
16G eMMC

Pop!_OS

## Chromebook keyboard

```sh
sudo tee /etc/udev/hwdb.d/90-chromebook-azerty.hwdb > /dev/null <<'EOF'
# Acer Chromebook 14 (Edgar) - rangée du haut : icônes -> fonctions dédiées
evdev:atkbd:dmi:bvn*:bvr*:bd*:svnGOOGLE:pnEdgar:pvr*
 KEYBOARD_KEY_3b=back            # F1  -> Précédent (navigateur)
 KEYBOARD_KEY_3c=forward         # F2  -> Suivant (navigateur)
 KEYBOARD_KEY_3d=refresh         # F3  -> Actualiser
 KEYBOARD_KEY_3e=fullscreen      # F4  -> Plein écran
 KEYBOARD_KEY_3f=scale           # F5  -> Vue activité (Toutes les fenêtres)
 KEYBOARD_KEY_40=brightnessdown  # F6  -> Luminosité -
 KEYBOARD_KEY_41=brightnessup    # F7  -> Luminosité +
 KEYBOARD_KEY_42=mute            # F8  -> Mute
 KEYBOARD_KEY_43=volumedown      # F9  -> Volume -
 KEYBOARD_KEY_44=volumeup        # F10 -> Volume +
EOF
sudo systemd-hwdb update
sudo udevadm trigger --subsystem-match=input --action=change
```
