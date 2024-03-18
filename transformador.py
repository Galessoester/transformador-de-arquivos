import streamlit as st
from PIL import Image
import io

# Função para transformar em JPG
def transformaJpg(arquivo):
    img = Image.open(arquivo)
    img = img.convert('RGB')  # Convertendo para RGB para suportar formato JPG
    return img

# Função para transformar em PNG
def transformaPng(arquivo):
    img = Image.open(arquivo)
    return img

# Função para transformar em WEBP
def transformaWebp(arquivo):
    img = Image.open(arquivo)
    img = img.convert('RGB')  # Convertendo para RGB para suportar formato WEBP
    return img

# Função para download do arquivo transformado
def download_arquivo(img, formato):
    output = io.BytesIO()
    img.save(output, format=formato)
    return output.getvalue()

st.markdown('''
# Oi amorzaum 🥰
            
Como você é incrivel e faz as coisinhas pensando em mim com **TODO AMOR E CARINHO DO MUNDO**
            
To te dando uma ajudinha pra facilitar a vida 


''')

arquivo = st.file_uploader(
    'Coloque aqui a sua imagem 🖼️',
    type=['jpg', 'png', 'webp', 'jpeg'],
    accept_multiple_files=True
)

if arquivo:
    escolha = st.selectbox(
        'Qual tipo você vai querer? 👀',
        options=['JPG', 'PNG', 'WEBP']
    )
    if escolha == 'JPG':
        img_transformada = transformaJpg(arquivo)
        formato = 'jpeg'
    elif escolha == 'PNG':
        img_transformada = transformaPng(arquivo)
        formato = 'png'
    elif escolha == 'WEBP':
        img_transformada = transformaWebp(arquivo)
        formato = 'webp'

        st.image(img_transformada, caption=f'Imagem transformada para {escolha}')

    st.download_button(
        label=f'Download {escolha}',
        data=download_arquivo(img_transformada, formato),
        file_name=f'ta_aqui_sua_imagem_transofrmada_amorzao_lindo_maravilhoso_perfeito_sensacional_divino_incrivel_meu_deus_que_que_eh_isso.{formato}',
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
