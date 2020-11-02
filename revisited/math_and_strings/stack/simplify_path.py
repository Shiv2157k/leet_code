

class Directory:

    def get_simplified_path(self, path: str) -> str:
        """
        Approach: Using Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param strs:
        :return:
        """
        # no matter what given path is valid & needs to be shorten
        # using the delimiter "/"
        path = path.split("/")
        stack = []

        for portion in path:
            if portion == "." or not portion:
                continue
            elif portion == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(portion)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    directory = Directory()
    print(directory.get_simplified_path("/home/"))
    print(directory.get_simplified_path("/../"))
    print(directory.get_simplified_path("/home//foo/"))
    print(directory.get_simplified_path("/a/./b/../c//.//"))
    print(directory.get_simplified_path("/a/../../b/../c//.//"))
    print(directory.get_simplified_path("/a//b///c/d//././/.."))
    print(directory.get_simplified_path('.//.././'))
