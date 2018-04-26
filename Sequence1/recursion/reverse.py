def reverse(s):
    if len(str(s)) == 1:
        return s
    
    return reverse(str(s[1:])) + str(s[0])

print(reverse("123"))