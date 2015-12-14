
from args import Args

from Core import Core


def main():

    args = Args().get_args()
    Core(args).recommend()