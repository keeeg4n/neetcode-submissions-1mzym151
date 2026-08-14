from typing import List

def read_integers() -> List[int]:
    integer_list: List[int] = []
    
    integer_string: str = str(input())

    integer_list = integer_string.split(",")
    integer_list = [int(val) for val in integer_list ]

    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
