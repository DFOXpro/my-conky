#! /usr/bin/env python

"""
		Print if arg app is running independent of the owner
		in conky
"""

import sys, getopt, commands, collections

colors = ['color green', 'color']
initialmarkup = '${voffset 3}#'
font = '${font %s:size=14}#'
toRender = ''' ${%(color)s}%(programShortName)s#'''
endmarkup = '${font}${voffset 3}'


# Don't touch
if len(sys.argv) < 2:
	sys.exit('''Usage: %s  -l program-name -s program-short-name
-l : the actual name of the program
-s : the abbreviation of the program
-f : icon-font to use
-u true : if use unicode font
Example: %s -l apache -l mysqld -s A2 -s MS -f appzIcon''' % sys.argv[0])
else:
	opts, args = getopt.getopt(sys.argv[1:], "l:s:f:u")
	d = collections.defaultdict(list)
	for o in opts:
		d[o[0]].append(o[1])
	#print d, opts

	if len(d['-l']) != len(d['-s']):
		sys.exit('long names does not match with short names')
	else:
		print initialmarkup
		if len(d['-f']) > 0: print font % d['-f'][0]
		useUnicode = len(d['-u']) > 0
		#print useUnicode
		for i in range(len(d['-l'])):
			isRunning = len(max(commands.getstatusoutput('pidof '+ d['-l'][i]))) > 0
			print(toRender % \
				{
					'programShortName': (unichr(int(d['-s'][i], 16)).encode('utf-8') if (useUnicode) else d['-s'][i]),
					'color': (colors[0] if (isRunning) else colors[1])
				}
		)
		print endmarkup
