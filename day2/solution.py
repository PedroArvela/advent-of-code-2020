from typing import Tuple

def password_is_valid(password_tuple: Tuple[int, int, str, str]) -> bool:
    min_repeats, max_repeats, char, password = password_tuple
    count = password.count(char)
    return count >= min_repeats and count <= max_repeats

def part_2_password_is_valid(password_tuple: Tuple[int, int, str, str]) -> bool:
    position_1, position_2, char, password = password_tuple
    return (password[position_1-1] == char) ^ (password[position_2-1] == char)
