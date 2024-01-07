#Question 3
string1 = "Radar"
string2 = "rad ar"
string3 = "WiLSon"
def is_palindrome(curString):
    #remove spaces and turns all strings to lowercase
    cleanStr = "".join(curString.split())
    cleanStr = "".join(cleanStr.lower())
    #reverses clean string
    revCleanStr = cleanStr[::-1]
    if (cleanStr == revCleanStr):
        return True
    return False

print(is_palindrome(string1))
print(is_palindrome(string2))
print(is_palindrome(string3))

