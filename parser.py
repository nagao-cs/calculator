class Parser():
    _tokens: list
    _stack: list
    _queue: list
    _current_index: int
    
    symbols = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    
    def __init__(self, expr):
        self._tokens = expr.split()
        self._current_index = 0
        self._stack = list()
        self._queue = list()
        
        self.parse(expr)
        self.evaluate(self._queue)
        
    def parse(self, expr):
        for token in self._tokens:
            if token == '(':
                self._stack.append(token)
            elif token == ')':
                for i in range(len(self._stack)-1, -1, -1):
                    if self._stack[i] == '(':
                        self._stack.pop(i)
                        break
                    else:
                        self._queue.append(self._stack.pop())
            elif token in self.symbols.keys():
                while len(self._stack) > 0 and self._stack[-1] != '(' and self.symbols[token] <= self.symbols[self._stack[-1]]:
                    self._queue.append(self._stack.pop())
                self._stack.append(token)
            else:
                self._queue.append(token)
        
        while len(self._stack) > 0:
            self._queue.append(self._stack.pop())
        
        return self._queue
    
    def evaluate(self, BNF):
        """
        先頭から見ていって、記号だったらスタックから2つ取り出してそれらを計算した後出力スタックへ。
        """
        cnt = 0
        while len(BNF) != 1:
            if BNF[cnt] in Parser.symbols.keys():
                targetIndex = cnt-2
                symbol = BNF.pop(cnt)
                num1 = BNF.pop(targetIndex)
                num2 = BNF.pop(targetIndex)
                if symbol == '+':
                    res = int(num1) + int(num2)
                elif symbol == '-':
                    res = int(num1) - int(num2)
                elif symbol == '*':
                    res = int(num1) * int(num2)
                elif symbol == '/':
                    res = int(num1) / int(num2)
                else:
                    raise ValueError("Invalid operator")
                BNF.insert(targetIndex, res)
                cnt = targetIndex+1
            else:
                cnt += 1
        
        return BNF[0]


#test
if __name__ == "__main__":
    expr = "3 + 5 * ( 2 - 8 )"
    parser = Parser(expr)
    print(parser._queue)  # Output the postfix notation
    print(parser.evaluate(parser._queue))  # Output the result of the expression