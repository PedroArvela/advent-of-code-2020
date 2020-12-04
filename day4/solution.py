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
