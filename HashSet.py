def hash_function(item, size):
    char_sum = 0
    for char in str(item):
        char_sum += ord(char)
    return char_sum % size


class HashSetItem:
    def __init__(self, value):
        self.value = value
        self.next = None


class HashSet:
    def __init__(self):
        self.size = 32
        self.slots = [None] * self.size

    def add_item(self, value):
        hash = hash_function(value, self.size)
        slot = self.slots[hash]
        if slot is None:
            self.slots[hash] = HashSetItem(value)
        else:
            if slot.value == value:
                return print("Такой элемент уже есть")
            # Обработка коллизий
            else:
                while slot.next:
                    if slot.value == value:
                        return print("Такой элемент уже есть")
                    else:
                        slot = slot.next
                slot.next = HashSetItem(value)
                return

    def remove(self, value):
        hash = hash_function(value, self.size)
        slot = self.slots[hash]
        if slot is None:
            return print("Такого элемента нет")
        else:
            if slot.value == value and slot.next is None:
                self.slots[hash] = None
                return
            elif slot.value != value and slot.next is not None:
                while slot.next:
                    if slot.next.value == value:
                        slot.next = slot.next.next
                        return
                    else:
                        slot = slot.next

    def search(self, value):
        hash = hash_function(value, self.size)
        slot = self.slots[hash]
        if slot is None:
            return print("Такого элемента нет")
        while True:
            if slot.value == value:
                return print(hash)
            else:
                if slot.next:
                    slot = slot.next
                else:
                    return print("Такого элемента нет")

    def print(self):
        result = []
        for slot in range(self.size):
            if self.slots[slot] is not None:
                if self.slots[slot].next is None:
                    result.append(self.slots[slot].value)
                else:
                    result.append(self.slots[slot].value)
                    next_item = self.slots[slot].next
                    while next_item:
                        result.append(next_item.value)
                        next_item = next_item.next
        return print(result)

    def clear(self):
        for slot in range(self.size):
            if self.slots[slot] is not None:
                self.slots[slot] = None
        return print("Множество очищено")


set = HashSet()

set.add_item("шишки")
set.add_item(7)
set.add_item("план")
set.add_item(8)
set.add_item(9)
set.add_item("norm")
set.add_item(15)
set.add_item(18)
set.add_item("Sergey")

set.add_item(15)
set.add_item("з")

set.remove("шишки")
set.remove("з")

set.print()

set.clear()

set.print()
