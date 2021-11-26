from abc import ABC, abstractmethod

class Geometry(ABC):
    @abstractmethod
    def nearest_distance(self, point):
        pass

class LineSegment(Geometry):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def nearest_distance(self, point):
        return 0.0