class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0

    # def insert(self, index, element):


    def pop(self, index=None):
        if self._length == 0:
            raise IndexError('pop from empty list')

        if index is None:
            index = self._length - 1

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        current = self._head
        for _ in range(index):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        if current == self._head:
            self._head = current.next
        if current == self._tail:
            self._tail = current.prev

        self._length -= 1
        return current.value

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    # Обход списка
    for element in my_list:
        print(element)

    my_list.clear()
    print("После очистки:", my_list)

    my_list.pop()
    print("После удаления последнего элемента:", my_list)

    my_list.pop(0)
    print("После удаления элемента с индекса 0:", my_list)


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()