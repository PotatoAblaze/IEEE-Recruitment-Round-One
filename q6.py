import sqlite3 as sql
import random
import time

class Banking:

    def __init__(self) -> None:
        self.db = sql.connect('bank.db')
        self.cursor = self.db.cursor()
        
        listOfTables = self.db.execute(
        """SELECT name FROM sqlite_master WHERE type='table'
        AND name='BANK'; """).fetchall()
        
        if(listOfTables == []):
            self.db.execute('''CREATE TABLE BANK(
                Account int,
                Name varchar(50),
                Balance int
                );''')
            
    
    def restart(self):
        self.take_input()
    
    def take_input(self):
        message = '''Welcome to the Ghot Bank! We ensure your money doesn't take it lite and take flight!
Please select one of the following options using the number listed at the start of the line.
        1. Create Account
        2. Deposit Money
        3. Withdraw Money
        4. Account Summary
        5. Exit\n'''
        
        option_selected = input(message)
        if(not option_selected.isnumeric):
            print("Invalid Input! Please read the prompt message properly!")
            self.restart()
        
        option_selected = int(option_selected)
        
        match option_selected:
            case 1:
                self.create_account()
            
            case 2:
                self.deposit_money()
            
            case 3:
                self.withdraw_money()
            
            case 4:
                self.account_summary()
            
            case 5:
                print("Thank you for your patronage!")
                self.db.close()
                exit()
            
            case _:
                print("Invalid Input! Please read the prompt message properly!")
        
        
        print("Hit ENTER to continue.")
        input()
        self.restart()
                
    def create_account(self):
        name = input("Enter name:")
        account_no = random.randint(100000000, 999999999)
        balance = 0
        command = f'''INSERT INTO BANK VALUES({account_no}, '{name}', {balance})'''
        self.db.execute(command)
        print("Account created successfully!")
        print(f"Your account number is: {account_no}")
        print("Your current balance is: Rs. 0")
        self.db.commit()
    
    def deposit_money(self):
        account_no = int(input("Enter account number: "))
        results = self.db.execute(f'''SELECT * FROM BANK WHERE Account = {account_no}''').fetchall()
        if(results == []):
            print("Account not found!")
            self.restart()
        
        money_to_add = int(input("Enter deposit amount: "))
        new_balance = results[0][2] + money_to_add
        print(f"New balance set to: Rs.{new_balance}")
        
        self.db.execute(f'''UPDATE BANK SET Balance = {new_balance} WHERE Account = {account_no}''')
        self.db.commit()
    
    def withdraw_money(self):
        account_no = int(input("Enter account number: "))
        results = self.db.execute(f'''SELECT * FROM BANK WHERE Account = {account_no}''').fetchall()
        if(results == []):
            print("Account not found!")
            self.restart()
        
        money_to_withdraw = int(input("Enter withdrawal amount: "))
        curr_balance = results[0][2]
        if(money_to_withdraw <= curr_balance):
            new_balance = curr_balance - money_to_withdraw
            self.db.execute(f'''UPDATE BANK SET Balance = {new_balance} WHERE Account = {account_no}''')
            self.db.commit()
            print(f"New balance set to: Rs.{new_balance}")
        else:
            print("Not enough money in account!")

        
    
    def account_summary(self):
        account_no = int(input("Enter account number: "))
        results = self.db.execute(f'''SELECT * FROM BANK WHERE Account = {account_no}''').fetchall()
        if(results == []):
            print("Account not found!")
            self.restart()
            
        print(f"Name of owner: {results[0][1]}")
        print(f"Current Balance: Rs.{results[0][2]}")
        
    
if __name__ == '__main__':
    obj = Banking()
    obj.take_input()