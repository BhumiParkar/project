def checkvowel(char):
    if char in "a e i o u A E I O U":
        return True
    else:
        return False
char = input("enter a character")

status=checkvowel(char)
if status:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a constant")