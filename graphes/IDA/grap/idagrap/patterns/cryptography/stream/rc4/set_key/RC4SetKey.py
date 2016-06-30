#!/usr/bin/env python

from os.path import abspath, dirname

from idagrap.modules.Pattern import Pattern, Patterns

# Definition----------------------------------------------------------------
ROOT = dirname(abspath(__file__))

#
# Pattern
#
# RC4 set key first loop
loop1 = Pattern(f=ROOT + "/loop1.dot",
                name="First Loop",
                description="First Initialization loop of RC4 set_key.")

# RC4 set key second loop
loop2 = Pattern(f=ROOT + "/loop2.dot",
                name="Second Loop",
                description="Second Initialization loop of RC4 set_key.")


RC4_SET_KEY = Patterns(
    patterns=[
        loop1,
        loop2
    ],
    threshold=1.0,
    name="RC4 Set_Key()",
    description="Initialization function of the RC4 algorithm."
)
