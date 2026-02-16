class Demo:
    No = 10

    def __init__(self, A, B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):  # No Decorator
        print("Inside instance method fun : ", self.Value1, self.Value2)

    @classmethod   # Compulsory Decorator
    def sun(cls):
        print("Inside class method sun :", cls.No)

    @staticmethod  # optional decorator
    def gun():
        print("Inside static method gun :", Demo.No)

Demo.sun()
print("Class variable No :", Demo.No)

obj = Demo(11, 21)

obj.fun()
print("Instance Variable :", obj.Value1, obj.Value2)

Demo.gun()