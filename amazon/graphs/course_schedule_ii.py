from typing import List
from collections import defaultdict, deque


class GNode:

    def __init__(self):
        self.out_nodes = []
        self.in_degrees = 0


class CourseSchedule(object):

    def find_order(self, num_courses: int, pre_requisites: List[List[int]]) -> List[int]:
        """
        Approach: Topological Sort
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        :param num_courses:
        :param pre_requisites:
        :return:
        """

        graph = defaultdict(GNode)
        for index in range(len(pre_requisites)):
            graph[pre_requisites[index][1]].out_nodes.append(pre_requisites[index][0])
            graph[pre_requisites[index][0]].in_degrees += 1

        no_pre_requisite_courses = deque()
        course_order = []

        for course in range(num_courses):
            if course not in graph or graph[course].in_degrees == 0:
                no_pre_requisite_courses.append(course)

        while no_pre_requisite_courses:
            course = no_pre_requisite_courses.popleft()
            course_order.append(course)
            for next_course in graph[course].out_nodes:
                graph[next_course].in_degrees -= 1

                if graph[next_course].in_degrees == 0:
                    no_pre_requisite_courses.append(next_course)
        return course_order if len(course_order) == num_courses else []


if __name__ == "__main__":
    course_schedule = CourseSchedule()
    print(course_schedule.find_order(2, [[1, 0]]))
    print(course_schedule.find_order(2, [[1, 0], [0, 1]]))
    print(course_schedule.find_order(2, []))
    print(course_schedule.find_order(3, [[0, 1]]))
    print(course_schedule.find_order(3, []))