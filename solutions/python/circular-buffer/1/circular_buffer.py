class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message):
        super().__init__(message)

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message):
        super().__init__(message)

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest_index = 0

    def read(self):
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")
        return self.buffer.pop(0)

    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)  # Remove oldest
            self.buffer.append(data)  # Add new data
        else:
            self.buffer.append(data)
            self.oldest_index = (self.oldest_index + 1) % (len(self.buffer) or 1)  # Avoid division by zero

    def clear(self):
        self.buffer = []
        self.oldest_index = 0