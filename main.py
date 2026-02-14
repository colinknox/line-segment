class LineSegment:
    def __init__(self, center_x, width):
        self.center_x = center_x
        self.width = width
        self.__range = width / 2 
        self.left_edge = self.center_x - self.__range
        self.right_edge = self.center_x + self.__range

    def contains_point(self, x):
        if self.left_edge <= x <= self.right_edge:
            return True
        else:
            return False
        
    def overlaps_with(self, other):
        if self.left_edge <= other.right_edge and self.right_edge >= other.left_edge:
            return True
        else:
            return False