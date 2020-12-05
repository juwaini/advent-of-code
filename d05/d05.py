def get_seat_id(data):
    rows = [i for i in range(0, 128)]
    columns = [i for i in range(0, 8)]

    for d in data:
        if d == 'F':
            rows = rows[:len(rows) // 2]
        elif d == 'B':
            rows = rows[len(rows) // 2:]
        elif d == 'R':
            columns = columns[len(columns) // 2:]
        elif d == 'L':
            columns = columns[:len(columns) // 2]
        else:
            continue

    row = min(rows)
    column = min(columns)
    return (row * 8) + column


def d05():
    max_seat_id_list = []

    with open('input.txt') as input_data:
        for data in input_data:
            max_seat_id_list.append(get_seat_id(data))

    seat_id_list_sorted = sorted(max_seat_id_list)
    max_seat_id = max(max_seat_id_list)
    print(max_seat_id)
    for i in range(len(seat_id_list_sorted)):
        if seat_id_list_sorted[i] + 1 != seat_id_list_sorted[i + 1]:
            print(seat_id_list_sorted[i], seat_id_list_sorted[i + 1])
            break


if __name__ == '__main__':
    print(get_seat_id('BFFFBBFRRR'))
    print(get_seat_id('FFFBBBFRRR'))
    print(get_seat_id('BBFFBBFRLL'))

    d05()
