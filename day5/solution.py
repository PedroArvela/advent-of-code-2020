from typing import List, Tuple

def _get_row_and_column(boarding_pass: str) -> Tuple[int, int]:
    min_row = 0
    max_row = 127
    row_range = 127

    min_col = 0
    max_col = 7
    col_range = 7

    for c in boarding_pass[0:7]:
        row_range = row_range // 2
        if c == "F":
            max_row = min_row + row_range
        elif c == "B":
            min_row = min_row + row_range + 1

    for c in boarding_pass[7:10]:
        col_range = col_range // 2

        if c == "L":
            max_col = min_col + col_range
        elif c == "R":
            min_col = min_col + col_range + 1

    return (min_row, min_col)

def _get_seat_id(row_and_col: Tuple[int, int]) -> int:
    return (row_and_col[0] * 8) + row_and_col[1]

def day5_part1(boarding_passes: List[str]) -> int:
    seat_ids = [_get_seat_id(_get_row_and_column(p)) for p in boarding_passes]
    return max(seat_ids)

def day5_part2(boarding_passes: List[str]) -> List[int]:
    seat_ids = [_get_seat_id(_get_row_and_column(p)) for p in boarding_passes]
    sorted_seats = sorted(seat_ids)
    missing_seats = []

    for i,seat in enumerate(sorted_seats[:-1]):
        if sorted_seats[i+1] != (seat + 1):
            missing_seats.append(seat + 1)

    return missing_seats