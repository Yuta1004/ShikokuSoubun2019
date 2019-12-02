import sys
import json


def error(msg):
    print(msg)
    exit(1)


def main():
    # 引数検証
    if len(sys.argv) != 2:
        error("Usage : python3 validator.py (JSONPATH)")

    # JSON読み込み
    board_json = None
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            board_json = json.loads(f.read())
    except FileNotFoundError:
        error("FileNotFound : "+sys.argv[1])


if __name__ == '__main__':
    main()

