msg = 'hello world!123'
print(msg)
ch=0
dig=0
for letter in msg:
    if letter.isalpha():
         ch=ch+1
    elif letter.isdigit():
      dig=dig+1
print(ch)
print(dig)


