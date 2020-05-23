def hash(item, size):
    char_sum = 0
    for char in item:
        char_sum += ord(char)
    return char_sum % size


class HashMap:
    def __init__(self):
        self.size = 32
        self.keys = [None] * self.size
        self.values = [None] * self.size
