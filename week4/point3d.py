from dataclasses import dataclass
from typing import Union


@dataclass
class PointCoords:
    x: Union[int, float]
    y: Union[int, float]
    z: Union[int, float]


class Point3D:
    def __init__(self, point_coordinates: PointCoords):
        self.x = point_coordinates.x
        self.y = point_coordinates.y
        self.z = point_coordinates.z


    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


    def git_distance(self, second_point: 'Point3D') -> float:
        return (
            (second_point.x - self.x) ** 2 +
            (second_point.y - self.y) ** 2 +
            (second_point.z - self.z) ** 2
        ) ** 0.5


if __name__ == '__main__':
    first_point_coords = PointCoords(1.1, 2.5, 1.2)
    second_point_coords = PointCoords(3.3, 2, 0.7)
    first_point = Point3D(first_point_coords)
    second_point = Point3D(second_point_coords)
    distance = first_point.git_distance(second_point)
    print(distance)
