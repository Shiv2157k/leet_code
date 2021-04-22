

class ReachingPoints:

    def reached(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        Approach: Modulo
        Time Complexity: O(log(max(tx, ty)))
        Space Complexity: O(1)
        :param sx:
        :param sy:
        :param tx:
        :param ty:
        :return:
        """

        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else: # ty > tx
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy


if __name__ == "__main__":

    reaching_points = ReachingPoints()
    print(reaching_points.reached(2, 5, 19, 12))
    print(reaching_points.reached(3, 3, 21, 9))
    print(reaching_points.reached(2, 3, 2, 11))