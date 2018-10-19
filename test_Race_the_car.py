import pytest
import Race_the_car

BOARDWIDTH = Race_the_car.BOARDWIDTH
BOARDHEIGHT = Race_the_car.BOARDHEIGHT

OPEN_SPACE = Race_the_car.OPEN_SPACE
PLAYER_ONE = Race_the_car.PLAYER_ONE
PLAYER_TWO = Race_the_car.PLAYER_TWO

BOARDWIDTH_CENTER = Race_the_car.BOARDWIDTH_CENTER
ONE_STARTING_ROW = Race_the_car.ONE_STARTING_ROW
TWO_STARTING_ROW = Race_the_car.TWO_STARTING_ROW

def test_getStartingBoard():
    board = Race_the_car.getStartingBoard(OPEN_SPACE)

    # player 1 position correct
    assert board[BOARDWIDTH_CENTER][ONE_STARTING_ROW] == PLAYER_ONE 
    board[BOARDWIDTH_CENTER][ONE_STARTING_ROW] = OPEN_SPACE

    # player 2 position correct
    assert board[BOARDWIDTH_CENTER][TWO_STARTING_ROW] == PLAYER_TWO
    board[BOARDWIDTH_CENTER][TWO_STARTING_ROW] = OPEN_SPACE

    # Everything else empty spaces
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            assert board[x][y] == OPEN_SPACE

    # proper behavior if input is changed
    board = Race_the_car.getStartingBoard(0)
    assert board[BOARDWIDTH_CENTER][ONE_STARTING_ROW] == PLAYER_ONE
    board[BOARDWIDTH_CENTER][ONE_STARTING_ROW] = 0
    assert board[BOARDWIDTH_CENTER][TWO_STARTING_ROW] == PLAYER_TWO
    board[BOARDWIDTH_CENTER][TWO_STARTING_ROW] = 0
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            assert board[x][y] == 0

    return

