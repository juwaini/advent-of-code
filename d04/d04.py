import re

replchars = re.compile(r'[\n\r]')
replcomma = re.compile(r';')
hexstr = re.compile(r'#[0-9a-f]{6}')


def replchars_to_hex(match):
    return r'\x{0:02x}'.format(ord(match.group()))


def replchars_to_comma(match):
    return r';'


def replcomma_to_space(match):
    return r' '


valid_fields = (
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # 'cid',
)


def check_validity(value, key):
    if key != 'cid' and key not in valid_fields:
        return False

    if key == 'byr' and int(value) in range(1920, 2003):
        return True

    if key == 'iyr' and int(value) in range(2010, 2021):
        return True

    if key == 'eyr' and int(value) in range(2020, 2031):
        return True

    if key == 'hgt':
        if 'cm' in value and int(value.split('cm')[0]) in range(150, 194):
            return True
        if 'in' in value and int(value.split('in')[0]) in range(59, 77):
            return True

    if key == 'hcl':
        return (
                (value[0] == '#') and
                all(
                    value[i] in '0123456789abcdef' for i in range(1, len(value))
                )
        )

    if key == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    if key == 'pid':
        return len(value) == 9 and all(value[i] in '0123456789' for i in range(0, len(value)))

    if key == 'cid':
        return True

    return False


def d04():
    # Part One
    damnlongstring = ''
    with open('input.txt') as input_data:
        for i in input_data:
            damnlongstring += replchars.sub(replchars_to_comma, i)

    passports = damnlongstring.split(';;')
    passports = [replcomma.sub(replcomma_to_space, passport) for passport in passports]

    valid_passport = 0
    valid_passport_list = []
    for passport in passports:
        if all(f in passport for f in valid_fields):
            valid_passport += 1
            valid_passport_list.append(passport)

    print(f'{valid_passport=}')

    # Part Two

    valid_passport_part_2 = 0
    for v in valid_passport_list:
        v_dict = {}
        valid = v.split(' ')
        for val in valid:
            tmp = val.split(':')
            v_dict[tmp[0]] = tmp[1]
        if all(check_validity(v_dict[k], k) for k in v_dict.keys()):
            valid_passport_part_2 += 1

    print(f'{valid_passport_part_2=}')


if __name__ == '__main__':
    assert check_validity('2003', 'byr') == False
    assert check_validity('2002', 'byr') == True

    assert check_validity('60in', 'hgt') == True
    assert check_validity('190cm', 'hgt') == True
    assert check_validity('190in', 'hgt') == False
    assert check_validity('190', 'hgt') == False

    assert check_validity('#123abc', 'hcl') == True
    assert check_validity('#123abz', 'hcl') == False
    assert check_validity('123abc', 'hcl') == False

    assert check_validity('brn', 'ecl') == True
    assert check_validity('wat', 'ecl') == False

    assert check_validity('0123456789', 'pid') == False
    assert check_validity('000000001', 'pid') == True
    d04()
