# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
a = 'Разработка'
print(type(a))


# %%
a = 'Разработка'
b = a.encode('utf-8')
c = b.decode('utf-8')
print(b)
print(c)


# %%
s = 'Сокет'
print(type(s))


# %%
s = 'Сокет'
b = s.encode('utf-8')
c = b.decode('utf-8')
print(b, c)


# %%
d = 'Декоратор'
print(type(d))


# %%
d = 'Декоратор'
b = d.encode('utf-8')
c = b.decode('utf-8')
print(b, c)

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
check = ['разработка', 'сокет', 'декоратор']

for line in check:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))


# %%


