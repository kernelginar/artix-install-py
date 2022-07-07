#!/usr/bin/env python

import os
import time

os.system("clear")

#locale
locale = input("Select locale [en/tr]: ")
if locale == 'en':
    os.system("echo 'en_US.UTF-8' >> /etc/locale.gen")
    os.system("locale-gen")
    os.system("clear")
    os.system("touch /etc/locale.conf")
    os.system("echo 'LANG=en_US.UTF-8' >> /etc/locale.conf")
    os.system("clear")
elif locale == 'tr':
    os.system("echo 'tr_TR.UTF-8' >> /etc/locale.gen")
    os.system("locale-gen")
    os.system("clear")
    os.system("touch /etc/locale.conf")
    os.system("echo 'LANG=tr_TR.UTF-8' >> /etc/locale.conf")
    os.system("clear")

os.system("clear")

#local machine
hostname = input("Hostname: ")
os.system("echo " f"{hostname} " ">> /etc/hostname")

os.system("echo '127.0.0.1       localhost' >> /etc/hosts")
os.system("echo '::1             localhost' >> /etc/hosts")
os.system("echo '127.0.1.1             '" f"{hostname}"".localdomain " f"{hostname}" " >> /etc/hosts")
os.system("clear")

#root user password
print("Root user password: ")
os.system("passwd")
os.system("clear")

#packages
os.system("pacman -Sy networkmanager networkmanager-openrc")
os.system("rc-update add NetworkManager default")
os.system("clear")

os.system("pacman -S xf86-input-libinput")
os.system("clear")

os.system("pacman -S ntfs-3g")
os.system("clear")

#grub
os.system("pacman -S grub efibootmgr os-prober")
os.system("clear")

os.system("grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Artix")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
time.sleep(2)
os.system("clear")

#useradd
username = input("Username: ")
os.system("useradd -m -g users -G wheel,storage,power,audio,video,network -s /bin/bash " f"{username}")
print("Normal user password: ")
os.system("passwd " f"{username}")
os.system("clear")
time.sleep(2)
os.system("EDITOR=nano visudo")
