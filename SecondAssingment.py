#for second Assignment
import random
import sys
class MiniBank:
    def __init__(self):
        self.r_name = ''
        self.r_passcode = ''
        self.amount = '0'
        self.main_userInfo = {}
        self.userInformation = ''
        self.login_id = 0

    def firstOption(self):
            option= input('\nPress 1 to Login/ Press 2 to Register : ')
            try:
                if int(option) == 1:
                    self.login()
                else:
                    self.register()
            except Exception as err:
                print(err)


# _______________Checking Email____________________________
    def checkUsername(self):
        uname, my_string = self.validEmail(self.r_name)
        domain = ["@gmail.com", "@yahoo.com", '@icloud.com', '@outlook.com']
        print(uname)
        print(my_string)
        flag = False
        uflag = False
        dflag = False
        for i in uname:
            if i >= chr(48) and i <= chr(57) or i >= chr(65) and i <= chr(90) or i>= chr(97) and i<= chr(122):
                uflag = True
        for i in range(len(domain)):
            if my_string == str(domain[i]):
                print(my_string)
                dflag = True
                break

        if(uflag == True and dflag == True):
            print('Valid username...')
            flag = True
        else:
            print('Invalid username!')
            flag = False
        return flag

# _______________Checking Passcode____________________________
    def validPasscode(self, passcode):
        # to check length
        if not len(passcode) <= 10 and not len(passcode) >= 6:
            return False
        # to check space
        for i in passcode:
            if i == chr(32):
                return False
        # to check digit 0-9
        if True:
            count = 0
            for i in passcode:
                if i >= chr(48) and i <= chr(57):
                    count = 1
            if count == 0:
                return False
        # to check special character
        if True:
            count = 0
            for i in passcode:
                if i >= chr(33) and i <= chr(47) or i >= chr(58) and i <= chr(64) or i >= chr(91) and i<= chr(96) or i >= chr(123) and i<= chr(126) :
                    count = 1
            if count == 0:
                return False
        #to check capital letters
        if True:
            count = 0
            for i in passcode:
                if i >= chr(65) and i <= chr(90):
                    count = 1
            if count == 0:
                return False
        # to check small letters
        if True:
            count = 0
            for i in passcode:
                if i >= chr(97) and i <= chr(122):
                    count = 1
            if count == 0:
                return False
        # if all conditions fail
        return True

# _______________Validation Email____________________________
    def validEmail(self, username):
        user_list :list = []
        uname_list :list = []
        uname :str = ''
        my_string :str = ''
        for i in username:
            user_list.append(i)
        for i in user_list:
            uname_list.append(i)
            if i =='@':
                break
        for i in uname_list:
            if i != '@':
                uname = uname + str(i)
        for i in range(len(uname), len(user_list)):
            my_string = my_string + str(user_list[i])
        return uname, my_string

# _______________User count and ID____________________________
    def checkingUserCount(self):
        count = len(self.main_userInfo)
        return count+1

    def returnId(self, transfer_username):
        userInfo_length: int = len(self.main_userInfo)
        for i in range(1, userInfo_length + 1):
            if self.main_userInfo[i]["mail"] == transfer_username:
                return i
        return None

# _______________File Reading___________________________
    def fileReading(self):
        with open(self.userInformation,'r') as fileread:
            contents = fileread.readlines()
            self.login_id = 1
            for i in contents:
                # id: int = self.checkingUserCount()
                mail,passcode,money = i.split(" ")
                myForm = {self.login_id:{"mail":mail,"passcode":passcode,"amount":money}}
                self.main_userInfo.update(myForm)
                self.login_id=self.login_id+1

# _______________Exit user / exit register___________________________
    def exitUser(self,l_username,l_passcode):
        self.fileReading()
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1):
            if self.main_userInfo[i]["mail"] == l_username and self.main_userInfo[i]["passcode"] == l_passcode:
                return True
        return False

    def exitRegister(self, email):
        user_count = len(self.main_userInfo)
        for i in range(1, user_count + 1):
            if self.main_userInfo[i]["mail"] == email:
                return True
        return False

# _______________Checking Digit___________________________
    def checkDigit(self, menu):
        flag = False
        for i in menu:
            if i >= chr(48) and i <= chr(57):
                flag = True
            else:
                flag = False
                break
        if flag == False:
            print('Your input is invalid!')
        return flag

# _______________Show user information___________________________
    def showUser(self):
        print("\n----------USER INFORMATION LISTS----------")
        user_length = len(self.main_userInfo)
        for i in range(1,user_length+1):
            username, email = self.validEmail(self.main_userInfo[i]["mail"])
            print("Account Holder: ", username)
            print("Accout Email: ",self.main_userInfo[i]["mail"])
            print("Account Password: ", self.main_userInfo[i]["passcode"])
            print("Available balance: $", self.main_userInfo[i]["amount"])

