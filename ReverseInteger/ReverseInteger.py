class ReverseInteger(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not self.is_in_range(x):
            return 0

        is_less_zero = False
        if x < 0:
            is_less_zero = True
            x = abs(x)

        list_result = list(str(x))
        self.remove_zero(list_result)
        list_result.reverse()
        self.remove_zero(list_result)

        if len(list_result) <= 0:
            return 0

        result = int(list_result[0])
        for i in range(1, len(list_result)):
            result = result * 10 + int(list_result[i])
        if is_less_zero:
            result = -result

        if not self.is_in_range(result):
            return 0

        return result

    def remove_zero(self, input_list):
        del_list = []
        length = len(input_list)
        for i in range(0, length):
            if i < 0 or i >= len(input_list):
                break
            temp = input_list[i]
            if temp <= '0' or temp > '9':
                del_list.append(temp)
            else:
                break
        for item in del_list:
            input_list.remove(item)

    def is_in_range(self, x):
        return 2147483647 >= x and x >= -2147483648
