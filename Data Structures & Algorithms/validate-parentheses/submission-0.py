class Solution:
    def isValid(self, s: str) -> bool:
        s_list = [i for i in s]
        stack = []
        while s_list:
            last = s_list.pop()
            if(len(stack) == 0):
                stack.append(last)
            else:
                top = stack[-1]
                if(last == '(' and top == ')'):
                    stack.pop()
                elif(last == '[' and top == ']'):
                    print(stack)
                    stack.pop()
                elif(last == '{' and top == '}'):
                    stack.pop()
                else:
                    stack.append(last)
        result = len(stack) == 0
        return result

        