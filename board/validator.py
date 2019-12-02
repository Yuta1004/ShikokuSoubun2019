import sys
import json


def error(msg):
    print(msg)
    exit(1)


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
        x = agent["x"]
        y = agent["y"]
        agent_ids.add(agent["agentID"])
        assert 1 <= x and x <= width
        assert 1 <= y and y <= height
    assert len(agent_ids) == len(agents)


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
    check_size(board_json)
    check_start_time(board_json)
    check_turn(board_json)
    check_teams(board_json)


if __name__ == '__main__':
    main()

