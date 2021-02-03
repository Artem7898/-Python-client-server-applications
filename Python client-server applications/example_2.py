# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
a = 'class'
b = bytes(a, 'utf-8')
c = str(b, 'utf-8')
print(b)
a = 'class'
len(a)


d = 'function'
e = bytes(d, 'utf-8')
print(e)
d = 'function'
len(d)

g = 'method'
h = bytes(g, 'utf-8')
print(h)
g = 'method'
len(g)

# %%

for line in check:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))

