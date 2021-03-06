"""
computes the image of applying the initial strategy to each of
all quasicones
:input: iterator through quasicones
:output: the non-solved quasicones as pickle in the file 'default_outputfile.pi'
and as TeX in the file 'quasicones_rank[n].tex'
"""

import logging

logger = logging.getLogger(__name__)
# logger.propagate = False

import Quasicone
from Quasicone.Apply_strategy import Apply_strategy

number_of_exceptionals = None


def generate_list(**kwargs):
    """
    :kwargs: startweight, exceptionals
    """
    global number_of_exceptionals
    list_of_exceptionals = []
    initial_strategy = Quasicone.Strategy.initial()  # this is the shortest long strategy
    # initial_strategy = [1, -1]  # to test only the shortest strategy

    for mu, quasicone in enumerate(Quasicone.Iterator.iterator()):
        new_instance = Apply_strategy(
                quasicone, initial_strategy, startweight=kwargs['startweight'])
        new_instance.enumerator.append(mu)
        logger.debug('({}) new_instance.successful: {} -> \n {}'.format(
                mu, new_instance.successful, new_instance._C
        ))
        if new_instance.successful:
            pass  # do nothing
        else:
            list_of_exceptionals.append(new_instance)

    number_of_exceptionals = len(list_of_exceptionals)

    from utils import to_file
    to_file(list_of_exceptionals, kwargs['exceptionals'])

    import TeX
    filename = 'quasicones_rank{}.tex'.format(str(Quasicone.Iterator.n - 1))
    TeX.to_file(TeX.Quasicones_to_TeX(list_of_exceptionals), filename)
