import streamlit as st
from PIL import Image
import io
import zipfile

# Abrindo a imagem
def transforma(arquivo):
    img = Image.open(arquivo)
    return img

# Abrindo a imagem e convertendo para RGB
def transformaRgb(arquivo):
    img = Image.open(arquivo)
    img = img.convert('RGB')  
    return img

# Salvando o arquivo com o formato recebido como parametro
def download_arquivo(img, formato):
    output = io.BytesIO()
    img.save(output, format=formato)
    return output.getvalue()

# Retirar o tipo do arquivo do nome original
def renomeiaArquivo(arquivo):
    nome_arquivo = arquivo.name
    
    # Se existir ".jpg" ou ".png" ou ".webp" ou ".jpeg" no nome do arquivo, substitui essa parte com uma string vazia
    if '.jpg' in nome_arquivo:
        nome_arquivo = nome_arquivo.replace('.jpg', '')
    elif '.png' in nome_arquivo:
        nome_arquivo = nome_arquivo.replace('.png', '')
    elif '.webp' in nome_arquivo:
        nome_arquivo = nome_arquivo.replace('.webp', '')
    elif '.jpeg' in nome_arquivo:
        nome_arquivo = nome_arquivo.replace('.jpeg', '')
    return nome_arquivo

# filtra a escolha do usuário
def escolhaArquivo(escolha, arquivo):
    img_transformada = arquivo
    
    # Transforma para o formato JPG
    if escolha == 'JPG':
        # Chama o método de abertura da imagem e tranformação em RGB
        img_transformada = transformaRgb(arquivo)
        # Muda o formato para jpeg
        formato = 'jpeg'
    
    # Transforma para o formato PNG
    elif escolha == 'PNG':
        # Chama o método de abertura da imagem
        img_transformada = transforma(arquivo)
        # Muda o formato para PNG
        formato = 'png'
    
    # Transforma para o formato WEBP
    elif escolha == 'WEBP':
        # Chama o método de abertura da imagem e tranformação em RGB
        img_transformada = transformaRgb(arquivo)
        # Muda o formato para WEBP
        formato = 'webp'
    
    # retorna a imagem aberta e o formato selecionado
    return img_transformada, formato

# Introdução
st.markdown('''
# Oi amorzaum 🥰
            
Como você é incrivel e faz as coisinhas pensando em mim com **TODO AMOR E CARINHO DO MUNDO**
            
To te dando uma ajudinha pra facilitar a vida 
''')

# Caixa de upload de arquivo(s)
arquivos = st.file_uploader(
    # título
    'Coloque aqui a sua imagem 🖼️',
    
    # aceita os seguintes tipos de arquivo
    type = ['jpg', 'png', 'webp', 'jpeg'],
    
    # Aceita mais de um arquivo por vez
    accept_multiple_files = True
)

texto = 'ta_aqui_suas_imagens_transofrmadas_amorzao_lindo_maravilhoso_perfeito_sensacional_divino_incrivel_meu_deus_que_que_eh_isso'

# Confirma a existencia de arquivo(s) a ser(em) convertido(s)
if arquivos:

    # Abre selectbox e disponibiliza opções para converção
    escolha = st.selectbox(
        # label
        'Selecione o tipo a ser convertido',
        
        # opções
        options=['JPG', 'PNG', 'WEBP']
    )

     # Confirma se existe um ou mais arquivos a serem transformados.
    # Se existir apenas um arquivo a ser transformado:
    if len(arquivos) == 1: 
        arquivo = arquivos[0]
        
        # Chama a função para abrir a imagem e alterar o formato
        img_transformada, formato = escolhaArquivo(escolha, arquivo)
        
        # chama o método para renomear o arquivo
        nome = renomeiaArquivo(arquivo)
        
        # Botão de download
        st.download_button(
            label=f'Download imagem',
            data=download_arquivo(img_transformada, formato),
            file_name=f'{nome}.{formato}',
        )
    

     # Se existir mais de um arquivo a ser transformado:
    else:
        # arquivos transformados recebe um array vazio
        arquivos_transformados = []

        # Loop para cada arquivo na lista de arquivos, fazer a transformação conforme a escolha
        for arquivo in arquivos:
            # Chama a função para abrir a imagem e alterar o formato
            img_transformada, formato = escolhaArquivo(escolha, arquivo)
            
            # chama o método para renomear o arquivo
            nome = renomeiaArquivo(arquivo)

            # Adiciona o arquivo na lista de arquivos
            arquivos_transformados.append((img_transformada, nome, formato))

        # Botão para iniciar o download dos arquivos em uma pasta zipada
        if st.button('Download em uma pasta zipada'):
            # Inicializa um BytesIO para armazenar os bytes do arquivo zip
            zip_bytes = io.BytesIO()
            
            # Abre um arquivo zip no modo de escrita
            with zipfile.ZipFile(zip_bytes, 'w') as zip_file:
                # Loop através dos arquivos transformados
                for img_transformada, nome, formato in arquivos_transformados:
                    # Inicializa um BytesIO para armazenar os bytes da imagem
                    buffer = io.BytesIO()
                    
                    # Concatena o nome do arquivo com sua extensão
                    nome_com_extensao = f'{nome}.{formato}'
                    
                    # Salva a imagem no buffer com o formato apropriado
                    img_transformada.save(buffer, format=formato)
                    
                    # Escreve os bytes da imagem no arquivo zip
                    zip_file.writestr(nome_com_extensao, buffer.getvalue())

            # Reposiciona o cursor no início do BytesIO
            zip_bytes.seek(0)
            
            # Botão de download para baixar o arquivo zip
            st.download_button(
                label='Clique aqui para baixar',
                data=zip_bytes.getvalue(),
                file_name='Imagens_transformadas.zip',
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
