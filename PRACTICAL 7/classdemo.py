class demo:
    
    def __init__(self,a):
        print("This is class demo.")
        self.a=a
        print("value of a is: ",self.a)
    def __del__(self):
        print("this is descructor")
d=demo(10)