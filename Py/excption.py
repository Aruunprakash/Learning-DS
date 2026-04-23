a=int(input("enter your first number:"))
b=input("enter your second number:")
try:
    c=a/b
except Exception as e:
    print("exception occurred", e)
    c=None

except Exception as e:
    print("exception occurred", type(e))
    c=None
print("division is :",c)
