#!/bin/bash
ACTION=$1
DEVBASE=$2
mountDir="/mnt/usb"                        # recommended USB mount point - /media causes problems
if [ ! -d $mountDir ]; then                # mount point does not exists
  mkdir $mountDir
  if [ $? != 0 ]; then exit 1; fi          # unable to create mount point  
fi  
DEVICE="/dev/${DEVBASE}"
MOUNT_POINT=$(/bin/mount | /bin/grep ${DEVICE} | /usr/bin/awk '{ print $3 }')  # See if this drive is already mounted
case "${ACTION}" in
    add)
        if [[ -n ${MOUNT_POINT} ]]; then exit 2; fi # Already mounted, exit
        eval $(/sbin/blkid -o udev ${DEVICE})       # Get info for this drive: $ID_FS_LABEL, $ID_FS_UUID, and $ID_FS_TYPE
        OPTS="rw,relatime"                          # Global mount options
        if [[ ${ID_FS_TYPE} == "vfat" ]]; then OPTS+=",users,gid=100,umask=000,shortname=mixed,utf8=1,flush"; fi     # File system type specific mount options
        if ! /bin/mount -o ${OPTS} ${DEVICE} /mnt/usb/; then exit 3; fi # Error during mount process: cleanup mountpoint
        ;;
    remove)
        if [[ -n ${MOUNT_POINT} ]]; then /bin/umount -l ${DEVICE}; fi
        ;;
esac
