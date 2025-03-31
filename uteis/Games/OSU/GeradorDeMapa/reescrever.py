import os
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


conteudo = "aaaaaaaaa"
with open(f"{desktop_path}/teste.osk", mode="w", encoding="UTF-8") as arquivo:
    arquivo.write(conteudo)