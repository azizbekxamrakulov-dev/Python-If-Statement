a = int(input("1-tomon: ")) 
b = int(input("2-tomon: ")) 
c = int(input("3-tomon: ")) 
 
if a == b == c: 
    print("Teng tomonli") 
elif a == b or a == c or b == c: 
    print("Teng yonli") 
else: 
    print("Turli tomonli")
