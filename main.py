class LineSegment:
    def __init__(self, center_x, width):
        self.center_x = center_x
        self.width = width
        self.left_edge = self.center_x - self.width
        self.right_edge = self.center_x + self.width



line_one = LineSegment(5, 3)

print(f"DEBUG: center x = {line_one.center_x}")
print(f"DEBUG: width = {line_one.width}")
print(f"DEBUG: left edge = {line_one.left_edge}")
print(f"DEBUG: right edge = {line_one.right_edge}")
