class MergeTwoSortedLists(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_index = 0
        first_length = len(l1)
        scend_index = 0
        scend_length = len(l2)
        result_list = list()

        while first_index < first_length and scend_index < scend_length:
            first = l1[first_index]
            scend = l2[scend_index]
            if first < scend:
                result_list.append(first)
                first_index += 1
            else:
                result_list.append(scend)
                scend_index += 1

        for i in range(first_index, first_length):
            result_list.append(l1[i])
        for i in range(scend_index, scend_length):
            result_list.append(l2[i])
        return result_list
