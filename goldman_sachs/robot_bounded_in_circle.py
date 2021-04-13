class Robot:

    def is_bounded(self, instructions: str) -> bool:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param instructions:
        :return:
        """
        # starts from origin
        x = y = 0
        # initially faces north or straight
        route = 0
        # directions 0 = north, 1 = east, 2 = south, 3 = west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == "L":  # west
                route = (route + 3) % 4
            elif instructions == "R":  # east
                route = (route + 1) % 4
            else:
                x += directions[route][0]
                y += directions[route][1]
        return x == y == 0 or route != 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.is_bounded("GGLLGG"))
    print(robot.is_bounded("GG"))
    print(robot.is_bounded("GL"))
