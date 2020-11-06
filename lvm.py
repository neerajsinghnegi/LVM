import os

def show_hd():
    print("\n")
    os.system("lsblk")

def partition_hd():
    os.system("lsblk")
    hd = input("\n Enter Harddisk : ")
    os.system("fdisk /dev/{}".format(hd))
    os.system("udevadm settle")


def create_pv():
    os.system("lsblk")
    partition = input("Enter Hard Disk Partition : ")
    os.system("pvcreate /dev/{0}".format(partition))

def create_vg():
    vg_name = input("Give name to your VG : ")
    os.system("lsblk")
    partition = input("\n Enter Partition : ")
    os.system("vgcreate {0}  /dev/{1}".format(vg_name,partition))

def create_lv():
    print("\n All VGs...\n")
    os.system("vgs")
    lv_name = input("\n Give name to your LV : ")
    siz = input("How much you want to give space to LV : ")
    vg_name = input("Enter VG name : ")
    os.system("lvcreate --size {0}  --name {1} {2}".format(siz,lv_name,vg_name))

def format():
    os.system("vgs")
    os.system("lvs")
    vg_name = input("Enter VG name to format : ")
    lv_name = input("Enter LV name to format : ")
    os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_name,lv_name))

def mount():
    folder = input("Create Folder to Mount : ")
    os.system("mkdir {0}".format(folder))
    os.system("vgs")
    os.system("lvs")
    vg_name = input("Enter VG name to format : ")
    lv_name = input("Enter LV name to format : ")
    os.system("mount /dev/mapper/{0}-{1} {2}".format(vg_name,lv_name,folder))

while True:

    os.system("clear")

    print(""" LVM Automation
            1. Show Hard Disks

            2. Create Harddisk Partition

            3. Create PV (Physical Volume)

            4. Create VG (Volume Group)

            5. Create LV (Logical Volume)

            6. Format Partition

            7. Mount Partition

            Advanced

            8. Reduce LVM Partition

            9. Exit
            """)
    ch = int(input("Enter your choice : "))

    if ch == 1:
        show_hd()
        input("Press Enter to continue..")
        continue
    if ch == 2:
        partition_hd()
        print("Select your Harddisk and write below to do Partition")

    if ch == 3:
        create_pv()
        input("Press Enter to continue..")
        continue
    if ch == 4:
        create_vg()
        input("Press Enter to continue..")
        continue

    if ch == 5:
        create_lv()
        input("Press Enter to continue..")
        continue

    if ch == 6:
        format()
        input("Press Enter to continue..")
        continue

    if ch == 7:
        mount()
        input("Press Enter to continue..")
        continue

    if ch == 10:
        exit()

    else:
        input("Not supported.")
