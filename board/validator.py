import sys
import json


def error(msg):
    print(msg)
    exit(1)


def size_check(board_json):
    width = board_json["width"]
    height = board_json["height"]
    tiled = board_json["tiled"]
    points = board_json["points"]

    assert 10 <= width and width <= 20
    assert 10 <= height and height <= 20
    assert len(tiled) > 0
    assert len(tiled) == height
    assert len(tiled[0]) == width
    assert len(points) > 0
    assert len(points) == height
    assert len(points[0]) == width


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

    # テスト
    size_check(board_json)


if __name__ == '__main__':
    main()

