class Date:

    def formatter(self, d: str) -> str:
        """
        Approach: String formatter
        :param d:
        :return:
        """

        day, month, year = d.split(" ")
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        return "{}-{:02}-{:>02}".format(year, months.index(month) + 1, day[:-2])


if __name__ == "__main__":
    date = Date()
    print(date.formatter("20th Oct 2052"))
    print(date.formatter("1st Jun 2025"))
    print(date.formatter("19th Jul 2021"))