if __name__ == '__main__':
    testaja = []
    testaja2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        testaja.append([score, name])
    for i in testaja:
        testaja2.append(i[0])
    x = sorted(list(set(testaja2)))
    for k in sorted(testaja):
        if k[0] == x[1]:
           print(k[1])
