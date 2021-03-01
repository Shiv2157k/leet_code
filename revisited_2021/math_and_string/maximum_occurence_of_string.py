

class String:

    def max_occurence(self, s: str) -> str:

        count = [0] * 256
        maxx = -1
        char = ""
        for i in s:
            count[ord(i)] += 1
        for i in s:
            if maxx < count[ord(i)]:
                maxx = count[ord(i)]
                char = i
        return char


if __name__ == "__main__":
    string = String()
    print(string.max_occurence("aaab"))