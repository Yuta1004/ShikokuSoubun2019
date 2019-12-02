import sys


def main():
    if len(sys.argv) != 2:
        print("Usage : python3 validator.py (JSONPATH)")
        exit(0)

    print(sys.argv[1])


if __name__ == '__main__':
    main()

