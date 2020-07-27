from operator import itemgetter


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", itemgetter("name")))
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
# using a first class functions.
# result = calculate(20, 4, operator=divide)
# print(result)

# grades = [78, 99, 85, 100]
# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}")
