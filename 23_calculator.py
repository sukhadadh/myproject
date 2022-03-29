class calc:
    def __init__(self,n):
        self.n = n
        print(f'square of a given number ={self.n **2}')
        print(f'cube of a given number = {self.n **3}')
        print(f'squareroot of a given number ={self.n **0.5}')
        i=1
        for i in range(1,11):
            print(f"{n}x{i}={n*i}")

    @staticmethod
    def greet():
        print("wlcome to the calculator!")
    
    
#num1 = calc(num)
num = int(input("enter a number:"))
num1 = calc(num)

num1.greet()



        