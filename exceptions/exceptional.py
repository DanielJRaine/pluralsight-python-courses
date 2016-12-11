'''A module for demonstrating exceptions'''

import sys


def convert(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError("innappropriate value error, of correct type"),
            TypeError("incorrect type")) as err:
        print("conversion error: {}".format(str(err)), file=sys.stderr)
    raise  # re-raises the excetion being currently handled
