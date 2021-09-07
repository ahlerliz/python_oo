class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Setting the starter number """
        self.original_start = self.start = start
        # self.start = start

    def generate(self):
        """ Returns the start number + 1 every time it's called"""
        self.start += 1
        return self.start-1

    def reset(self):
        """Reset self.start to original start number"""

        self.start = self.original_start
    
# Opportunity to do the -1 in generate

