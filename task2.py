import random

servers_list = []

def mirrorMatrix():
    global servers_list
    n = int(input('Размерность NxN, N = '))
    servers_list = [[random.sample(range(100), 1) for i in range(n)] for j in range(n)]
    for row in range(n):
        for col in range(n):
            if row % 2 != 0:
                servers_list[row][col][0] = servers_list[row-1][col-1][0]

if __name__ == '__main__':
    mirrorMatrix()
    for row in servers_list:
        print(row)
