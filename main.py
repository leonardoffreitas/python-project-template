import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Project Template")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--many", dest="param", action="store_true", default=False, help="help single param")
    group.add_argument("-m", "--single", dest="params", nargs="+", metavar="<param>", help="help many params")
    results = parser.parse_args()

    if results.params:
        print(results.params)
    if results.param:
        print(results.param)


if __name__ == "__main__":
    main()
