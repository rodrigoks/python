
cidade = str(input('Informe o nome de uma cidade: ')).strip()
if cidade.lower().find('santo') != -1:
    print('Esta cidade contem Santo.')
else:
    print('Esta cidade nao contem Santo.')
