expenses = []


while True:
    print("\n Expense Tracker Menu")
    print("\n 1.Add Expense \n 2.view Expenses \n 3.Total Expense \n 4.Exit\n")

    choice = input("Enter the choice( 1,2,3,4):")

    if choice == "1":
        item = input("Enter Expense Name:")
        amount = float(input("Enter Expense Amount:"))
        expenses.append([item,amount])
        print("Expense is added to your list..")
    elif choice== "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour Expenses:")
            for expense in expenses:
                print(f"{expense[0]} - ₹{expense[1]}")

    elif choice == "3":
        total = sum([expense[1] for expense in expenses])
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!!")

