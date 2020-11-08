import re

#pattern=r"\d"
#pattern=r"^\d$"
#pattern=r"^\D$"
#pattern=r"^\d\d\d$"
#pattern=r"^\d{3}$"
#pattern=r"^\d{3,5}$"
#pattern=r"^\d{,5}$"
#pattern=r"^\d{3,}$"
#pattern=r"^\d+$"
#pattern=r"^\d*$"
#pattern=r"^\d+[$]?$"
#pattern=r"^[yY][eE][sS]$"
#pattern=r"^[1-6]$"
#pattern=r"^[a-z]+$"
#pattern=r"^[A-Z]+$"
#pattern=r"^\w$"
#pattern=r"^\s$"
#pattern=r"car\b"
#pattern=r"car\B"
#pattern=r"^.$"
#pattern=r"^(([yY][eE][sS])|([nN][oO]))$"
pattern=r"^(((13\d{2})/(0?[1-6])/((0?[1-9])|([12]\d)|(3[01])))|((13\d{2})/((0?[7-9])|(1[0-2]))/((0?[1-9])|([12]\d)|(30))))$"

while True:
    expression=input("Enter expression : ")
    #print(re.match(pattern,expression)!=None)
    if re.match(pattern,expression):
        print("Yes")
    else:
        print("No")
