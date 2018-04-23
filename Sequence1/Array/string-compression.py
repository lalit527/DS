def compress(s):
    n = len(s)
    count = 1
    current_char = s[0]
    current_index = 1
    final_str = ""

    while current_index < n:
        if current_char == s[current_index]:
            count += 1
        else:
            final_str += current_char + str(count)
            current_char = s[current_index] 
            count = 1
        current_char = s[current_index]
        current_index += 1
    final_str += current_char + str(count)
    return  final_str

s = "AAAAABBBBCCCCD"
print(compress(s))