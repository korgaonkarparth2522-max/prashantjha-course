# #positional arguments
# def login(username, password): # called function  
#         if username ==  password:  
#                 print("login successfully")   
#         else:  
#                 print("you have entered wrong credentials")  
# username = input("Enter your username:")
# password = input("Enter your password:")
# login(username, password) #calling function

# # keyword arguments
# def login(username, password): # called function  
#         if username ==  password:  
#                 print("login successfully")   
#         else:  
#                 print("you have entered wrong credentials")  
# username = input("Enter your username:")
# password = input("Enter your password:")
# login(username = "admin", password = "admin") #calling function

# #default arguments
# def cityName(city="pune"):
#     print(city)
# cityName("city") 
# cityName()

# # variable length arguments
# def nameOfCitys(*city):
#     print("City name's =", city) 
# nameOfCitys("pune", "mumbai", "nagpur", "nashik")