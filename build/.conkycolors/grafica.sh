#!/bin/bash
asd=$(aticonfig --odgc)
echo $asd | awk '{ printf "${color}${goto 32}Clocks: ${font Ubuntu:style=Bold:size=8}${alignr 25}${color0}%s ${alignr 4}%s ${font}\n ${color}${goto 32}Peak: ${font Ubuntu:style=Bold:size=8}${color0}${alignr 25}%s ${alignr 4}%s ${font}\n" , $15 , $16 , $20 , $21 }'

