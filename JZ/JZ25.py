# _*_coding:utf-8_*_

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if None is pHead:
            return None

        temp = dict()
        node = pHead
        
        new_list = None
        new_list_node = None

        while None is not node:
            if None is new_list_node:
                new_list = RandomListNode(node.label)
                new_list_node = new_list
            else:
                new_node = RandomListNode(node.label)
                new_list_node.next = new_node
                new_list_node = new_list_node.next

            temp[node] = node.random
            node = node.next


        node = pHead
        new_list_node = new_list
        while None is not node:
            new_list_node.random = temp[node]
            new_list_node = new_list_node.next
            node = node.next
        
        return new_list


def spawn(node_value, node_random):
    if len(node_value) <= 0:
        return None

    result = list()
    for item in node_value:
        result.append(RandomListNode(item))
    
    for index, item in enumerate(node_random):
        if item >= 0:
            result[index].random = result[item]

    for index, item in enumerate(result):
        if index + 1 >= len(result):
            item.next = None
        else:
            item.next = result[index + 1]

    return result[0]


def show(list_node):
    head = list_node
    while head:
        print(head.label, end='\t')
        head = head.next
    print('')

s = Solution()
    
case = [
    spawn([1, 2, 3, 4, 5], [2, 4, 1, 3, 0]),
    spawn([1, 2, 3, 4, 5], [2, 4, 1, 3, -1]),
    spawn([1, 2, 3, 4, 5], [-1, -1, -1, -1, -1])
]

for item in case:
    result = s.Clone(item)
    print(item, result)
    show(item)
    show(result)
    print('')
