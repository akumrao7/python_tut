balance = 0.0
kyc_documents={}
def check_balance():
    print(f"Your current balance is {balance}")
    print("==========================")

def deposit(amount):
    global balance
    if amount >= 0:
        balance += amount
    else:
        print("Can not deposit a negative amount")
        print("==========================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Can not withdraw a negative amount")
        print("==========================")
    elif amount > balance:
        print("You don't have enough money")
        print("==========================")
    else:
        balance -= amount
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done.")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

if __name__ == "__main__":

    print("==========================")
    print("Welcome to the Umrao bank")
    print("==========================")
    print()
    while True:
        print('1. Check the balance')
        print('2. Deposit an amount')
        print('3. Withdraw an amount')
        print('4. Check KYC')
        print('5. Update KYC')
        print('6. Quit')

        choice = input('Enter your choice (1-6): ')
        print("==========================")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt=float(input("Enter the amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
        elif choice == '3':
            amt=float(input("Enter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdrawed successfully")
        elif choice == '4':
            check_kyc()
        elif choice == '5':
            kyc_docs={}
            n_documents=int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key=input("Enter the document's type: ")
                value=input("Enter the document's number: ")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
            print("KYC updated successfully")
        elif choice == '6':
            print("Thank you for using Umrao! Quting")
            break
        else:
            print('Invalid choice! Try again!')
            print("==========================")


    print()
    print("Thank you for your Banking with us.")