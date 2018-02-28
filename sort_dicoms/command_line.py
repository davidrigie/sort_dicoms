import sort_dicoms
import sys

usage = """
expected 1 argument

usage: sort_dicoms [dirpath]
"""

def check_args(arglist):
    if len(arglist) != 2:
        print(usage)
        return False
    
    return True


def main():
    if check_args(sys.argv):
        rootdir = sys.argv[1]
        sort_dicoms.sort_dicoms(rootdir)
    



        