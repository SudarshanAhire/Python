class Arithematic:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
        print("Object gets created succesfullly")

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Subtraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

obj1 = Arithematic(11, 10) # Arithematic(id(obj1), 11, 10) -> __init__(obj1, 11, 10)
obj2 = Arithematic(21, 20) # Arithematic(id(obj2), 21, 20) -> __init__(obj2, 21, 20)

Ret = obj1.Addition()
print(Ret) # 21

Ret = obj2.Subtraction()
print(Ret) # 1


