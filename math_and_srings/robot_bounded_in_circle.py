class Robot:

    def is_bounded_in_circle(self, instructions: str) -> bool:
        """
        Approach:
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param instructions:
        :return:
        """
        # north, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # origin
        x = y = 0
        # set to north
        route = 0

        for i in instructions:
            if i == "L":  # west
                route = (route + 3) % 4
            elif i == "R":  # east
                route = (route + 1) % 4
            else:
                x += directions[route][0]
                y += directions[route][1]
        return x == y == 0 or route != 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.is_bounded_in_circle("GGRL"))
    print(robot.is_bounded_in_circle("GR"))
    print(robot.is_bounded_in_circle("GGLLGG"))
