from typing import Callable, List
import math

# DO NOT MAKE UNNECESSARY CHANGES
class DistanceFuncs:
    def calc_distance(
        self, point_a: List[float], point_b: List[float], dist_func: Callable, /
    ) -> float:
        """Calculates distance between two points using the passed dist_func"""
        return dist_func(point_a, point_b)

    @staticmethod
    def euclidean(point_a: List[float], point_b: List[float], /) -> float:
        """
        Calculates Euclidean Distance between two points Example:
        >>> DistanceFuncs.euclidean([1,1],[1,1])
        0.0
        """
        return math.dist(point_a, point_b)

    @staticmethod
    def manhattan_distance(point_a: List[float], point_b: List[float], /):
        """Compute the manhattan_distance between two points"""
        sum = 0
        for i in range(len(point_a)):
            sum += abs(point_a[i] - point_b[i])
        return sum

    @staticmethod
    def jaccard_distance(point_a: List[float], point_b: List[float], /):
        """Compute the jaccard_distance between two points"""
        dict = {}
        common = 0
        total = len(set(point_a))
        for x in set(point_a): dict[x] = 1
        for x in set(point_b): 
            if x in dict:
                common += 1
            else:
                total += 1
        return common / total

def main():
    """Demonstrate the usage of DistanceFuncs"""
    point_a = [1, 1]
    point_b = [1, 2]
    df = DistanceFuncs()
    print(df.euclidean(point_a, point_b))
    print(df.manhattan_distance(point_a, point_b))
    print(df.jaccard_distance(point_a, point_b))

if __name__ == "__main__":
    main()
