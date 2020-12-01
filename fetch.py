# coding: utf8
import pafy
import argparse


def download(url, path):
    best = pafy.new(url).getbest()
    best.download(filepath=path)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--url', help='url of youtube source',
    )
    parser.add_argument(
        '--path', help='path of downloading', default='D:\\'
    )
    args = parser.parse_args()
    return args.url, args.path


if __name__ == "__main__":
    url, path = get_args()
    download(url, path)

