# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
check = ['разработка', 'администрирование', 'protocol', 'standard']
for i in check:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print('----')


# %%
