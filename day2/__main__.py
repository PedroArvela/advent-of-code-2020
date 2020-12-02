import re
from solution import password_is_valid, part_2_password_is_valid

def main():
    pass

if __name__ == "__main__":
    with open('inputs/day2.txt', 'r') as f:
        lines = f.read().splitlines()
        
        unparsed_passwords = [tuple(re.split(': | |-', line)) for line in lines]

        passwords = [(int(min_r), int(max_r), char, password) for min_r, max_r, char, password in unparsed_passwords]

        valid_passwords = [password for password in passwords if password_is_valid(password)]
        valid_passwords_part2 = [password for password in passwords if part_2_password_is_valid(password)]

        print(len(valid_passwords), len(valid_passwords_part2))


