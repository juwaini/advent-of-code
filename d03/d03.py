def traversal(right, down):
    global_positions = [0]
    global_rows = [0]
    t_or_os = ['!']

    for x in range(0, 323 // down):
        global_positions.append((global_positions[-1] + right) % 31)
        global_rows.append(global_rows[-1] + down)

        assert len(global_positions) == len(global_rows)

        positions_and_lines = zip(global_positions, global_rows)

    map = []
    with open('input.txt') as input_data:
        for i in input_data:
            map.append(i.strip('\n'))

    for c in range(1, len(global_positions) - 1):
        if c == 0:
            continue
        else:
            t_or_os.append(map[global_rows[c]][global_positions[c]])

    return t_or_os.count('#')


def d03():
    # Part One
    print(f'Part 1: {traversal(3, 1)}')

    # Part Two
    print(f'{traversal(1, 1)=}')
    print(f'{traversal(3, 1)=}')
    print(f'{traversal(5, 1)=}')
    print(f'{traversal(7, 1)=}')
    print(f'{traversal(1, 2)=}')

    part_2_answer = traversal(1, 1) * traversal(3, 1) * traversal(5, 1) * traversal(7, 1) * traversal(1, 2)
    print(f'{part_2_answer = }')


if __name__ == '__main__':
    d03()
