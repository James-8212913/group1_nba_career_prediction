#!/usr/bin/env python3
"""
Author : James M
Purpose: This is a test script using functions from another file
"""

from functions import add

def get_args():
    """command line arguments to be input by the user"""
    parser = argparse.ArgumentParser(
        description='{args.purpose}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('x',
                        metavar = 'x',
                        type = int,
                        help = 'Two numbers to be added together')

def my_main():
    """This function will add two numbers together"""
    sum = add(x,y)
    print("sum is {}".format(sum))

if __name__=="__main__":
    my_main()
