#Greatest Common Divisor
t=0
gcd=0
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
x=a
y=b
while b!=0:
    t=b
    b=a%b
    a=t
gcd=a
print("The GCD of",x,"and",y,"is:",gcd)


#Reverse a string by input from user
def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=str(input("Enter the string:"))
print("The original string is:",s)
print("The reversed string is:",reverse(s))


#Even or Odd
n=(101,45,24,27,97,5,3,61,46)
codd=0
ceven=0
for i in n:
        if not i%2:
            ceven=ceven+1
        else:
            codd=codd+1
print("Number of even numbers :",ceven)
print("Number of odd numbers :",codd)


#Numbers from 0-6 except 3 and 6
n=(0,1,2,3,4,5,6)
print(0)
for i in n:
    if i%3!=0:
        print(i)