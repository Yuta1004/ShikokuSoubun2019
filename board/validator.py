# -*- coding: utf-8 -*-

import sys
import json
from simulator import Game, Board

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
    except AssertionError as aserr:
        test_fail(check_func)
        print(aserr.args[0])
    except Exception as excep:
        test_fail(check_func)
        print(excep.args[0])
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

    assert 10 <= width and width <= 20 , "widthは10以上20以下である必要があります"
    assert 10 <= height and height <= 20, "heightは10以上20以下である必要があります"
    assert len(tiled) > 0, "tiledのサイズが不正です"
    assert len(tiled) == height, "tiledの高さとheightが一致しません"
    assert len(tiled[0]) == width, "tiledの幅とwidthが一致しません"
    assert len(points) > 0, "pointsのサイズが不正です"
    assert len(points) == height, "pointsの高さとheightが一致しません"
    assert len(points[0]) == width, "pointsの高さとwidthが一致しません"


# startedAtUnixTime
def check_start_time(board_json):
    assert board_json["startedAtUnixTime"] == 0, "startedAtUnixTimeは0である必要があります"


# turn
def check_turn(board_json):
    assert board_json["turn"] == 0, "turnは0である必要があります"

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
    assert teams[0]["teamID"] == 1, "teamIDは1 or 2である必要があります"
    assert teams[1]["teamID"] == 2, "teamIDは1 or 2である必要があります"
    assert len(teams[0]["agents"]) == len(teams[1]["agents"]), "チーム1とチーム2のエージェント数が一致しません"

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
        assert 1 <= x and x <= width, "エージェントのx座標は1以上width以下である必要があります"
        assert 1 <= y and y <= height, "エージェントのy座標は1以上height以下である必要があります"
    assert len(agent_ids) == len(agents), "IDが重複しているエージェントが存在します"


# tiled, teams
def check_agent_pos(board_json):
    tiled = board_json["tiled"]
    for team in range(1, 3):
        for agent in board_json["teams"][team-1]["agents"]:
            x = agent["x"]-1
            y = agent["y"]-1
            assert tiled[y][x] == team, "エージェントの配置情報とtiledが一致しません => ("+str(x+1)+","+str(y+1)+")"

# actions
def check_actions(board_json):
    assert len(board_json["actions"]) == 0, "actionsは長さ0のリストである必要があります"


# init_score
def check_init_score(board_json):
    width = board_json["width"]
    height = board_json["height"]
    points = board_json["points"]
    tiled = board_json["tiled"]
    teams = [None, None, None]
    teams[1] = board_json["teams"][0]
    teams[2] = board_json["teams"][1]

    board = Board(width, height, points, tiled)
    agents = []
    game = Game(board, agents)
    score = game.cal_score([1, 2])

    for team_id in range(1, 3):
        assert teams[team_id]["tilePoint"] == score[team_id]["tilePoint"],\
            "チーム"+str(team_id)+"のタイルポイントが不正です => tilePoint: "+str(score[team_id]["tilePoint"])
        assert teams[team_id]["areaPoint"] == score[team_id]["areaPoint"],\
            "チーム"+str(team_id)+"のエリアポイントが不正です => areaPoint: "+str(score[team_id]["areaPoint"])


# points(range)
def check_points_range(board_json):
    points = board_json["points"]
    width = len(points[0])
    height = len(points)
    for y in range(height):
        for x in range(width):
            assert -16 <= points[y][x] <= 16, "pointsの各要素は-16以上16以下である必要があります => ("+str(x+1)+","+str(y+1)+")"


# tiled, points(symmetry)
def check_points_tiled_symmetry(board_json):
    cnt = 0
    tiled = board_json["tiled"]
    tiled = __convert_tiled_flat(tiled)
    points = board_json["points"]

    cnt += (__check_symmetry_h(tiled) and __check_symmetry_h(points))
    cnt += (__check_symmetry_v(tiled) and __check_symmetry_v(points))
    cnt += (__check_symmetry_r(tiled) and __check_symmetry_r(points))
    assert cnt > 0, "points, tiledの配置は上下、左右、点のいずれかで対称である必要があります"


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
        test(check_init_score, board_json)
        test(check_teams, board_json)
        test(check_agent_pos, board_json)
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

