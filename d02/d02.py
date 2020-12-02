def d02():
    with open('input.txt') as input:
        ls = [i for i in input]

        correct = 0
        for l in ls:
            tmp = l.split()
            julat = tmp[0].split('-')
            char = tmp[1].split(':')[0]
            st = tmp[2]
            char_count = st.count(char)
            # print(julat, char, st, char_count)
            if char_count in range(int(julat[0]), int(julat[1]) + 1):
                correct += 1

        print(correct)

        new_correct = 0
        for l in ls:
            cnt = 0
            tmp = l.split()
            posisi = tmp[0].split('-')
            posisi1 = int(posisi[0])
            posisi2 = int(posisi[1])
            char = tmp[1].split(':')[0]
            st = tmp[2]
            if st[posisi1-1] == char:
                cnt += 1
            if st[posisi2-1] == char:
                cnt += 1

            if cnt == 1:
                new_correct += 1

        print(new_correct)

if __name__ == '__main__':
    d02()
