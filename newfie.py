username = "Per"
user_name = input("PLEASE ENTER YOUR USERNAME:   ")
while username != user_name:
    user_name = input("WRONG USERNAME, ENTER YOUR USERNAME:  ")
    
#print("welcome", username)

password = "Python"
user_password = input("Please Enter your password :    ")
while password != user_password:
    user_password = input("Incorrect  password, Enter your passworld:  ")
        
print("welcome to PYTHONHUB")
  
for _ in range(5):
    name = input("Your Name Please:  ")
    lucky = len(password)  / 2
    pri = "welcome to Python, "
    welcome = len(name) * lucky
    print(pri, name , "your lucky number is ", welcome)
    welcome = welcome / 2
    
    
print("Thanks")
