def palindrom(text):
    text = text.replace(" ", "").lower()
    l = 0
    r = len(text) - 1
    
    while l < r:
        if text[l] != text[r]:
            return False
        l += 1
        r -= 1
    
    return True

word = input("Vuvedi duma: ")

if palindrom(word):
    print("Dumata e palindroma")
else:
    print("Dumata ne e palindroma")
