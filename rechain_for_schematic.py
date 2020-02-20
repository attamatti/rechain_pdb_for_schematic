#!/usr/bin/env python

## rechain a fibril with all of the chains as X for takinoris script
import sys

try:
    pdbdata = open(sys.argv[1],'r').readlines()
except:
    sys.exit('USAGE: rechain_for_schematic.py <pdb flile>')

output = open('r_{0}'.format(sys.argv[1]),'w')
atn = 1
aan = 1
lino = 0
for line in pdbdata:
    if line[:4] == 'ATOM':
        newline = line[:7]+'{0:04d}'.format(atn)+line[11:21]+'X {0:03d}'.format(aan)+line[27:]
        output.write(newline)
        try:
            if int(line[22:26]) < int(pdbdata[lino+1][22:26]):
                aan+=1
        except:
            output.write('TER\n')
        atn+=1
    if line[:3] == 'TER':
        output.write('TER\n')
        aan+=10
        atn+=10
    lino+=1
 
        
    
    
