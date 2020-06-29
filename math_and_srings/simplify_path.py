class Path:

    def get_simplified(self, path: str) -> str:
        """
        Approach: Using stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param path:
        :return:
        """
        if not path:
            return path
        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    paths = Path()
    print(paths.get_simplified("/../"))
    print(paths.get_simplified("/home/"))
    print(paths.get_simplified("/a/./b/../../c/"))
    print(paths.get_simplified("/a//b////c/d//././/.."))
