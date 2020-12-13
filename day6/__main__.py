from day6.solution import prepare_input, day6_part1, day6_part2

if __name__ == "__main__":
    with open("inputs/day6.txt", "r") as f:
        input = f.read()

        answers = prepare_input(input)
        print(day6_part1(answers))
        print(day6_part2(input))