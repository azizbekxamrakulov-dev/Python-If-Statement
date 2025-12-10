email = input("Email kiriting: ") 
 
if " " in email: 
    print("Email manzili noto‘g‘ri") 
elif "@" in email and "." in email.split("@")[-1]: 
    print("Email manzili to‘g‘ri") 
else: 
    print("Email manzili noto‘g‘ri")
