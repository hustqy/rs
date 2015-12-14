
from args import Args

from docs import Documents


def main():

    args = Args().get_args()
    path = args.filename
    type = args.method
    user = args.userid

    news = Documents(path)
    matrix = news.parse()

    for item in matrix:
        if item.userid == user:
            print item.tags

    if type == 0:
        pass
    if type == 1:
        pass
