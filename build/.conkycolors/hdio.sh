#!/bin/bash
mount | awk '/sd/ {printf "${goto 32}${color0}sda ${goto 72}${color1}${diskiograph_read sda 10,40 5684ba E07A1F -t}${goto 75}${color2}${diskio_read }${goto 115}${color2}${diskiograph_write 10,40 5684ba E07A1F -t}${goto 120}${color2}$diskio_write "} '
