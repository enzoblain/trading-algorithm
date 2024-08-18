def get_fibonacci(begin, end):
    fibonacci = {
        '0': '', 
        '50': '', 
        '61.8': '', 
        '70.5': '', 
        '100': ''}

    difference = end - begin

    for key in fibonacci.keys():
        fibonacci[key] = round(end - (float(key) * difference / 100), 5)
    
    return fibonacci

print(get_fibonacci(0, 20))
print(get_fibonacci(20, 0))