# _______________Account Detail Menu___________________________
    def userAccount(self, login_id):
        print("\n----------USER DETAIL----------")
        username, email = self.validEmail(self.main_userInfo[login_id]["mail"])
        print("Account Holder: ", username.upper())
        print("Accout Email: ", self.main_userInfo[login_id]["mail"])
        print("Account Password: ", self.main_userInfo[login_id]["passcode"])
        print("Available balance: $", self.main_userInfo[login_id]["amount"])

# _______________Account Detail Menu___________________________
    def detailAccount(self,login_id):
        print("\n----------ACCOUNT DETAIL----------")
        username, email = self.validEmail(self.main_userInfo[login_id]["mail"])
        print("Account Holder: ", username.upper())
        print("Accout Email: ", self.main_userInfo[login_id]["mail"])
        print("Account Password: ", self.main_userInfo[login_id]["passcode"])
        print("Available balance: $", self.main_userInfo[login_id]["amount"])

# _______________Deposit Menu___________________________
    def depositMoney(self, login_id, deposit_amount):
        my_balance :int = int(self.main_userInfo[login_id]['amount'])
        self.main_userInfo[login_id]['amount'] = my_balance + deposit_amount
        print('Current account balance: $',self.main_userInfo[login_id]['amount'])
        self.unpackingToString()

# _______________Transfer Menu___________________________
    def transferMoney(self,login_id, transfer_id, transfer_amount):
        my_balance :int = int(self.main_userInfo[login_id]['amount'])
        receiver_balance :int = int(self.main_userInfo[transfer_id]['amount'] )
        if(my_balance >= transfer_amount):
            self.main_userInfo[login_id]['amount'] = my_balance - transfer_amount
            self.main_userInfo[transfer_id]['amount'] = receiver_balance + transfer_amount
            self.userAccount(login_id)
            self.userAccount(transfer_id)
            print(self.main_userInfo)
            self.unpackingToString()
        else:
             print("Insufficient fund!")
             print("Your balance is ${0} only.".format(self.main_userInfo[login_id]['amount']))
             print("Try with lesser amount than balance.")

# _______________Withdraw Menu___________________________
    def withdrawMoney(self,login_id, withdraw_amount):
        my_balance :int = int(self.main_userInfo[login_id]['amount'])
        if my_balance >= withdraw_amount:
            self.main_userInfo[login_id]['amount'] = my_balance-withdraw_amount
            print('${0} withdraw successful!'.format(withdraw_amount))
            print('Current account balance: $',self.main_userInfo[login_id]['amount'])
            self.unpackingToString()
        else:
            print("Insufficient fund!")
            print("Your balance is ${0} only.".format(self.main_userInfo[login_id]['amount']))
            print("Try with lesser amount than balance.")
            print()

# _______________Update Menu___________________________
    def updateName(self, login_id, newName):
        self.main_userInfo[login_id].update({"mail": newName})
        self.userAccount(login_id)
        self.unpackingToString()

    def updatePw(self, login_id, newPw):
        self.main_userInfo[login_id].update({"passcode": newPw})
        self.userAccount(login_id)
        self.unpackingToString()

    def updateAmount(self, login_id, newAmount):
        self.main_userInfo[login_id].update({"amount": newAmount})
        self.userAccount(login_id)
        self.unpackingToString()

# _______________Unpacking Data___________________________
    def unpackingToString(self):
        # self.fileReading()
        for i in range(1, len(self.main_userInfo)):
            mail = self.main_userInfo[i]["mail"]
            passcode = self.main_userInfo[i]["passcode"]
            amount = str(self.main_userInfo[i]["amount"])
            # print(mail, passcode, amount)
            toWriteUpdateDataToFile =mail+" "+passcode+" "+amount+"\n"

            if i == 1:
                with open("userInformation.txt", 'w') as fileUnpack:
                    fileUnpack.write(toWriteUpdateDataToFile)
                fileUnpack.close()
            else:
                with open("userInformation.txt", 'a') as fileUnpackAppend:
                    fileUnpackAppend.write(toWriteUpdateDataToFile)
                fileUnpackAppend.close()

