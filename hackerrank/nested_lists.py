if __name__ == '__main__':
    testaja = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        testaja.append([score, name])
    for i in testaja:
        print(i[0], end='')
    # if (x[1][0] == x[2][0]):
        # print(x[1][0], x[2][0])
    # else:
        # print(x[1][0])

