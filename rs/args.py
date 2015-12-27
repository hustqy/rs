#!/usr/bin/python
import argparse
import sys



class Args:
    def __init__(self,arguments = None):
        self.__args = None
        self.__parse()

    def __parse(self):

        arguments = sys.argv[1:]
        if len(arguments) < 1:
            print "please specify at least 2 arguments,just -h for help"
            exit(-1)
        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description="""recommender system
""")
        parser.add_argument("-train", "--trainfile", metavar='<trainfile>', type=str, help="please specify the train data file")
        parser.add_argument("-test", "--testfile", metavar='<testfile>', type=str, help="please specify the text data file")
        parser.add_argument("-m", "--method", metavar='<method>', type=int, choices=xrange(0,3),help="""please specify method to recommend:

0 for user2user;1 for term2term;2 for others""")
        parser.add_argument("-u", "--userid", metavar='<userid>', type=int, help="please specify the user to recommend")
        self.__args = parser.parse_args(arguments)



    def get_args(self):
        return self.__args



if __name__ == "__main__":

    print  Args().get_args()