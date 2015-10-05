import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../..")

def main():
    print PROJECT_ROOT

    print os.path.exists("target")
    print "hello"

main()
