#Area of triangle
base=10
height=5
area=0.5*(base*height)
print(area)

# if statement
# 1
n=int(input("enter the number:"))
if n%2==0:
      print("Even")
else:
      print("Odd")

indian=["vada","idli","dosa"]
chinese=["noodles","fried rice"]
italian=["pizza","pasta"]

dish=input("enter your favorite dish:")
if dish in indian:
    print("your favorite dish is indian")
elif dish in italian:
    print("your favorite dish is italian")
elif dish in chinese:
    print("your favorite dish is chinese")
else:
    print("your favorite dish is not on the list")

#for loop
l1=[2022,2089,2918,2315]
total=0
for i in l1:
    total=total+i
print(total)

#using range
l1=[2022,2089,2918,2315]
total=0
for i in range(len(l1)):
    total=total+l1[i]
    print("month",(i+1),"expense is:",(l1[i]))
print("total expense is",total)

#break
key="chair"
furniture=["desk","bench","wardrobe","chair","sofa"]
for i in furniture:
    if key==i:
        print("key is part of the furniture")
        break
    else:
        print("it is not part of the furniture")

#continue
for i in range(1,11):
    if i%2==0:
        continue
    else:
        print("squares of odd numbers are:",i*i)

#while
i=1
while i<=10:
    print(i)
    i+=1

#function
def exp_caluclator(exp):
    sum=0
    for i in exp:
        sum=sum+i
    return sum

a_exp=[243,567,642]
exp_caluclator(a_exp)

#keyword argument
def sum(a,b):
    return a+b

n=sum(b=5,a=6)
print(n)

#global and local variable
total=0
def sum(a,b):
    global total
    total=a+b
    return total

n=sum(54,46)
print(total)

#default argument
def sum(a,b=98):
    return a+b

n=sum(5)
print(n)

#documentation
def sum(a,b=98):
    """

    :param a:
    :param b:
    :return:
    """
    return a+b

n=sum(5)
print(n)

