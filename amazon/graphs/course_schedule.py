from typing import List
from collections import defaultdict


class GNode:

    def __init__(self):
        self.out_nodes = []
        self.in_degrees = 0


class Courses(object):

    def can_finish(self, num_courses: int, pre_requisites: List[List[int]]) -> bool:
        """
        Approach: Topological Sort
        Time Complexity: O(|E| + |V|)
            - V number of courses
            - E number of dependencies
        Space Complexity: O(|E| + |V|)
            - O(|E| + 2*|V|)
        :param num_courses:
        :param pre_requisites:
        :return:
        """

        # build the graph with node data structure
        graph = defaultdict(GNode)

        # initialize total depth which helps in detecting the cycle
        total_depth = 0

        for relation in pre_requisites:
            next_course, curr_course = relation[0], relation[1]
            graph[curr_course].out_nodes.append(next_course)
            graph[next_course].in_degrees += 1
            total_depth += 1

        # find the course that has no in degree or pre requisite
        courses = []
        for index, node in graph.items():
            if node.in_degrees == 0:
                courses.append(index)

        courses_removed = 0

        while courses:
            course = courses.pop()
            for next_course in graph[course].out_nodes:
                graph[next_course].in_degrees -= 1
                courses_removed += 1

                if graph[next_course].in_degrees == 0:
                    courses.append(next_course)

        if courses_removed == total_depth:
            return True
        else:
            return False


class CourseSchedule:

    def can_finish_k_courses(self, num_course: int, pre_requisites: List[List[int]]) -> bool:
        """
        Approach: DFS (Pre-order traversal)
        Time Complexity: O(|E| + |V|)
            - V number of courses
            - E number of dependencies
        Space Complexity: O(|E| + |V|)
            - O(|E| + 2*|V|)
        :param num_course:
        :param pre_requisites:
        :return:
        """
        graph = defaultdict(list)
        # build the directed graph
        for next_course, curr_course in pre_requisites:
            graph[curr_course].append(next_course)
        path = [False] * num_course
        visited = [False] * num_course

        for curr_course in range(num_course):
            if self.is_cycle(curr_course, graph, visited, path):
                return False
        return True

    def is_cycle(self, curr_course, graph, visited, path) -> bool:
        """
        DFS traversal
        :param curr_course:
        :param graph:
        :param visited:
        :param path:
        :return:
        """
        # base cases
        if visited[curr_course]:
            return False
        if path[curr_course]:
            # detected cycle
            return True

        # add it to the path
        path[curr_course] = True

        # back tracking
        ret = False
        for next_course in graph[curr_course]:
            ret = self.is_cycle(next_course, graph, visited, path)
            if ret:
                break  # back track

        # remove from path
        path[curr_course] = False
        # add to the visited
        visited[curr_course] = True
        return ret


if __name__ == "__main__":
    course_schedule = Courses()
    print(course_schedule.can_finish(2, [[1, 0]]))
    print(course_schedule.can_finish(2, [[1, 0], [0, 1]]))

    course_scheduler = CourseSchedule()
    print(course_scheduler.can_finish_k_courses(2, [[1, 0]]))
    print(course_scheduler.can_finish_k_courses(2, [[1, 0], [0, 1]]))




