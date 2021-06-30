class Robot:

    def is_bounded(self, instructions: str) -> bool:
        """
        Approach: One Pass
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param instructions:
        :return:
        """
        # faces north initially
        route = 0
        # starts from origin
        x = y = 0
        # north=0, east=1, south=2, west=3
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for instruction in instructions:
            if instruction == "L":  # going west
                route = (route + 3) % 4
            elif instructions == "R":  # going east
                route = (route + 1) % 4
            else:
                x += directions[route][0]
                y += directions[route][1]
        return x == y == 0 or route != 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.is_bounded("GGLLGG"))
    print(robot.is_bounded("GL"))
    print(robot.is_bounded("GG"))
