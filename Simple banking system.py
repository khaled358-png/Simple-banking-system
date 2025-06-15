accounts = {
    "khaled": {"email": "khaled@example.com", "balance": 1},
    "gamal": {"email": "gamal@example.com", "balance": 2},
    "helal": {"email": "helal@example.com", "balance": 3}
}
# test 


name = input("Enter your name: ")

if name in accounts:
    print("Choose an operation:")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = input("Chooes  number: ")

    if choice == "1":
        print("Your current balance is:", accounts[name]["balance"])

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        accounts[name]["balance"] += amount
        print("Deposit successful. New balance:", accounts[name]["balance"])

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[name]["balance"]:
            accounts[name]["balance"] -= amount
            print("Withdrawal successful. New balance:", accounts[name]["balance"])
        else:
            print("Insufficient balance.")

    else:
        print("Invalid choice.")
else:
    print("User not found.")