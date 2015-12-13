
from args import Args

from news import News

from tfidf import Tfidf


def main():

    args = Args().get_args()
    path = args.filename
    type = args.method

    news = News(path)

    if type == 0:
        Tfidf(news)

    if type == 1:
        pass
