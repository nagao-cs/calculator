import re

class Parser():
    _tokens: list
    _stack: list
    _output: list
    _current_index: int
    
    symbols = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    
    def __init__(self, expr):
        self._tokens = re.findall(r'\d+|[()+\-*/]', expr)
        self._current_index = 0
        self._stack = list()
        self._output = list()
        
        print("tokens", self._tokens)
        
        
    def parse(self, expr):
        """
        式を逆ポーランド気泡に変換する
        """
        for token in self._tokens:
            if token == '(':
                self._stack.append(token)
            elif token == ')':
                if token in self._stack:
                    raise ValueError("Invalid expression")
                
                while True:
                    top = self._stack.pop()
                    if top == '(':
                        break
                    self._output.append(top)
            
            elif token in Parser.symbols.keys():
                if self._stack and self._stack[-1] in Parser.symbols.keys() and Parser.symbols[token] <= Parser.symbols[self._stack[-1]]:
                    # print(self._stack[-1], token)
                    symbol = self._stack.pop()
                    self._output.append(symbol)
                    self._stack.append(token)
                else:
                    self._stack.append(token)
            else:
                self._output.append(token)
            # print(self._output, self._stack)
        
        while self._stack:
            self._output.append(self._stack.pop())
        print("BNF:", self._output)
        # return self._output
    
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
        
        print("Result:", BNF[0])
        return BNF[0]


#test
if __name__ == "__main__":
    expr = "3 + 5 * ( 2 - 8 )" 
    parser = Parser(expr)
    parser.parse(expr)
    result = parser.evaluate(parser._output)