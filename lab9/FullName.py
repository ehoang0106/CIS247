class FullName:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return str(self.first) + " " + str(self.last)
    
    def __gt__(self, other):
        if self.last > other.last:
            return True
        elif self.last == other.last and self.first > other.first:
            return True
        else:
            return False

        