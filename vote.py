miaka = int(input("Enter age: "))
if miaka>=18:
    print("You can vote")
else:
    print("You still a kid")

# new code
balance = 25000
withdraw = int(input("Enter amount: "))

if withdraw>=balance:
    print("Transaction successful")
else:
    fuliza = sum(withdraw-balance)
    print("You have insufficient funds. Would you like to fuliza Ksh " + fuliza + "?")