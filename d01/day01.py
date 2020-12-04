def day_01():
    with open('input.txt') as input_data:
        ls = [int(i) for i in input_data]

        for x in range(len(ls)):
            for y in range(x + 1, len(ls)):
                if ls[x] + ls[y] == 2020:
                    print(ls[x] * ls[y])
                    break

        for x in range(len(ls)):
            for y in range(x + 1, len(ls)):
                for z in range(y + 1, len(ls)):
                    if ls[x] + ls[y] + ls[z] == 2020:
                        print(ls[x] * ls[y] * ls[z])
                        break


if __name__ == '__main__':
    day_01()
