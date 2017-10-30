def adder(x, r):
    y = z + r
    import code
    code.interact(local=locals())
    return x + y

z = 7
adder(5, 6)
print("globals")
print(globals())
print("locals")
print(locals())
