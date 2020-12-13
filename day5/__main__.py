from day5.solution import day5_part1, day5_part2

if __name__ == "__main__":
    with open("inputs/day5.txt", "r") as f:
        input = f.readlines()

        print(day5_part2(input))