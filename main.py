class BankAccount:

    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def save_account(self):
        with open("accounts.txt", "a") as file:
            file.write(f"{self.account_no},{self.name},{self.balance}\n")


while True:

    print("\n==== BANK MANAGEMENT SYSTEM ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Search Account")
    print("7. Delete Account")
    print("8. Exit")

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    # CREATE ACCOUNT
    if choice == 1:

        account_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Opening Balance: "))

        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == account_no:
                        found = True
                        break

        except FileNotFoundError:
            pass

        if found:
            print("Account already exists")

        else:
            acc = BankAccount(account_no, name, balance)
            acc.save_account()
            print("Account Created Successfully")

    # DEPOSIT
    elif choice == 2:

        search_acc = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))

        updated_lines = []
        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == search_acc:

                        current_balance = float(data[2])
                        data[2] = str(current_balance + amount)

                        found = True

                    updated_lines.append(",".join(data) + "\n")

            with open("accounts.txt", "w") as file:
                file.writelines(updated_lines)

            if found:
                print("Amount Deposited Successfully")
            else:
                print("Account Not Found")

        except FileNotFoundError:
            print("No accounts found")

    # WITHDRAW
    elif choice == 3:

        search_acc = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))

        updated_lines = []
        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == search_acc:

                        current_balance = float(data[2])

                        if amount <= current_balance:

                            data[2] = str(current_balance - amount)
                            print("Amount Withdrawn Successfully")

                        else:
                            print("Insufficient Balance")

                        found = True

                    updated_lines.append(",".join(data) + "\n")

            with open("accounts.txt", "w") as file:
                file.writelines(updated_lines)

            if not found:
                print("Account Not Found")

        except FileNotFoundError:
            print("No accounts found")

    # CHECK BALANCE
    elif choice == 4:

        search_acc = input("Enter Account Number: ")

        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == search_acc:

                        print("Current Balance:", data[2])

                        found = True
                        break

            if not found:
                print("Account Not Found")

        except FileNotFoundError:
            print("No accounts found")

    # VIEW ALL ACCOUNTS
    elif choice == 5:

        try:
            with open("accounts.txt", "r") as file:

                data = file.read()

                print("\n==== ALL ACCOUNTS ====")

                if data.strip():
                    print(data)
                else:
                    print("No accounts found")

        except FileNotFoundError:
            print("No accounts found")

    # SEARCH ACCOUNT
    elif choice == 6:

        search_acc = input("Enter Account Number: ")

        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == search_acc:

                        print("\n==== ACCOUNT FOUND ====")
                        print("Account Number:", data[0])
                        print("Name:", data[1])
                        print("Balance:", data[2])

                        found = True
                        break

            if not found:
                print("Account Not Found")

        except FileNotFoundError:
            print("No accounts found")

    # DELETE ACCOUNT
    elif choice == 7:

        delete_acc = input("Enter Account Number: ")

        updated_lines = []
        found = False

        try:
            with open("accounts.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if data[0] == delete_acc:
                        found = True
                        continue

                    updated_lines.append(line)

            with open("accounts.txt", "w") as file:
                file.writelines(updated_lines)

            if found:
                print("Account Deleted Successfully")
            else:
                print("Account Not Found")

        except FileNotFoundError:
            print("No accounts found")

    # EXIT
    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")