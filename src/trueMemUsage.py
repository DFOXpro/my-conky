#! /usr/bin/env python

"""
		Print a more accurate mem usage
		in conky
"""

from __future__ import print_function


MemTotal = MemFree = Buffers = Cached = 0.0

"""
SLine = String that maybe contain the value.
SName = String name of the value.
VContainer = Variable that will contain the value
"""
def getValue(SLine, SName, VContainer):
	if SLine and SLine.rstrip('\n').startswith(SName):
		VContainer = float(SLine.rstrip('\n').split(':')[1].replace(' ', '').replace('kB', ''))/1048576#GB
		#print(VContainer)
	return VContainer

def percentage(Ivalue):
	return (Ivalue*100)/(MemTotal)


with open('/proc/meminfo') as f:
	for line in f:
		MemTotal = getValue(line, 'MemTotal:', MemTotal)
		MemFree = getValue(line, 'MemFree:', MemFree)
		Buffers = getValue(line, 'Buffers:', Buffers)
		Cached = getValue(line, 'Cached:', Cached)

MemTrueUsage = (MemTotal-MemFree)-(Buffers+Cached)
MemTrueUsagePercentage = percentage(MemTrueUsage)
#MemUsagePercentage = percentage(MemTotal-MemFree)

#print(MemTotal, MemFree, Buffers, Cached)
#print('MemAppUsage:',MemTrueUsage, str(MemTrueUsagePercentage)+'%')
#print(str(MemTrueUsagePercentage))
#print('MemUsage:', str(MemUsagePercentage)+'%')

toRender = """${%(color)s}${font Poky:size=14}M#
${voffset -3}${goto 28}${font Ubuntu:style=Bold:size=8}${color1}#
Memory:#
${font}#
${goto 100}${color0}${execbar echo "%(totalUsage)d" 10,60}#
${goto 100}${color2}${execbar echo "%(MemTrueUsagepercentage)d" 10,60 5684ba E07A1F -t}#
${goto 135}${color2}%(totalUsage)d%%#
${goto 104}${color1}%(MemTrueUsagepercentage)d%%
${color}Task Used: ${alignr}${color0}%(MemTrueUsage).2fG
${color}Buffers: ${alignr}${color0}%(Buffers).2fG
${color}Cached: ${alignr}${color0}%(Cached).2fG
${color}Swap: ${alignr}${color0}$swap
${color}Total: ${alignr}${color0}%(MemTotal).2fG#"""
#See https://github.com/brndnmtthws/conky/issues/153
# https://github.com/brndnmtthws/conky/issues/224
#${color}History:#
#${goto 100}${color0}${execgraph echo "%(totalUsage)d"}#
#${goto 100}${color2}${execgraph echo "%(MemTrueUsagepercentage)d" 10,60 5684ba E07A1F -t}#

print(toRender % \
	{
		'totalUsage':percentage(MemTotal-MemFree),
		'MemTrueUsagepercentage':MemTrueUsagePercentage,
		'MemTrueUsage':MemTrueUsage,
		'Buffers':Buffers,
		'Cached':Cached,
		'MemTotal':MemTotal,
# red, color2, color0
		'color':('color red' if(MemTrueUsagePercentage>80) else 'color2' if(MemTrueUsagePercentage>50) else 'color0')
	}
)