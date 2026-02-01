# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 3. Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

class UniqueTracker:
    def __init__(self):
        self.items = set()

    def add(self, value):
        self.items.add(value)

    def add_list(self, value):
        for itm in value:
            self.items.add(itm)

    def get_unique_count(self):
        return len(self.items)
    
    def print_unique_items(self):
        print(self.items)
    

if __name__ == "__main__":
    test_ut = UniqueTracker()
    test_ut.add_list(["apple", "banana", "apple", "kiwi", "banana"])
    print(test_ut.print_unique_items())