from solution import day3, prepare_input

if __name__ == "__main__":
    with open('inputs/day3.txt', 'r') as f:
        input = f.read()
        
        matrix = prepare_input(input)
        print(day3(matrix))
