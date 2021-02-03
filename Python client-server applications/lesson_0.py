# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import chardet
import subprocess
args = ['ping', 'yandex.ru']
sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in sub_ping.stdout:
    print(line)


# %%
progr_1 = "Программирование"
print(progr_1)


# %%
