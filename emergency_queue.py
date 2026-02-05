class Patient:
    """
    Represents a patient in the emergency room.
    """
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    """
    Min-heap priority queue for emergency patients.
    """
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index],
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            self.heapify_down(smallest)

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_patient

    def print_heap(self):
        print("\nCurrent Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()

    # Edge case: peek/remove on empty heap
    print(heap.peek())       # None
    print(heap.remove_min()) # None

    # Insert patients
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()
    # Expected root: Taylor (1)

    # Peek test
    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor 1

    # Remove most urgent
    served = heap.remove_min()
    print("Served:", served.name)         # Taylor

    heap.print_heap()
    # Remaining: Jordan, Avery

    # Remove remaining patients
    heap.remove_min()
    heap.remove_min()

    # Edge case: removing from empty heap again
    print(heap.remove_min())  # None
