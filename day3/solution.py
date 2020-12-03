from typing import Dict

def day3(input: Dict[int, Dict[int, bool]], h_slope, v_slope) -> int:
    position = (0,0)
    width = len(input[position[0]])
    count = 0

    while (position[0] + v_slope) < len(input):
        position = (position[0] + v_slope, (position[1] + h_slope) % width)
        if input[position[0]][position[1]]:
            count += 1
    
    return count

def prepare_input(input: str) -> Dict[int, Dict[int, bool]]:
    lines = input.strip().splitlines()

    output = dict()

    for i in range(0, len(lines)):
        output[i] = dict()

    for x,line in enumerate(lines):
        for y,char in enumerate(list(line)):
            if char == '#':
                output[x][y] = True
            else:
                output[x][y] = False

    return output
