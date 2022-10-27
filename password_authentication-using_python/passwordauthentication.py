import getpass
database = {"charan.naga": "123535", "happy.learning": "64446"}
username = input("enter your username: ")
password = getpass.getpass("Enter your password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("enter your password again : ")
        break
print("Congratulations ! you are verified ")
