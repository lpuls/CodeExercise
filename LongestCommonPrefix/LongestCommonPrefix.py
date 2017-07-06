class LongestCommonPrefix(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length <= 0:
            return ""

        prefix = strs[0]
        prefix_length = len(prefix)
        for i in range(0, length):
            current = strs[i]
            current_length = len(current)
            # 前缀比当前词汇大，找出当前词汇和前缀相同的部份
            if prefix_length > current_length:
                prefix = self.getPrefix(prefix, prefix_length, current, current_length)
                prefix_length = len(prefix)
            else:  # 找出当前词词是否存在该前缀
                if current[0: len(prefix)] != prefix:
                    prefix = self.getPrefix(current, current_length, prefix, prefix_length)
                    prefix_length = len(prefix)
        return prefix        

    def getPrefix(self, prefix, prefix_length, current, current_length):
        temp = ""
        for j in range(0, current_length):
            if prefix[j] != current[j]:
                break
            temp += current[j]
        return temp



