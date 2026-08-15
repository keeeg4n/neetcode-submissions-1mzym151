class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts: int = 0
    total_balance: int = 0
    
    def __init__(self, name: str, balance: str) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

# TODO: Create two accounts
# TODO: Print the information using the mentioned format
alice_bank_account: "BankAccount" = BankAccount("Alice", 1000)
bob_bank_account: "BankAccount" = BankAccount("Bob", 2000)

print("Alice's balance: ${}".format(alice_bank_account.balance))
print("Bob's balance: ${}".format(bob_bank_account.balance))
print("Total Accounts: {}".format(BankAccount.total_accounts))
print("Total Balance: ${}".format(BankAccount.total_balance))


