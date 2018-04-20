def checkAnagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    for letter in count:
        if count[letter] != 0:
            return False

    return True

# Testing block
print(checkAnagram("hell2o", "hello"))