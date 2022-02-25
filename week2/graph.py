from collections import defaultdict
from pprint import pprint

from tree.tree import Tree, csv_parser


class Graphs(Tree):

    _distance = 0

    def __init__(self, csv_list: list):
        super().__init__(csv_list)
        
        self.graph = defaultdict(dict)
        
        for i in range(len(csv_list) + 1):
            info = self.find_node_by_id(str(i))
            self.graph[str(i)] = info
        
        
    def show_graph(self):
        pprint(dict(self.graph))


    def __find_distance(self, from_node: str, to_node: str) -> None:
        if from_node > to_node:
            from_node, to_node = to_node, from_node
        first_node = self.graph[from_node]
        second_node = self.graph[to_node]
        if first_node == second_node:
            return 0
        
        if first_node['ID'] == second_node['Parent_ID']:
            Graphs._distance += 1
        else:
            Graphs._distance += 1
            self.__find_distance(from_node, second_node['Parent_ID'])


    def get_distance(self, from_node: str, to_node: str) -> int:
        self.__find_distance(from_node, to_node)
        self.distance = Graphs._distance
        Graphs._distance = 0
        return self.distance


if __name__ == '__main__':
    csv_list = csv_parser('tree/tree2.csv')
    t = Graphs(csv_list)
    # t.show_tree()
    # t.show_graph()
    print(t.get_distance('1', '6'))
