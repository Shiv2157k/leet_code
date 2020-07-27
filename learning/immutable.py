
a = []
b = a

c = []
# list are mutable

k = 2157
# doesn't create a new one.
l = 2157

print(id(k))
print(id(l))

k = 8990

print(id(k))
print(id(l))

a.append(19)
print(a)
print(b)
print(c)
print(id(a))
print(id(b))

d = ()
e = ()
d = d + (15, )

