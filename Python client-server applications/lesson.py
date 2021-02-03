import chardet

charset = 'utf-8'
with open('test.txt', 'rb') as f:
    data = f.read()
    charset.detect(data)


with open('test.txt, 'r', encoding=charset) as f:
