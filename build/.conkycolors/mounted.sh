#!/bin/bash
mount |grep -v home| awk '/dev\/sd/ {printf "${color}"$3" ${goto 75}${if_match ${fs_used_perc "$3"} >85}${color red}${else}${if_match ${fs_used_perc "$3"} >65}${color2}${else}${color1}${endif}${endif}${fs_bar 10,40 "$3"}${goto 75}${color0}${fs_free "$3"}${alignr}${color1}${fs_size "$3"}\n "} '

