from collections import Counter


class EnglishWords:

    def reconstruct_to_digits(self, words: str) -> str:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param words:
        :return:
        """

        """
        unique numbers:
        zero - z
        two - w
        four - u
        six - x
        eight - g
        
        one - count[n] - seven - 2 * nine
        five - count[f] - four
        seven - count[s] - six
        three - count[h] - eight
        nine - count[i] - five - six - eight
        """

        word_counter = Counter(words)

        out = {}

        out["0"] = word_counter["z"]

        out["2"] = word_counter["w"]

        out["4"] = word_counter["u"]

        out["6"] = word_counter["x"]

        out["8"] = word_counter["g"]

        out["5"] = word_counter["f"] - out["4"]

        out["3"] = word_counter["h"] - out["8"]

        out["7"] = word_counter["s"] - out["6"]

        out["9"] = word_counter["i"] - out["8"] - out["5"] - out["6"]

        out["1"] = word_counter["n"] - out["7"] - 2 * out["9"]

        output = [key * out[key] for key in sorted(out.keys())]

        return "".join(output)


if __name__ == "__main__":

    english_words = EnglishWords()
    print(english_words.reconstruct_to_digits("nineowozonetneoerzerotwoninesix"))