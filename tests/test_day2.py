from day2 import password_is_valid, part_2_password_is_valid

def test_valid_1():
    password = (1, 3, 'a', 'abcde')
    assert password_is_valid(password) == True

def test_valid_2():
    password = (2, 9, 'c', 'ccccccccc')
    assert password_is_valid(password) == True

def test_invalid():
    password = (1, 3, 'b', 'cdefg')
    assert password_is_valid(password) == False

def test_part_2_password_is_valid():
    password = (1, 3, 'a', 'abcde')
    assert part_2_password_is_valid(password) == True

def test_part_2_password_is_invalid_1():
    password = (1, 3, 'b', 'cdefg')
    assert part_2_password_is_valid(password) == False

def test_part_2_password_is_invalid_2():
    password = (2, 9, 'c', 'ccccccccc')
    assert part_2_password_is_valid(password) == False
