# Class for the queue
class SongQueue:
    def __init__(self):
        self.queue = []

    # Add to the queue
    def add(self, obj):
        self.queue.append(obj)

    # Return size of queue
    def size(self):
        return len(self.queue)

    # Remove from the queue
    def remove(self, obj):
        self.queue.remove(obj)

    # Remove first item from queue
    def popFront(self):
        self.queue.remove(self.queue[0])
        
    # Get first element in queue
    def first(self):
        return self.queue[0]