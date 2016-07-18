# Defining our Csound ORC code within a triple-quoted, multline String
orc = """
sr=96000
ksmps=16
nchnls=2
0dbfs=1
instr 1
aout randh .3,3600

outs aout, aout
endin"""

