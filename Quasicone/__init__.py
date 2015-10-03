
# declare global parameter n

from parameters import parameters

def __init__(**kwargs):
    for k, v in kwargs.items():
        parameters[k] = v
    import Iterator, Strategy, Weyl_normal
    from Apply_strategy import  Apply_strategy#, Defect
    from Weyl_normal import Weyl_normal_form
