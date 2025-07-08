save_id = "admin"
save_pw = "1234"

input_id = input("your id: ")
input_pw = input("your password: ")

if save_id ==input_id and save_pw == input_pw:
    print("success login")
elif save_id != input_id:
    print("wrong id")
elif save_pw != input_pw:
    print("wrong password")
else:
    print("login failed")   