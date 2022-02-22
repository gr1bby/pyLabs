import csv

from collections import defaultdict


class Tree:
    def __init__(self, csv_list: list):
        self.tree = defaultdict(Tree)
        sorted_csv = sorted(csv_list)
        addition_list = list()
        prev_id = None
        for parent_id, children_id in sorted_csv:
            if parent_id != prev_id:
                if addition_list: 
                    self.tree[prev_id] = addition_list
                prev_id = parent_id
                addition_list = [children_id]
            else:
                addition_list.append(children_id)
        
        self.tree[prev_id] = addition_list

    def show_tree(self) -> None:
        print(dict(self.tree))

    def find_node_by_id(self, id: str) -> int:
        parent_id, children_id = None, []
        for key, value in self.tree.items():
            if id in value:
                parent_id = key

        if id in self.tree.keys():
            children_id = self.tree[id]

        if parent_id:
            print(f"Node ID is {id},\nParent ID is {parent_id},\nChildren ID is {children_id}")
            return int(id)
        elif id == '0':
            print(f"Node ID is {id},\nIt is head node,\nChildren ID is {children_id}")
            return int(id)
        else:
            print("Node isn't found")
            return None


def csv_parser(file_path: str) -> list:
    list_of_id = list()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                list_of_id.append(row)                
            line_count += 1

    return list_of_id


if __name__ == '__main__':
    tree = Tree(csv_parser('tree2.csv'))
    tree.show_tree()
    tree.find_node_by_id('1')
    