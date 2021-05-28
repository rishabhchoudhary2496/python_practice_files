import random
import pprint


def shuffleItems(*args):
    '''Takes a collection and shuffles the order
    
        input -> any collection
        return value -> collection
    '''
    chosen_list = list(*args)
    random.shuffle(chosen_list)
    return chosen_list


if __name__ == '__main__':
    pprint.pprint(dir())