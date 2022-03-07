from typing import Union


class Point3D:
    def __init__(self, x: Union[int, float], y: Union[int, float], z: Union[int, float]):
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


    def git_distance(self, second_point) -> float:
        return (
            (second_point.x - self.x) ** 2 +
            (second_point.y - self.y) ** 2 +
            (second_point.z - self.z) ** 2
        ) ** 0.5


if __name__ == '__main__':
    first_point = Point3D(1.1, 2.5, 1.2)
    second_point = Point3D(3.3, 2, 0.7)
    distance = first_point.git_distance(second_point)
    print(distance)
