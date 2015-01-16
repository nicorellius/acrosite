"""
file        :   constructions.py
date        :   2015-01-16
module      :   common
description :   Constructions configuration file
"""

"""
KEY:
N = noun - use `noun`
V = verb - use `verb`
A = adjective - use `adj`
D = adverb - use `adv`

P = plural (modifies above 4) - use `plu`
S = singular (modifies above 4) - use `sin`
"""


def constant(f):

    def fset(self, value):
        raise SyntaxError

    def fget(self):
        return f()
    return property(fget, fset)


@constant
def NS_VS_D():
    return 'NS;VS;D;'

NS_VS_A_N = 'NS;VS;A;N'
NS_VS_A_D = 'NS;VS;A;D'
NP_VP_D = 'NP;VP;D;'
A_N = 'A;N'
A_A_N = 'A;A;N'
A_A_A_N = 'A;A;A;N'
A_A_A_A_N = 'A;A;A;A;;N'
A_A_A_A_A_N = 'A;A;A;A;A;N'
A_A_NP = 'A;A;NP'
A_A_A_NP_VP_D = 'A;A;A;NP;VP;D;'
A_A_NP_VP_D = 'A;A;NP;VP;D;'