
# declare global parameter n

import parameters

def __init__(n):
    parameters.n = n
    import Iterator, Strategy, Weyl_normal
    from Apply_strategy import  Apply_strategy#, Defect
    from Weyl_normal import Weyl_normal_form
