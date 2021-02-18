class Robot:

    def judge_circle(self, moves: str) -> bool:
        """
        Approach: Simulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param moves:
        :return:
        """
        x_axis = y_axis = 0
        for move in moves:
            if move == "U":
                y_axis -= 1
            elif move == "D":
                y_axis += 1
            elif move == "L":
                x_axis -= 1
            elif move == "R":
                x_axis += 1
        return x_axis == y_axis == 0


if __name__ == "__main__":
    robot = Robot()
    print(robot.judge_circle("LDRRLRUULR"))
    print(robot.judge_circle("UD"))