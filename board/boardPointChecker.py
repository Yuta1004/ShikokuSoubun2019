import sys
import json

def error(msg):
    print(msg)
    exit(1)


def read_board_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        error("FileNotFound : "+path)


def print_board(path_list):
    for path in path_list:
        print("\033[1m"+path+"\033[0m")
        board_json = read_board_json(path)
        for n in range(-16, 17):
            print("\033[1mpoint"+str(n)+"\033[0m")
            for i in board_json["points"]:
                for j in i:
                    if int(j) != n:
                        j = "---"
                    print('{:>3}'.format(j), end=',')
                print()


def main():
    if len(sys.argv) < 2:
        error("Usage : python3 validator.py (JSONPATH)")
    print_board(sys.argv[1:])


if __name__ == '__main__':
    main()