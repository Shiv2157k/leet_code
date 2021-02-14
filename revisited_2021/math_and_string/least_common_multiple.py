

class LCM:

    def get(self, n1: int, n2: int) -> int:
        """
        Find the least common multiple.
        :param n1:
        :param n2:
        :return:
        """
        if n1 > n2:
            greater = n1
        else:
            greater = n2

        while True:
            if greater % n1 == 0 and greater % n2 == 0:
                return greater
            greater += 1


if __name__ == "__main__":
    lcm = LCM()
    print(lcm.get(24, 36))