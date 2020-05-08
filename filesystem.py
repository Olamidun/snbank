import os
import random
from pathlib import Path


def login():
    question = input("Enter 'login' to login and 'Close App' to close app: ")
    while question == 'login':
        username1 = input('Enter username: ')
        password1 = input('password: ')
        with open('staff.txt', 'r') as file:
            content = file.read()
            if username1 in content and password1 in content:
                print('login successful')
                with open('user_session.txt', 'a') as user_session:
                    user_session.write(username1)
                    user_session.write(password1)

                while True:
                    account_option = input(
                        'Hey there, what do you want to do today? 1 to create account, 2 to check account details, 3 to logout')
                    if account_option == "1":
                        def create_account():
                            account_name = input('Enter account name: ')
                            opening_balance = float(input('Enter opening balance: '))
                            account_type = input('Enter account type: ')
                            account_email = input('Enter email address: ')
                            n = 10
                            account_password = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
                            print(f'Account number: {account_password} please make sure to write this account number down')
                            with open('customer.txt', 'a') as customer_account:
                                customer_account.write(account_name)
                                customer_account.write('\n' + str(opening_balance))
                                customer_account.write('\n' + account_type)
                                customer_account.write('\n' + account_email)
                                customer_account.write('\n' + account_password)

                        create_account()
                        continue
                    elif account_option == "2":
                        def account_details():
                            account_number = int(input('Enter your account number: '))
                            with open('customer.txt', 'r') as customer:
                                for line in customer:
                                    if str(account_number) in line:
                                        print('fetching data....')
                                        print(line)
                                    elif str(account_number) not in line and username1 in line:
                                        print('you are not the owner of the account number, type in the correct account number')
                                        break

                        account_details()

                    elif account_option == '3':
                        os.unlink('user_session.txt')
                        login()

            else:
                print('invalid input')
                continue
    while question == 'Close App':
        exit()

login()




