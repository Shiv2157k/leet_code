

class Robot:

    def is_bounded(self, instructions: str) -> bool:
        """
        G - Go Straight
        L - Left 90 degrees (West)
        R - Right 90 degrees (East)
        Approach:
        Time Complexity:
        Space Complexity:
        :param instructions:
        :return:
        """

        # starts from origin and faces north
        route = 0
        x = y = 0

        # directions 0 = North, 1 = East, 2 = South, 3 = West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == "L":
                route = (route + 3) % 4
            elif instruction == "R":
                route = (route + 1) % 4
            else:
                x += directions[route][0]
                y += directions[route][1]
        return x == y == 0 or route != 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.is_bounded("GGRLGR"))
    print(robot.is_bounded("GGLLGG"))
    print(robot.is_bounded("GG"))
