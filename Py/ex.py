#Area of triangle
base=10
height=5
area=0.5*(base*height)
print(area)

#if statement
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

