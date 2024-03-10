import random
def randomArray(len, min_value, max_value):
    arr = []
    for i in range(len):
        arr[i] = random.randint(min_value, max_value);
