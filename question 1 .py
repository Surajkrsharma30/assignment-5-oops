#Explanation
#use should be able to find the nth powwr of x.(i.e x*x*x*x...n times)
#you must implement it using class

#sample input
#x:10
#n:2

#sample output
#100

class power:
    def pow(self,x,n):
       print("pow(",x,",",n,")=",x**n)
p = power()
x = int(input("enter'x',value :"))
n = int(input("enter'n',value :"))
p.pow(x,n)
