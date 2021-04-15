class Robot:

    def returned_to_origin(self, moves: str) -> bool:
        """
        Approach: Simulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param moves:
        :return:
        """
        # initializing x and y axis to origin
        x = y = 0

        for move in moves:
            if move == "U":
                y += 1
            elif move == "R":
                x += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
        return x == y == 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.returned_to_origin("UD"))
    print(robot.returned_to_origin("LL"))
    print(robot.returned_to_origin("RRDD"))
    print(robot.returned_to_origin("LDRRLRUULR"))