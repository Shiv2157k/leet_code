from typing import List
from collections import defaultdict


class TransactionLogs:

    def get_fraud_ids(self, log_data: List[List[str]], threshold: int) -> List[str]:
        result = []
        dictionary = defaultdict(int)
        for each_row in log_data:
            row = "".join(each_row)
            temp = row.split()

            if temp[0] != temp[1]:
                dictionary[temp[1]] += 1
            dictionary[temp[0]] += 1
        for key, value in dictionary.items():
            if value >= threshold:
                result.append(key)
        result.sort(key=int, reverse=True)
        return result


if __name__ == "__main__":
    threshold = int(input())
    log_data_num = int(input())
    log_data = [[x for x in input()] for _ in range(log_data_num)]
    transaction_logs = TransactionLogs()
    print(transaction_logs.get_fraud_ids(log_data, threshold))

    print(transaction_logs.get_fraud_ids([["345366 89921 45"],
                                          ["38239 345366 15"],
                                          ["1111 23233 12"],
                                          ["029323 38239 1"],
                                          ["029323 38239 1"],
                                          ["1111 2233 12"],
                                          ["345366 38239 23"],
                                          ["029323 345366 2"],
                                          ["1111 23231 12"],
                                          ["38239 38239 23"]], 3))
