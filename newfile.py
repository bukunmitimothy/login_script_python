Name = input("Full-Name Please :  ")
user_name = "AstroBukunmi"
username_user = input("Username :  ")
x = 0

#password now

password_reg = "Python3"
password_user = input("Please Enter your password : ")
y = 0

#the  while loop for the username .
while user_name != username_user:
    x += 1
    print("number of incorrect password entered  " , x)
    username_user = input("Incorrect Username, Re-enter your correct Username :  ")
    password_user = input("Enter your password:  ")
    
 #the while loop for the password    

while password_reg != password_user:
    y += 1
    print("Number of attempt password ", y)
    password_user = input("input your password:   ")
  #Welcome address  
print("Welcome ", Name)


#
