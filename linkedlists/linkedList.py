class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data: object) -> None:
        node = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, data: object) -> None:
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return

        self.tail.next = Node(data, None)
        if self.tail:
            self.tail = self.tail.next

    def insert_values(self, data_list: list) -> None:
        for data in data_list:
            self.insert_at_beginning(data)

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= self.get_length():
            raise Exception("Inavalid index")

        if index == 0:
            if self.head:
                self.head = self.head.next
            if self.head is None:
                self.tail = None

            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next:
                    itr.next = itr.next.next
                if itr.next is None:
                    self.tail = itr

                break
            itr = itr.next
            count += 1

    def insert_at(self, index: int, data: object) -> None:
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                if itr.next is None:
                    self.tail = node

                break
            itr = itr.next
            count += 1

    def search(self, value: object) -> int:
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1

        raise ValueError("Value {value} not found in the list")

    def __str__(self) -> str:
        if self.head is None:
            return "Linked list is empty"

        itr = self.head
        ll_str = ""
        while itr:
            ll_str += str(itr.data) + " --> "
            itr = itr.next

        return ll_str + "NULL"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["Orange", "Apple"])
    print(ll)
    ll.insert_at(0, "Pineaple")
    print(ll)
    ll.remove_at(2)
    print(ll)
    try:
        print(ll.search("Apple"))

    except ValueError as e:
        print(e)
