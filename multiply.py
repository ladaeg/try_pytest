def multiply(iter_data):
    if len(iter_data) != 0 and len(iter_data) != 1:
        result = 1
        for value in iter_data:
            if type(value) == str:
                raise TypeError
            result *= value
        return result

print(multiply([]))