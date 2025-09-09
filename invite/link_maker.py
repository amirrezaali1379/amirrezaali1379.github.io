with open('invite/names.txt','r',encoding='utf8') as file:
    names=file.readlines()


with open('invite/index.html','r',encoding='utf8') as file:
    html=file.read()

id='2'

for i,name in enumerate(names):
    html2=html.replace(' namemamad ',name)
    with open(f'invite/{id}/{i}.html','w',encoding='utf8') as file:
        file.write(html2)
    with open(f'invite/{id}_links.txt','a',encoding='utf8') as file:
        file.write(f'{(name.strip())}:   https://amirrezaali1379.github.io/invite/{id}/{i}.html')
        file.write('\n')