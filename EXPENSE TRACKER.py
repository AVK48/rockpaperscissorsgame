#creating list named "expenses" to store and track
expenses = []

#creating a while loop
while True:
    print("\n Expense Tracker Menu")
    print("\n 1.Add Expense \n 2.view Expenses \n 3.Total Expense \n 4.Exit\n")
#variable for storing the users input to the menu
    choice = input("Enter the choice( 1,2,3,4):")
#conditional statements
    if choice == "1":
        item = input("Enter Expense Name:")
        amount = float(input("Enter Expense Amount:"))
        #appending the item and item ammount
        expenses.append([item,amount])
        print("Expense is added to your list..")
    elif choice== "2":
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour Expenses:")
            #printing the expenses which are stored previously
            for expense in expenses:
                print(f"{expense[0]} - ₹{expense[1]}")

    elif choice == "3":
        #adding all the expenses in the list 
        total = sum([expense[1] for expense in expenses])
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!!")


