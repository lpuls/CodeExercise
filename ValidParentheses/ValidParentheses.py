class ValidParentheses(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_dict = {'[': ']', '(': ')', '{': '}' }

        length = len(s)
        stack = list()
        for item in s:
            if '[' == item or '(' == item or '{' == item:
                stack.append(item)
            else:
                stack_length = len(stack)
                if stack_length <= 0:
                    return False
                top = stack[len(stack) - 1]
                if brackets_dict[top] != item:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


