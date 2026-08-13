from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    result_dict: Dict[str, int] = {}

    for character in word:
        if character in result_dict:
            result_dict[character] += 1
        else:
            result_dict[character] = 1
    
    return result_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
