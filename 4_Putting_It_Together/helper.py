# YOUR NAME HERE 
# TA SESSION 4 Intro To Programming
# helper.py


def get_ranks(input_dict):
    '''
    doc string will result in points off on the hw!

    Input:  input_dict - dictionary {'str': [list]}
    Output: ranks - dictionary {'str': {'str': int}}

    Example:
        Input:  {'X': ['B', 'A', 'C']}
        Output: {'X': {'A': 2, 'C': 3, 'B': 1}}
    '''
    ranks = {} 
    for key, val_list in input_dict.items():
        for position, name in enumerate(val_list): 
            inner_dict = {} 
            inner_dict[name] = position + 1
        ranks[key] = inner_dict

    return ranks
