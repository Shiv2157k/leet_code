from typing import List


class Promotion:

    def is_winner(self, promotions: List[List[str]], orders: List[str]) -> bool:
        """
        Approach: Two Pointers
        Time Complexity: O(MN)
        promotion_list = [["apple", "apple"], ["banana", "anything", "banana"]]
        order = ["orange", "apple", "apple", "banana", "orange", "banana"]
        :param promotions:
        :param orders:
        :return:
        """
        # initialize indexes to 0
        p_idx = o_idx = 0

        # 1st loop until both index reach their size
        while p_idx < len(promotions) and o_idx < len(orders):
            # put the each promotion combination into a list
            promo_combination = promotions[p_idx]
            # initialize the above combination index
            promo_idx = 0
            # loop through the promo_combination and orders to see if
            # it satisfies
            while promo_idx < len(promo_combination) and o_idx < len(orders):
                # now compare each combination with the order and also wild card anything
                if promo_combination[promo_idx] == orders[o_idx] or promo_combination[promo_idx] == "anything":
                    # increment the promo_idx
                    promo_idx += 1
                else:
                    # if not start the comparision from beginning
                    promo_idx = 0
                # move to next order
                o_idx += 1
            if promo_idx != len(promo_combination):
                return False
            # move to next promotion combinations
            p_idx += 1
        # if the promotion index is less than total promotions
        # return False
        if p_idx < len(promotions):
            return False
        return True


if __name__ == "__main__":

    promotion_list = [["apple", "apple"], ["banana", "anything", "banana"]]
    order = ["orange", "apple", "apple", "banana", "orange", "banana"]
    promotion_list_1 = [["apple", "apple"], ["banana", "anything", "banana"]]
    order_1 = ["banana", "orange", "banana", "apple", "apple"]

    promotion = Promotion()
    print(promotion.is_winner(promotion_list, order))
    print(promotion.is_winner(promotion_list_1, order_1))