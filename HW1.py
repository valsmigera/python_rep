a = "HZ"
b = 10
c = 10.25
d = bytes([10, 15])
e = ('1', '2')
f = (1, 2, 3, 4)
g = set('qwerty')
h = frozenset('qwerty')
i = dict(short='dict', long='dictionary')
print("This is,", type(a))
print("This is,", type(b))
print("This is,", type(c))
print("This is,", type(d))
print("This is,", type(e))
print("This is,", type(f))
print("This is,", type(g))
print("This is,", type(h))
print("This is,", type(i))
j = "I"
k = "Like"
l = (j + k)
print(l)
print(a, str(b))
print(a + str(b))