#personal_finance_manager
def show_details():
    print("account details")
    for k,v in details.items():
        print("name",k,"age,balance",v)
        break


def add_user():
        name=input("Enter your name: ")
        age=input("Enter your age: ")
        balance=input("Enter your balance: ")
        details[name]={"name":name,"age":age,"balance":balance}
        return name,age,balance

def add_expense(name,age,balance):
    name=input("Enter your name: ")
    expense=int(input("Enter your expense: "))
    new_balance=details[name]["balance"]+expense
    details[name]={"age":age,"balance":new_balance}
    return name,new_balance

def delete_entry():
    name=input("Enter your name: ")
    if name in details:
        confrim=input(f"are you sure you want to delete this account? {name} (y/n) ? ")
        if input.lower()=="y":
            details.pop(name)
    else:
        print("account does not exist")

def quit():
    print("bye")
    sys.exit()


details={"karan":{"age":26,"balance":45000},
        "aswin":{"age":23,"balance":50000},
         "athul":{"age":25,"balance":36000}}

import sys

print("Personal Finance Tracker")
print("main menu")
print("1.Show account details.\n 2.Add new user\n 3.Add expense \n 4.delete entry \n 5.Quit")
choice = input("Enter your choice: ")
while True:
    match choice:
        case "1":
            show_details()
            break
        case "2":
            add_user()
        case "3":
            add_expense()
        case "4":
            delete_entry()
        case "5":
            quit()
