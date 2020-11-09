import consts as c

class RegularExpressionReader(object):

    def __init__(self, expr):
        self.expr = expr
        for i in self.expr:
            if i not in c.ALPHABET and i not in c.OPERATION_LIST:
                raise AttributeError("Regular expression has improper symbols")
        if expr[-1] in c.ALPHABET:
            raise AttributeError("Incorrect expression")

    def FindMinLenEqualToRemainderByMod(self, mod, remainder):
        stack = self.StackForExpr()
        for i in self.expr:
            if i in c.ALPHABET:
                letter_expr = [-1] * mod
                letter_expr[1] = 0 if i != "1" else -1
                letter_expr[0] = 0 if i == "1" else -1
                stack.push(letter_expr)
            elif i in c.OPERATION_LIST:
                if i == c.OPERATIONS.CONCATENATION.value:
                    expr1 = stack.pop()
                    expr2 = stack.pop()
                    concat = self.__ExprConcatenation(expr1, expr2)
                    stack.push(concat)
                elif i == c.OPERATIONS.SUM.value:
                    expr1 = stack.pop()
                    expr2 = stack.pop()
                    expr_sum = self.__ExprSum(expr1, expr2)
                    stack.push(expr_sum)
                elif i == c.OPERATIONS.REPEATING.value:
                    expr = stack.pop()
                    repeated_expr = self.__ExprRepeated(expr)
                    stack.push(repeated_expr)
        answer_storage = stack.top()
        if answer_storage[remainder] >= 0:
            res = answer_storage[remainder] * mod + remainder
        else:
            res = None
        return res 


    @staticmethod
    def __ExprSum(expr1, expr2):
        length = len(expr1)
        res = [0] * length
        for i in range(length):
            if expr1[i] * expr2[i] == 0:
                res[i] = 0
            elif expr1[i] * expr2[i] > 0:
                res[i] = min(expr1[i], expr2[i])
            else:
                res[i] = max(expr1[i], expr2[i])
        return res


    @staticmethod
    def __ExprConcatenation(expr1, expr2):
        length = len(expr1)
        max_value = max(expr1) + max(expr2) + 1
        res = [max_value] * length
        changed = [False] * length
        for i in range(length):
            for j in range(length):
                new_possible_value = expr1[i] + expr2[j] + (i + j) // length
                if res[(i + j) % length] >= new_possible_value and (expr1[i] >= 0 and expr2[j] >= 0):
                    res[(i + j) % length] = new_possible_value
                    changed[(i + j) % length] = True
        for i in range(length):
            if not changed[i]:
                res[i] = -1
        return res


    @staticmethod
    def __ExprRepeated(expr):
        expr[0] = 0
        res = expr.copy()
        length = len(expr)
        for cnt in range(length - 1):
            temp = RegularExpressionReader.__ExprConcatenation(res, expr)
            if temp == res:
                break
            for i in range(length):
                if temp[i] == -1:
                    temp[i] = res[i]
            res = temp
        return res

    class StackForExpr(object):
        
        def __init__(self):
            self.stack = []

        
        def pop(self):
            res = None
            if len(self.stack) != 0:
                res = self.stack[-1]
                self.stack.pop()
            return res
        

        def push(self, obj):
            self.stack.append(obj)


        def top(self):
            res = None if len(self.stack) == 0 else self.stack[-1]
            return res            
