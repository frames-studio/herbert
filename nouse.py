import csnd6
from random import randint
from math import sin
execfile('orchestran.py')


# Defining our Csound SCO code

sco = ""
t = 0
dur = 1.0/60.0
for x in range(0, 300):
	sco += "i1 "+  `x/13.0` +  " " + `dur` + " \n"
	sco += "i1 "+  `.1 + x/11.0` +  " " + `dur` + " \n"
	sco += "i1 "+  `.2 + x/9.0` +  " " + `dur` + " \n"

       
c = csnd6.Csound()
c.SetOption("-odac")  # Using SetOption() to configure Csound
                      # Note: use only one commandline flag at a time
c.CompileOrc(orc)     # Compile the Csound Orchestra string
c.ReadScore(sco)      # Compile the Csound SCO String
c.Start()  # When compiling from strings, this call is necessary before doing any performing
c.Perform()  # Run Csound to completion
c.Stop()
