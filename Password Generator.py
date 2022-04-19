import random

Length = int(input("Enter the length of your password"))
if Length < 6:
    print("Your Password Should Consist at Least of 6 Characters")
    quit()
else:
    Characters = "`qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
    password = "".join(random.sample(Characters, Length))
    print(password)
