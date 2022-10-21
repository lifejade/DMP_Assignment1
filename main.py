import sys
import numpy as np
import cv2
import ctypes

screensize = 680


def checknQueen(x, y):
    check = True
    for i in range(0, n):
        if arr[i] == -1:
            continue

        if (i == x) or (arr[i] == y) or (abs(i - x) == abs(arr[i] - y)):
            check = False
            break

    return check


def on_mouse(event, x, y, flags, param):
    global board
    if event == cv2.EVENT_LBUTTONDOWN:
        arrx, arry = int(x / int(screensize / n)), int(y / int(screensize / n))
        if arr[arrx] == arry:
            return

        startPos = [arry * int(screensize / n) + int(screensize / n / 2 - queenSize[0] / 2),
                    arrx * int(screensize / n) + int(screensize / n / 2 - queenSize[1] / 2)]
        board[startPos[0]:startPos[0] + queenSize[0],
        startPos[1]:startPos[1] + queenSize[1]] += queen
        cv2.imshow('board', board)

        if not checknQueen(arrx, arry):
            ctypes.windll.user32.MessageBoxW(0, "you lose!!", "game over")
            sys.exit(0)

        arr[arrx] = arry
        for i in range(0, n):
            if arr[i] == -1:
                return
        ctypes.windll.user32.MessageBoxW(0, "YOU WIN!!", "GOOD GAME")
        sys.exit(0)


def makeBoard(n):
    cv2.line(board, (0, 0), (0, screensize), (0, 0, 0), 4, cv2.LINE_AA)
    cv2.line(board, (0, 0), (screensize, 0), (0, 0, 0), 4, cv2.LINE_AA)
    cv2.line(board, (screensize, 0), (screensize, screensize), (0, 0, 0), 4, cv2.LINE_AA)
    cv2.line(board, (0, screensize), (screensize, screensize), (0, 0, 0), 4, cv2.LINE_AA)
    for i in range(1, n):
        k = int(i * screensize / n)
        cv2.line(board, (k, 0), (k, screensize), (0, 0, 0), 4, cv2.LINE_AA)
        cv2.line(board, (0, k), (screensize, k), (0, 0, 0), 4, cv2.LINE_AA)


n = int(input("Input number of size(below 20) : "))
if n > 20:
    ctypes.windll.user32.MessageBoxW(0, "please input number below 20", "error", 16)
    sys.exit(0)

arr = [-1] * n
queenSize = int(screensize / (n + 1)), int(screensize / (n + 1))

board = np.ones((screensize, screensize, 3), dtype=np.uint8) * 255
queen = cv2.imread('queen.png')
queen = cv2.resize(queen, queenSize)

makeBoard(n)

cv2.namedWindow('board')
cv2.setMouseCallback('board', on_mouse, board)
cv2.imshow('board', board)
cv2.waitKey()


cv2.destroyAllWindows()
