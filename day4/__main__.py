from solution import day4, prepare_input

if __name__ == "__main__":
    with open('inputs/day4.txt', 'r') as f:
        input = f.read()

        passports = prepare_input(input)
        print(day4(passports))