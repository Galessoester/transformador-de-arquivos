import streamlit as st
from PIL import Image
import io
import zipfile

def transforma(arquivo):
    img = Image.open(arquivo)
    return img

def transformaRgb(arquivo):
    img = Image.open(arquivo)
    img = img.convert('RGB')  
    return img

def download_arquivo(img, formato):
    output = io.BytesIO()
    img.save(output, format=formato)
    return output.getvalue()

st.markdown('''
# Oi amorzaum 🥰
            
Como você é incrivel e faz as coisinhas pensando em mim com **TODO AMOR E CARINHO DO MUNDO**
            
To te dando uma ajudinha pra facilitar a vida 
''')

arquivos = st.file_uploader(
    'Coloque aqui a sua imagem 🖼️',
    type=['jpg', 'png', 'webp', 'jpeg'],
    accept_multiple_files=True
)

texto = 'ta_aqui_suas_imagens_transofrmadas_amorzao_lindo_maravilhoso_perfeito_sensacional_divino_incrivel_meu_deus_que_que_eh_isso'

if arquivos:
    escolha = st.selectbox(
        'Qual tipo você vai querer? 👀',
        options=['JPG', 'PNG', 'WEBP']
    )
    if len(arquivos) == 1: 
        arquivo = arquivos[0]
        if escolha == 'JPG':
            img_transformada = transformaRgb(arquivo)
            formato = 'jpeg'
        elif escolha == 'PNG':
            img_transformada = transforma(arquivo)
            formato = 'png'
        elif escolha == 'WEBP':
            img_transformada = transformaRgb(arquivo)
            formato = 'webp'
        st.download_button(
            label=f'Download imagem',
            data=download_arquivo(img_transformada, formato),
            file_name=f'{texto}.{formato}',
        )

    else:
        arquivos_transformados = []
        for arquivo in arquivos:
            if escolha == 'JPG':
                img_transformada = transformaRgb(arquivo)
                formato = 'jpeg'
            elif escolha == 'PNG':
                img_transformada = transforma(arquivo)
                formato = 'png'
            elif escolha == 'WEBP':
                img_transformada = transformaRgb(arquivo)
                formato = 'webp'

            arquivos_transformados.append((img_transformada, arquivo.name))

        if st.button('Download em uma pasta zipada'):
            zip_bytes = io.BytesIO()
            with zipfile.ZipFile(zip_bytes, 'w') as zip_file:
                for img_transformada, filename in arquivos_transformados:
                    buffer = io.BytesIO()
                    img_transformada.save(buffer, format=formato)
                    zip_file.writestr(filename, buffer.getvalue())

            zip_bytes.seek(0)
            st.download_button(
                label='Clique aqui para baixar',
                data=zip_bytes.getvalue(),
                file_name=f'{texto}.zip',
                mime='application/zip'
            )

container = st.container()
a, b, c = container.columns(3)
a.image('media/amorzao.gif')
b.image('media/bunny.gif')
c.image('media/cama.gif')

container2 = st.container()
a, b, c = container.columns(3)
a.image('media/coracao.gif')
b.image('media/celular.gif')
c.image('media/abraco.gif')

st.title('Não esquece que eu te amo muitão ❤️')
