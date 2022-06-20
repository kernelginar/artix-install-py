import os

os.system("clear")
os.system("lsblk")
print(" ")
disk_selection = input("Select disk (example /dev/sda), /dev/???: ")
os.system("cfdisk " f"{disk_selection}")

os.system("clear")
os.system("lsblk")
print(" ")

root_partition = input("Root partition (example /dev/sda1), /dev/???: ")
os.system("mkfs.ext4 " f"{root_partition}")
os.system("mount " f"{root_partition} " "/mnt")
print(" ")

boot_partition = input("Boot partition (example /dev/sda1), /dev/???: ")
os.system("mkfs.fat -F32 " f"{boot_partition}")
os.system("mkdir -p /mnt/boot/efi")
os.system("mount " f"{boot_partition} " "/mnt/boot/efi")

os.system("clear")
os.system("basestrap -i /mnt base base-devel linux linux-headers linux-firmware runit git nano")
os.system("fstabgen -U /mnt >> /mnt/etc/fstab")
os.system("cp $(pwd)/chroot.py /mnt")
os.system("artix-chroot /mnt /bin/bash")
