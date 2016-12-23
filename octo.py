# Example 2 - Compilation with Csound without CSD
# Author: Steven Yi <stevenyi@gmail.com>
# 2013.10.28
#
# In this example, we move from using an external CSD file to 
# embedding our Csound ORC and SCO code within our Python project.
# Besides allowing encapsulating the code within the same file,
# using the CompileOrc() and CompileSco() API calls is useful when
# the SCO or ORC are generated, or perhaps coming from another 
# source, such as from a database or network.

import csnd6

# Defining our Csound ORC code within a triple-quoted, multline String
orc = """
sr=96000
ksmps=9600
nchnls=2
0dbfs=1
instr 1
amod randh 2200, 44 
aout randi 0.5, 4400 +amod
outs aout, aout
endin"""


# Defining our Csound SCO code 
sco = "i1 0 10"

c = csnd6.Csound()
c.SetOption("-otest.wav")  # Using SetOption() to configure Csound
                      # Note: use only one commandline flag at a time

c.CompileOrc(orc)     # Compile the Csound Orchestra string
c.ReadScore(sco)      # Compile the Csound SCO String
c.Start()  # When compiling from strings, this call is necessary before doing any performing
c.Perform()  # Run Csound to completion
c.Stop()
