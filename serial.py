"""Python serial number generator."""


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
        """Generate starting number of start"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Show representation """
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Generates the next sequential number, starting with the start number"""

        generated = self.next
        self.next += 1
        return generated

    def reset(self):
        """Resets the serial counting back to the start number"""
        self.next = self.start
        return
