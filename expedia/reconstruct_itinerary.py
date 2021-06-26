from typing import List
from collections import defaultdict


class FlightTickets:

    def __init__(self):
        # to keep track of origin and number of destinations
        # we can visit from the current origin
        self.flight_to_dest = defaultdict(list)
        # to keep track of visited destinations
        self.visit_map = dict()
        # total number of flights
        self.flights = 0
        # to store reconstructed itinerary in lexographic order
        self.result = []

    def reconstruct_itinerary(self, tickets: List[str]) -> List[str]:
        """
        Approach: Back tracking + Greedy
        Time Complexity: O(|E|)^d
        E - total number of flights
        Space Complexity: O(|V| + 2 * |E|)
        V - vertex or paths
        E - Edges or flights
        :param tickets:
        :return:
        """
        self.flight_to_dest = defaultdict(list)
        self.result = []
        self.visit_map = dict()

        # build the origin and number of destinations we can go from there
        for origin, destination in tickets:
            self.flight_to_dest[origin].append(destination)

        # perform back tracking on the current origin and destinations
        for origin, destinations in self.flight_to_dest.items():
            # sort the destinations in lexographically ascending order
            destinations.sort()
            # build the visit map tracker from each origin
            self.visit_map[origin] = [False] * len(destinations)

        self.flights = len(tickets)
        self.back_track("JFK", ["JFK"])
        return self.result

    def back_track(self, origin: str, route: List[str]) -> bool:

        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, next_destination in enumerate(self.flight_to_dest[origin]):

            if not self.visit_map[origin][i]:
                # mark it as visited
                self.visit_map[origin][i] = True
                ret = self.back_track(next_destination, route + [next_destination])
                self.visit_map[origin][i] = False
                if ret:
                    return True
        return False

    def reconstruct_itinerary_(self, tickets: List[str]) -> List[str]:
        """
        Approach: Hierholzer's Algorithm
        Time Complexity: O(|E| log |E / V|)
        Space Complexity: O(|V| + |E|)
        :param tickets:
        :return:
        """
        self.flight_to_dest = defaultdict(list)
        self.result = []

        for origin, destination in tickets:
            self.flight_to_dest[origin].append(destination)

        for origin, destinations in self.flight_to_dest.items():
            destinations.sort(reverse=True)

        self.dfs("JFK")
        return self.result[::-1]

    def dfs(self, origin: str) -> None:

        destinations = self.flight_to_dest[origin]

        while destinations:
            next_destination = destinations.pop()
            self.dfs(next_destination)
        self.result.append(origin)


if __name__ == "__main__":
    flight_tickets = FlightTickets()
    """
    Output:
    ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
    ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
    """
    print(flight_tickets.reconstruct_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(flight_tickets.reconstruct_itinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

    print(flight_tickets.reconstruct_itinerary_([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(flight_tickets.reconstruct_itinerary_(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
