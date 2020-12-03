from solution import day3, prepare_input

if __name__ == "__main__":
    with open('inputs/day3.txt', 'r') as f:
        input = f.read()
        
        matrix = prepare_input(input)
        result1_1 = day3(matrix, 1, 1)
        result3_1 = day3(matrix, 3, 1)
        result5_1 = day3(matrix, 5, 1)
        result7_1 = day3(matrix, 7, 1)
        result1_2 = day3(matrix, 1, 2)

        print(result1_1 * result3_1 * result5_1 * result7_1 * result1_2)
