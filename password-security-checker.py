print("PASSWORD SECURITY CHECKER")
password = input("Podaj hasło:")
print("Twoje hasło ma", len(password), "znaki.")
punkty = 0
if len(password) <10: 
    print("Twoje hasło jest za krótkie. Powinno mieć co najmniej 10 znaków.")
else:
    print("Twoje hasło jest wystarczająco długie.")
    punkty += 1
if any(znak.isupper() for znak in password):
    print("Twoje hasło zawiera co najmniej jedną wielką literę.")
    punkty += 1
else:
    print("Twoje hasło nie zawiera żadnej wielkiej litery. Powinno zawierać co najmniej jedną wielką literę.")
if any(znak.islower() for znak in password):
    print("Twoje hasło zawiera co najmniej jedną małą literę.")
    punkty += 1
else:
    print("Twoje hasło nie zawiera żadnej małej litery. Powinno zawierać co najmniej jedną małą literę.")
if any(znak.isdigit() for znak in password):
    print("Twoje hasło zawiera co najmniej jedną cyfrę.")
    punkty += 1
else:
    print("Twoje hasło nie zawiera żadnej cyfry. Powinno zawierać co najmniej jedną cyfrę.")
if any(not znak.isalnum() for znak in password):
    print("Twoje hasło zawiera co najmniej jeden znak specjalny.")
    punkty += 1    
else:
    print("Twoje hasło nie zawiera żadnego znaku specjalnego. Powinno zawierać co najmniej jeden znak specjalny.")
print("Twoje hasło ma", punkty, "punktów.")
if punkty ==5:
    print("Twoje hasło jest bardzo silne.")
if punkty ==4:
    print("Twoje hasło jest silne.")
if punkty ==3:
    print("Twoje hasło jest średnie.")
if punkty ==2:
    print("Twoje hasło jest słabe.")
if punkty ==1:
    print("Twoje hasło jest bardzo słabe.")
if punkty ==0:
    print("Twoje hasło jest bardzo słabe. Nie spełnia żadnych wymagań bezpieczeństwa.")
