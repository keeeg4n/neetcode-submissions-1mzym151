def add_two_numbers() -> int:
    result: int = 0
    
    int_inputs = input()
    int_inputs = int_inputs.split(",")
    for values in int_inputs:
        result += int(values) 
    
    return result



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
