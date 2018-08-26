def string_compress(s):
  count = 1
  result = ""
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
    else:
      result += s[i-1] + str(count)
      count = 1
  return result + s[len(s) - 1] + str(count)


s = "aabcccccaaa"
print(string_compress(s))