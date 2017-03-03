import numpy as np
import scipy


class Calculate:

    name="cal"

    def __init__(self,name):
        self.name=name

    def add(self,a,b):
        return (a+b)

    def minus(self,a,b):
        return(a-b)

    def multiple(self,a,b):
        return(a*b)

    def divide(self,a,b):
        return(a/b)

cal=Calculate("cal2");
print(cal.name)
print(cal.add(1,2))


class Advanced_Calculate(Calculate):

    def power(self,a,b):
        return(a**b)

    def __del__(self):
        return None


A_cal=Advanced_Calculate("A_cal")
add1=A_cal.add(10,20)
power1=A_cal.power(10,2)
print(add1,power1)
A_cal.__del__()

