import csnd6
from random import randint
from math import sin
execfile('orchestra.py')


# Defining our Csound SCO code

sco = ""
t = 0
for x in range(0, 300):
	sco += "i1 "+ `t` +" .01 "+ `randint(100,1000)` +" "+ `randint(1000,2000)` +"\n"
	t+=sin(20*t+1)*sin(20*t+1)


c = csnd6.Csound()
c.SetOption("-odac")  # Using SetOption() to configure Csound
                      # Note: use only one commandline flag at a time
c.CompileOrc(orc)     # Compile the Csound Orchestra string
c.ReadScore(sco)      # Compile the Csound SCO String
c.Start()  # When compiling from strings, this call is necessary before doing any performing
c.Perform()  # Run Csound to completion
c.Stop()
