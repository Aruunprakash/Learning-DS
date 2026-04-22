#personal_finance_manager
print("Personal Finance Tracker")
print("main menu")
print("1.Show account details.\n 2.Add expense \n 5.delete entry \n 6.Quit")
choice = int(input("Enter your choice: "))
match choice:
    case "1":
        show_details()


def show_details():
    print("account details")
    for k,v in details.items():
        print(k,v)




details={"karan":{"age":26,"balance":45000},
        "aswin":{"age":23,"balance":50000},
         "athul":{"age":25,"balance":36000}}
