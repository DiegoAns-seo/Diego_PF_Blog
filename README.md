# Diego - PF - Blog

## Descrição

Este é um projeto final de um blog desenvolvido em Python com Django, incluindo autenticação, perfis, páginas e mensagens.

## Funcionalidades

- Registro, login e logout de usuários
- Perfil com edição e alteração de senha
- Páginas de blog com criação, edição e exclusão (restritas a administradores)
- Sistema de mensagens entre usuários
- Página "Sobre mim" e Home

## Requisitos

- Python 3.13
- Django 5.1.7
- Veja `requirements.txt` para dependências completas

## Instalação

1. Clone o repositório:
   git clone https://github.com/DiegoAns-seo/Diego_PF_Blog.git cd Diego_PF_Blog

2. Crie e ative um ambiente virtual:
   python -m venv venv .\venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure o banco de dados:
   python manage.py migrate

5. Crie um superusuário:
   python manage.py createsuperuser

6. Inicie o servidor:
   python manage.py runserver

## Vídeo de Demonstração

[(https://drive.google.com/file/d/1ScyhzwLzst2iE-abBJgz2vY0DOTF_8NI/view?usp=sharing)]

## Autor

Diego Anselmo
