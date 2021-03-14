from typing import List, Dict
from collections import defaultdict


class City:

    def find_nearest(self, points: List[str], x_coordinates: List[int], y_coordinates: List[int], queries: List[str],
                     n: int):

        x_to_point = defaultdict(list)
        y_to_point = defaultdict(list)
        point_to_idx = dict()

        # initialize dictionaries to store all neighbors
        for i in range(n):
            if x_coordinates[i] not in point_to_idx:
                x_to_point[x_coordinates[i]].append(points[i])
            if y_coordinates[i] not in point_to_idx:
                y_to_point[y_coordinates[i]].append(points[i])
            point_to_idx[points[i]] = i

        # list to hold result of queries
        result = [None] * len(queries)
        for i in range(len(queries)):
            q = queries[i]
            q_idx = point_to_idx[q]
            x_neighbors = x_to_point[x_coordinates[q_idx]]
            y_neighbors = y_to_point[y_coordinates[q_idx]]
            # if there are no neighbors skip
            if len(x_neighbors) == 1 and len(y_neighbors) == 1:
                continue
            min_distance = float("inf")
            minimum = ""
            # get neighbors from x coordinate and update min
            for neighbor in x_neighbors:
                # if neighbors are same skip
                if neighbor == q:
                    continue
                distance = self.get_distance(q, neighbor, point_to_idx, x_coordinates, y_coordinates)
                if distance < min_distance:
                    min_distance = distance
                    minimum = neighbor
            for neighbor in y_neighbors:
                # if neighbors are same skip
                if q == neighbor:
                    continue
                distance = self.get_distance(q, neighbor, point_to_idx, x_coordinates, y_coordinates)
                if distance < min_distance:
                    min_distance = distance
                    minimum = neighbor
            result[i] = minimum
        return result

    def get_distance(self, q: str, neighbor: str, point_to_idx: Dict[str, int], x_coo: List[int], y_coo: List[int]):
        q_idx = point_to_idx[q]
        neighbor_idx = point_to_idx[neighbor]
        return abs(x_coo[q_idx] - x_coo[neighbor_idx]) + abs(y_coo[q_idx] - y_coo[neighbor_idx])


if __name__ == "__main__":
    points = ["p1", "p2", "p3"]
    x_coordinates = [30, 20, 10]
    y_coordinates = [30, 20, 30]
    queries = ["p3", "p2", "p1"]
    n = 3
    city = City()
    print(city.find_nearest(points, x_coordinates, y_coordinates, queries, n))
    points = ["p1", "p2", "p3", "p4", "p5"]
    x_coordinates = [10, 20, 30, 40, 50]
    y_coordinates = [10, 20, 30, 40, 50]
    queries = ["p1", "p2", "p3", "p4", "p5"]
    n = 5
    print(city.find_nearest(points, x_coordinates, y_coordinates, queries, n))
    points = ["p1", "p2", "p3", "p4", "p5"]
    x_coordinates = [10, 20, 30, 30, 50]
    y_coordinates = [10, 10, 30, 40, 50]
    queries = ["p1", "p2", "p3", "p4", "p5"]
    n = 5
    print(city.find_nearest(points, x_coordinates, y_coordinates, queries, n))
