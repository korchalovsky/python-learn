class Item:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class List:
    def __init__(self):
        self.first = None

    def print(self):
        current = self.first
        while current:
            print(current.value)
            current = current.next
        else:
            return

    def search(self, value):
        current = self.first
        while current:
            if value == current.value:
                return current.value
            else:
                current = current.next
        return print('Такого значения нет')

    def add_to_end(self, new_value):
        new_item = Item(new_value, None)
        if self.first is None:
            self.first = new_item
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = new_item

    def add_so_start(self, new_value):
        if self.first is None:
            self.first = Item(new_value, None)
            return
        self.first = Item(new_value, self.first)

    def get(self, index):
        item_index = 0
        current = self.first
        if current is not None:
            while item_index != index and current is not None:
                current = current.next
                item_index += 1
            if current:
                return print(current.value)
            else:
                return print('Такого элемента нет')
        else:
            return print('Список пуст')

    def remove(self, value):
        if self.first:
            if self.first.value == value:
                self.first = self.first.next
                return
            else:
                current = self.first
                while current.next:
                    if current.next.value == value:
                        current.next = current.next.next
                        return
                    else:
                        current = current.next

    def remove_by_index(self, value_index):
        if self.first:
            if value_index == 0:
                self.first = self.first.next
                return
            else:
                current = self.first.next
                previous_current = self.first
                item_index = 1
                while current:
                    if value_index == item_index:
                        previous_current.next = current.next
                        return
                    else:
                        previous_current = current
                        current = current.next
                        item_index += 1


