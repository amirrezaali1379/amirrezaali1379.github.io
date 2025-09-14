def change_text(current_text,new_text,file_name,id):
    with open(f'invite/{id}/{file_name}','r',encoding='utf8') as file:
        html=file.read()
        
    html2=html.replace(current_text,new_text)

    with open(f'invite/{id}/{file_name}','w',encoding='utf8') as file:
        file.write(html2)

import os
id='19'
folder_path = f"invite/{id}"  # مسیر پوشه‌ات

files = os.listdir(folder_path)

for f in files:
    if os.path.isfile(os.path.join(folder_path, f)):
        change_text('مرحومه','مرحومه مغفوره حاجیه خانم',f,id)