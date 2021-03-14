from typing import List
from collections import defaultdict
import heapq


class Competitor:

    def get_top_k_competitors(self, tc: int, tnc: int, nr: int, competitors: List[str], reviews: List[str]):

        if not top_n_competitors or not top_n_competitors or not num_reviews:
            return []
        counter = dict()

        for review in reviews:
            for competitor in competitors:
                if competitor.lower() in review.lower():
                    if competitor not in counter:
                        counter[competitor] = 1
                    else:
                        counter[competitor] += 1
        heap = []
        for competitor, freq in counter.items():
            heapq.heappush(heap, (-freq, competitor))
        return [heapq.heappop(heap)[1] for _ in range(tnc)]


if __name__ == "__main__":
    total_competitors = 6
    top_n_competitors = 2
    competitors = ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"]
    num_reviews = 6
    reviews = [
        "newshop is providing good services in the city; everyone should use newshop",
        "best services by newshop",
        "fashionbeats has great services in the city",
        "I am proud to have fashionbeats",
        "mymarket has awesome services",
        "Thanks Newshop for the quick delivery"
    ]
    reviews_1 = [
        "newshop is providing good services in the city; everyone should use newshop",
        "best services by newshop",
        "shopnow has great services in the city",
        "I am proud to have shopnow",
        "mymarket has awesome services",
        "Thanks mymarket for the quick delivery"
        "Thanks afashion for the quick delivery"
    ]
    com = Competitor()
    print(com.get_top_k_competitors(
        total_competitors,
        top_n_competitors,
        num_reviews,
        competitors,
        reviews
    ))
    print(com.get_top_k_competitors(
        total_competitors,
        top_n_competitors,
        num_reviews,
        competitors,
        reviews_1
    ))
