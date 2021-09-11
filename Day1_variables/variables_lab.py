# Switch variables values in output:

a = raw_input("a value:")
b = raw_input("b value:")

vala = a
valb = b
a = valb
b = vala

print("a = " + a)
print("b = " + b)