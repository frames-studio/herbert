import csnd6


# Defining our Csound ORC code within a triple-quoted, multline String
orc = """
sr=96000
ksmps=16
nchnls=2
0dbfs=1
instr 1
aout vco2 0.5, 440
amod vco2 1, 3333

outs aout*amod, aout*amod
endin"""


# Defining our Csound SCO code
sco = "i1 0 .1"


c = csnd6.Csound()
c.SetOption("-odac")  # Using SetOption() to configure Csound
                      # Note: use only one commandline flag at a time

c.CompileOrc(orc)     # Compile the Csound Orchestra string
c.ReadScore(sco)      # Compile the Csound SCO String
c.Start()  # When compiling from strings, this call is necessary before doing any performing
c.Perform()  # Run Csound to completion
c.Stop()