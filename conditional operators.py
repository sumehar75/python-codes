#conditional operators
# ==, >= , <= , != , < ,>

cab_fare = 500
e_wallet = 300

print("can i book the cab:", (e_wallet>=cab_fare))

cab_fare = 500
e_wallet = 600

print("can i book the cab:", (e_wallet>=cab_fare))

cab_fare = 500
e_wallet = 500

print("can i book the cab:", (e_wallet>cab_fare))

cab_fare = 500
e_wallet = 500

print("can i book the cab:", (e_wallet>=cab_fare))

#input output operation

email = input("Enter your emal:")
password = input("Enter your password")

print("email is:",email, "and password is:", password)

print("login status:", email== "sam123@gmail.com")
print("login status :", password=="sam7503")

print("Final login status:", ((email=="sam123@gmail.com")and(password=="sam7503")))



otp= 7503
user_otp= int(input("Enter otp:"))
print("otp status= ", otp==user_otp)

#membership testing
# is and is not
a= 10
b= 20
print(a is b)#false
print(a is not b)#true
