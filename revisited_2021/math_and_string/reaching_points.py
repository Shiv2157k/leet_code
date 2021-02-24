

class Points:

    def is_reaching(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        Approach: Work Backwards using modulo
        Time Complexity: O(log(max(tx, ty)))
        Space Complexity: O(1)
        :param sx:
        :param sy:
        :param tx:
        :param ty:
        :return:
        2, 5 -> 19, 12
        """
        while tx >= sx and ty >= sy:
            if tx == ty:  # cannot move any more.
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy


if __name__ == "__main__":
    points = Points()
    print(points.is_reaching(2, 5, 19, 12))
    print(points.is_reaching(2, 5, 19, 13))