class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        m = {'+', '-', '*', '/'}
        for t in tokens:
            if t in m:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.RPN(t, b, a))
            else:
                stack.append(t)
        print(stack)
        return int(stack[0])
    
    def RPN(self, op, b, a):
        b, a = int(b), int(a)
        if op=='+':
            return b+a
        elif op == '-':
            return b-a
        elif op == '*':
            return b*a
        else:
            return b/a