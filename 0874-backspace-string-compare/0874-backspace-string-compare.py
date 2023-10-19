class Solution(object):
    def backspaceCompare(self, s, t):
        def process_string(input_str):
            result = []
            for char in input_str:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return "".join(result)

        return process_string(s) == process_string(t)
