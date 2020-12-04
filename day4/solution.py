import re
from typing import List, Dict

def prepare_input(input: str) -> List[Dict[str, str]]:
    elements = re.split(r'\n{2,}', input.strip())
    passport_lines = [re.split(r'[ \n]', e.strip()) for e in elements]
    passports = list()

    for line in passport_lines:
        passport = dict()

        for field in line:
            key, value = field.split(':')
            passport[key] = value
        
        passports.append(passport)

    return passports

def day4(input: List[Dict[str, str]]):
    count = 0
    for i in input:
        if all (k in i for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
           count += 1
    return count


def day4_part2(input: List[Dict[str, str]]):
    count = 0
    for i in input:
        valid = all (k in i for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))

        if not valid:
            continue
        
        valid = valid and (1920 <= int(i['byr']) <= 2002)
        valid = valid and (2010 <= int(i['iyr']) <= 2020)
        valid = valid and (2020 <= int(i['eyr']) <= 2030)

        valid = valid and (i['hgt'].endswith('cm') or i['hgt'].endswith('in') )

        if i['hgt'].endswith('cm'):
            valid = valid and (150 <= int(i['hgt'][:-2]) <= 193)
        
        if i['hgt'].endswith('in'):
            valid = valid and (59 <= int(i['hgt'][:-2]) <= 76)
        
        valid = valid and (i['hcl'][0] == '#' and len(i['hcl']) == 7 and all (c in '1234567890abcdef' for c in i['hcl'][1:]))

        valid = valid and (i['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))

        valid = valid and (len(i['pid']) == 9 and all (c in '1234567890' for c in i['pid']))
        
        count += valid
    return count