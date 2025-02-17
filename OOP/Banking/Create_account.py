from simulated_aadhaar import aadhar_data
import hashlib,random,os
from Bank import Bank

class CreateAccount(Bank):

    def __init__(self):
        self.aadhar_no = input("Enter your aadhar No: ").strip()
        if len(str(self.aadhar_no)) == 12:
            self._aadhar_check()
        else:
            print("Please Enter Valid aadhar Number")

    def _aadhar_check(self):
        if str(self.aadhar_no) in aadhar_data:
            self.__createAccount()
        else:
            print("There is no such record found.")
            
    
    def set_pin(self):
        while True:
            pin = input("Set a 4-digit PIN for your account: ").strip()
            if len(pin) == 4 and pin.isdigit():
                return self.__hash_pin(int(pin))
            print("Invalid PIN! Please enter exactly 4 digits.")


    def accounts(self,__hash_pin):
          while True:
            account_No = random.randint(10000, 99999)
            if account_No not in Bank.accounts: 
                Bank.accounts[account_No] = {
                "aadhar_no": self.aadhar_no,
                "name": aadhar_data[self.aadhar_no]["name"],
                "age": aadhar_data[self.aadhar_no]["age"],
                "gender": aadhar_data[self.aadhar_no]["gender"],
                "DOB": aadhar_data[self.aadhar_no]["DOB"],
                "hashed_pin": __hash_pin
            }
            self.account_no = account_No
            print(f"Account successfully created! Your Account No: {account_No}")
            break

    def __createAccount(self):
        print("OTP sent to your aadhar mobile Number")
        otp = random.randint(1000, 9999)
        print(f"Your OTP {otp}")
        user_OTP = int(input("Enter your OTP: ").strip())
        if len(str(user_OTP)) == 4 and str(user_OTP).isdigit() and int(user_OTP) == otp:
            __hash_pin = self.set_pin()
            self.accounts(__hash_pin)
        else:
            print("OTP Invalid")

    def __hash_pin(self, pin:int):
        salt = os.urandom(16)
        return hashlib.pbkdf2_hmac("sha256", str(pin).encode(), salt , 100000)
