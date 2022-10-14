from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for t in tickets:
            tickets_dict[t[0]].append(t[1])
        path = ["JFK"]

        def backtracking(start_point):
            if len(path) == len(tickets) + 1:
                return True
            tickets_dict[start_point].sort()
            to_list = tickets_dict[start_point]
            for _ in to_list:
                end_point = to_list.pop(0)
                path.append(end_point)
                if backtracking(end_point):
                    return True
                path.pop()
                to_list.append(end_point)

        backtracking("JFK")
        return path


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
