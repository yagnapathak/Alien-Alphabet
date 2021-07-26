alpha = input()
alpha = "".join([ i.upper() + i for i in alpha ])
dec = "".join(sorted(input(), key=lambda x: alpha.index(x)))
print (dec)
