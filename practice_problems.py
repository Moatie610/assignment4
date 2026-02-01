"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    arr = [1, 2, 3, 4, 2, 5, 3]

    duplicates = set()
    seen = set()

    for item in product_ids:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    if len(duplicates)>0:
        return True
    
    return False 




"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing 
tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.items = []

    def add_task(self, task):
        self.items.append(task)

    def remove_oldest_task(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return
 the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.items = set()

    def add(self, value):
        self.items.add(value)

    def get_unique_count(self):
        return len(self.items)

if __name__ == "__main__":
    print(has_duplicates([10,20,20,30,30]))
    print(has_duplicates([10,20,30,40,50]))

    test_q = TaskQueue()
    test_q.add_task("t1")
    test_q.add_task("t2")
    test_q.add_task("t3")
    print(test_q.remove_oldest_task())

    test_ut = UniqueTracker()
    test_ut.add(10)
    test_ut.add(10)
    test_ut.add(20)
    test_ut.add(20)
    test_ut.add(10)
    test_ut.add(30)
    print(test_ut.get_unique_count())