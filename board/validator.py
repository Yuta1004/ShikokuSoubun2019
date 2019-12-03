# -*- coding: utf-8 -*-

import sys
import json

success_cnt = 0
fail_cnt = 0


def test_success(check_func):
    global success_cnt
    success_cnt += 1
    print("\033[32m\033[1mSuccess\033[0m : "+check_func.__name__)


def test_fail(check_func):
    global fail_cnt
    fail_cnt += 1
    print("\033[31m\033[1mFailed\033[0m : "+check_func.__name__)


def error(msg):
    print(msg)
    exit(1)


def test(check_func, board_json):
    try:
        check_func(board_json)
    except AssertionError:
        test_fail(check_func)
    else:
        test_success(check_func)


def read_board_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        error("FileNotFound : "+path)


# width, height
def check_size(board_json):
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


# startedAtUnixTime
def check_start_time(board_json):
    assert board_json["startedAtUnixTime"] == 0


# turn
def check_turn(board_json):
    assert board_json["turn"] == 0

# teams
def check_teams(board_json):
    teams = board_json["teams"]
    width = board_json["width"]
    height = board_json["height"]
    tiled = board_json["tiled"]

    # ID
    if teams[0]["teamID"] == 2:
        tmp = teams[0]
        teams[0] = teams[1]
        teams[1] = tmp
    assert teams[0]["teamID"] == 1
    assert teams[1]["teamID"] == 2
    assert len(teams[0]["agents"]) == len(teams[1]["agents"])

    # Agents
    agents = []
    agent_ids = set()
    agents.extend(teams[0]["agents"])
    agents.extend(teams[1]["agents"])
    for agent in agents:
        _id = agent["agentID"]
        x = agent["x"]
        y = agent["y"]
        agent_ids.add(_id)
        assert 1 <= x and x <= width
        assert 1 <= y and y <= height
        assert tiled[y-1][x-1] == (_id>len(agents)/2)+1
    assert len(agent_ids) == len(agents)


# actions
def check_actions(board_json):
    assert len(board_json["actions"]) == 0


# points(range)
def check_points_range(board_json):
    points = board_json["points"]
    width = len(points[0])
    height = len(points)
    for y in range(height):
        for x in range(width):
            assert -16 <= points[y][x] <= 16


# tiled, points(symmetry)
def check_points_tiled_symmetry(board_json):
    cnt = 0
    tiled = board_json["tiled"]
    tiled = __convert_tiled_flat(tiled)
    points = board_json["points"]

    cnt += (__check_symmetry_h(tiled) and __check_symmetry_h(points))
    cnt += (__check_symmetry_v(tiled) and __check_symmetry_v(points))
    cnt += (__check_symmetry_r(tiled) and __check_symmetry_r(points))
    assert cnt > 0


def __convert_tiled_flat(tiled):
    new_tiled = []
    for y in range(len(tiled)):
        new_tiled.append([])
        for x in range(len(tiled[y])):
            new_tiled[y].append(1 if tiled[y][x] > 0 else 0)
    return new_tiled


def __check_symmetry_h(board):
    result = True
    width = len(board[0])
    height = len(board)
    for y in range(height):
        for x in range(int(width/2+1)):
            result &= (board[y][x] == board[y][width-x-1])
    return result


def __check_symmetry_v(board):
    result = True
    width = len(board[0])
    height= len(board)
    for y in range(int(height/2+1)):
        for x in range(width):
            result &= (board[y][x] == board[height-y-1][x])
    return result


def __check_symmetry_r(board):
    result = True
    width = len(board[0])
    height = len(board)
    for y in range(height):
        for x in range(width):
            result &= (board[y][x] == board[height-y-1][width-x-1])
    return result


def main():
    # 引数検証
    if len(sys.argv) < 2:
        error("Usage : python3 validator.py (JSONPATH)")

    # テスト実行
    for path in sys.argv[1:]:
        print("\033[1m"+path+"\033[0m")
        board_json = read_board_json(path)
        test(check_size, board_json)
        test(check_start_time, board_json)
        test(check_turn, board_json)
        test(check_teams, board_json)
        test(check_actions, board_json)
        test(check_points_range, board_json)
        test(check_points_tiled_symmetry, board_json)
        print()

    # 結果表示
    print("\033[1mResult\033[0m")
    print("- \033[32m\033[1mSuccess : "+str(success_cnt)+"\033[0m")
    print("- \033[31m\033[1mFail : "+str(fail_cnt)+"\033[0m")
    exit(fail_cnt != 0)


if __name__ == '__main__':
    main()

