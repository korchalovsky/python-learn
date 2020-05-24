def hash_function(key, size):
    char_sum = 0
    for char in str(key):
        char_sum += ord(char)
    return char_sum % size


def rehash_function(last_hash, size):
    return (last_hash + 1) % size


class HashMap:
    def __init__(self):
        self.size = 32
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def add_item(self, key, value):
        hash = hash_function(key, self.size)
        if self.keys[hash] is None:
            self.keys[hash] = key
            self.values[hash] = value
        else:
            if self.keys[hash] == key:
                self.values[hash] = value
            else:
                # решение коллизии
                rehash = rehash_function(hash, self.size)
                while self.keys[rehash] is not None and self.keys[rehash] != key:
                    rehash = rehash_function(rehash, self.size)
                if self.keys[rehash] is None:
                    self.keys[rehash] = key
                    self.values[rehash] = value
                else:
                    self.values[rehash] = value

    def __setitem__(self, key, value):
        self.add_item(key, value)

    def get(self, key):
        hash = hash_function(key, self.size)
        if self.keys[hash] == key:
            return self.values[hash]
        else:
            rehash = rehash_function(hash, self.size)
            while self.keys[rehash] != key:
                rehash = rehash_function(rehash, self.size)
                if rehash == hash:
                    return "Такого ключа нет в словаре"
            return self.values[rehash]

    def __getitem__(self, key):
        return self.get(key)

    def get_keys(self):
        result = []
        for i in range(self.size):
            if self.keys[i] is not None:
                result.append(self.keys[i])
        return result

    def get_values(self):
        result = []
        for i in range(self.size):
            if self.values[i] is not None:
                result.append(self.values[i])
        return result

    def print(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(self.keys[i], ":", self.values[i])


table = HashMap()

table.add_item("A", 1)
table.add_item("B", 2)
table.add_item("C", 3)
table.add_item("D", 4)
table.add_item("E", 5)
table.add_item("20", "B")
table.add_item("шишки", 890)
table.add_item("план", "342")
table.add_item("norm", 324.23)
table.add_item("Sergey", "Это я")
table.add_item("636", 32)
table.add_item("744", "Алло")
table["Кек"] = 567

table.print()

print(table["744"], '- Значение по ключу')
print(table[342], '- Значение по ключу')
print(hash_function("636", 32), "- это коллизия")
print(hash_function("744", 32), "- это коллизия")

print(table.get_keys(), "-Список ключей")
print(table.get_values(), "-Список значений")
