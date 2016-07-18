# Defining our Csound ORC code within a triple-quoted, multline String
orc = """
sr=96000
ksmps=16
nchnls=2
0dbfs=1
instr 1
aout randi 0.5, p4
amod randh 1, p5

outs aout*amod, aout*amod
endin"""

