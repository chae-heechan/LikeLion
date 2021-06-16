class Calaulator:
    
    def __init__(self): # 초기화
        self.operand1 = 0
        self.operand2 = 0
        self.operation = "+"
        self.add_count = 0
        self.sub_count = 0
        self.mul_count = 0
        self.div_count = 0

    def calculate(self): # 연산
        while(True):
            expression = input("수식을 입력하시오 : ")
            self.operand1, self.operation, self.operand2 = map(str, expression.split())
            self.operand1 = int(self.operand1)
            self.operand2 = int(self.operand2)
            
            if self.operation=="+":
                self.add()
            elif self.operation=="-":
                self.sub()
            elif self.operation=="*":
                self.mul()
            elif self.operation=="/":
                self.div()
                self.print_result()

    def add(self):
        print(f"덧셈결과 : {self.operand1 + self.operand2}")
        self.add_count += 1

    def sub(self):
        print(f"뺄셈결과 : {self.operand1 - self.operand2}")
        self.sub_count += 1

    def mul(self):
        print(f"곱셈결과 : {self.operand1 * self.operand2}")
        self.mul_count += 1

    def div(self):
        print(f"나눗셈결과 : {self.operand1 / self.operand2}")
        self.div_count += 1

    def print_result(self):
        print(f"덧셈 : {self.add_count}")
        print(f"뺄셈 : {self.sub_count}")
        print(f"곱셈 : {self.mul_count}")
        print(f"나눗셈 : {self.div_count}")
        exit()

C = Calaulator()
C.calculate()