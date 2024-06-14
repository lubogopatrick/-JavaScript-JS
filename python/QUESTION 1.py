class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        """
        Add a student to the end of the queue.
        """
        self.queue.append(student)

    def dequeue(self):
        """
        Remove and return the student at the front of the queue.
        """
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the current size of the queue.
        """
        return len(self.queue)

# Example usage
if __name__ == "__main__":
    student_queue = StudentQueue()

    # Students join the queue
    student_queue.enqueue("IAN")
    student_queue.enqueue("OPI")
    student_queue.enqueue("MESSI")

    # Serve students
    print(f"Serving: {student_queue.dequeue()}")
    print(f"Serving: {student_queue.dequeue()}")

    # Check queue size
    print(f"Queue size: {student_queue.size()}")

    # Serve remaining students
    print(f"Serving: {student_queue.dequeue()}")
    print(f"Serving: {student_queue.dequeue()}")

    # Check if queue is empty
    print(f"Is queue empty? {student_queue.is_empty()}")