# _______________Transaction Menu___________________________
    def menu(self, login_id ):
        print("""
                TRANSACTION 
            *******************
                Menu:
                1. Account Detail
                2. Deposit
                3. Transfer
                4. Withdraw
                5. Update
                6. Exit
            *******************
            """)
        while True:
            menu_input = input('\nEnter 1,2,3,4,5 or 6 : ')
            flag: bool = self.checkDigit(menu_input)
            if flag:
                if int(menu_input) == 1:
                    self.detailAccount(self.login_id)
                elif int(menu_input) == 2:
                    print("\n----------Deposit Money----------")
                    deposit_amount: int = int(input('How much you want to deposit : $'))
                    self.depositMoney(self.login_id, deposit_amount)
                elif int(menu_input) == 3:
                    print("\n----------Transfer Money----------")
                    transfer_username: str = input('Pls enter username to transfer : ')
                    transfer_id: int = self.returnId(transfer_username)
                    transfer_amount: int = int(input('How much you want to transfer : $'))
                    print("\n We get to transfer ID : ", transfer_id)
                    print("\n My ID : ", login_id)
                    self.transferMoney(self.login_id, transfer_id, transfer_amount)
                elif int(menu_input) == 4:
                    print("\n----------Withdraw Money----------")
                    withdraw_amount: int = int(input("How much you want to withdraw : $"))
                    self.withdrawMoney(self.login_id, withdraw_amount)
                elif int(menu_input) == 5:
                    print("""
                Update Account
            *****************
                 Menu:
                 1. Change name
                 2. Change password
                 3. Change amount
            *****************
                                """
                          )
                    while True:
                        menu = int(input('Enter 1,2 or 3 : '))
                        if (menu == 1):
                            while True:
                                newName = input('Enter you want to change email : ')
                                self.r_name = newName
                                flag: bool = self.checkUsername()
                                if flag:
                                    self.updateName(self.login_id, newName)
                                    break
                                else:
                                    continue
                        elif (menu == 2):
                            while True:
                                newPw = input('Enter you want to change password : ')
                                flag :bool = self.validPasscode(newPw)
                                if flag:
                                    self.updatePw(self.login_id, newPw)
                                    break
                                else:
                                    continue
                        elif (menu == 3):
                            newAmount = int(input('Enter you want to change amount : $'))
                            self.updateAmount(self.login_id, newAmount)
                        else:

                            break
                elif int(menu_input) == 6:
                    name,email = self.validEmail(self.main_userInfo[login_id]["mail"])
                    print(f"""     
                 printing receipt..............
            ****************************************
                  Transaction is now complete.                         
                  Transaction number: {random.randint(10000, 1000000)} 
                  Account holder: {name.upper()}   
                  Account email: {self.main_userInfo[login_id]['mail']}               
                  Account password: {self.main_userInfo[login_id]['passcode']}                
                  Available balance: ${self.main_userInfo[login_id]['amount']}                    

                  Thanks for choosing us as your bank                  
            ****************************************
                        """)

                else:
                    self.firstOption()
                    break

# _______________Login User____________________________
    def login(self):
        print('\n-----------This is Login Form---------\n')
        with open('userInformation.txt', 'a') as filewrite:
            self.userInformation = 'userInformation.txt'
        self.fileReading()
        while True:
            l_username = input('Pls enter user name to login : ')
            l_passcode = input('Pls enter user passcode to login : ')
            exitUser: bool = self.exitUser(l_username, l_passcode)
            if (exitUser):
                 print('Login Successful...\n')
                 self.login_id: int = self.returnId(l_username)
                 self.menu(self.login_id)
            else:
                 print('You cannot login!')
                 break

# _______________Register user____________________________
    def register(self):
        print('\n-----------This is Register Form---------\n')
        while True:
            r_username = input('Pls enter user name to register : ')
            self.r_name = r_username
            flagName = self.checkUsername()
            if flagName:
                while True:
                    r_passcode1 = input('Pls enter user passcode to register : ')
                    flagPw = self.validPasscode(r_passcode1)
                    if flagPw:
                        print('Valid passcode...')
                        r_passcode2 = input('Pls enter again passcode to comfirm : ')
                        if(r_passcode1 == r_passcode2):
                            with open('userInformation.txt','a') as filewrite:
                                self.userInformation ='userInformation.txt'
                            self.fileReading()
                            exit_register : bool = self.exitRegister(self.r_name)
                            if not exit_register:
                                with open(self.userInformation, 'a') as file1:
                                     userInfo = self.r_name + " " + r_passcode1 + " " + self.amount + "\n"
                                     file1.write(str(userInfo))
                                     print("########### Success Registered! ##########\n")
                                     file1.close()
                                self.fileReading()
                                
                                self.showUser()
                            else:
                                print('Data is already exit!')
                                self.login()
                        break
                    else:
                        print('Invalid passcode!')
                        continue
                break
            else:
                continue

# _______________Main____________________________
print("\n*******WELCOME TO BANK OF MYBANK*******")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
if __name__ == "__main__":
    miniBank : MiniBank = MiniBank()
    while True:
        miniBank.firstOption()


     