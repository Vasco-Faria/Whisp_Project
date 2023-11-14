# Projeto TPW1 (Rede Social)

## 1. Membros do Grupo

| NMec | Name | email | 
|:---: |:---|:---:|
| 108317 | Miguel Aido Miragaia          | [miguelmiragaia@ua.pt](https://github.com/Miragaia)      |
| 107323 | Vasco Miguel Fernandes Faria  | [vascomfaria@ua.pt](https://github.com/Vasco-Faria)      |
| 107634 | Rodrigo Martins Graça         | [rodrigomgraca@ua.pt](https://github.com/rodrigograc4)   |

## 2. Descrição do Projeto
**Introdução**
- Este é um projeto de desenvolvimento de uma rede social básica utilizando o Django Framework. O objetivo principal é criar uma plataforma onde os users podem se registrar, criar posts, fazer upload de imagens e interagir uns com os outros de diversas formas.

**Objetivos**

| Objectives | Done |
|:---: |:---:|
| Client and Server side Web App| X |
| Interfaces for client and functionalities for server-side, associated with the database, to allow all operations: information showing, data searching, insertion, updating, deleting and validation| X |
| Public and private parts, using the login functionality. These parts must have a clear differentiation in the set of allowed operations| X |
| It must also be developed in a modular way, encapsulating the three components: data, logic and presentation; using all learned technics | X |
| It must be deployed in the public site, pythonanywhere, in order to be accessed from anywhere | X |

## Funcionalidades Atuais

Neste momento, as funcionalidades principais incluem:
- Registro e autenticação de users (AllAuth, Autenticação com gmail).
- Criação e visualização de posts (Upload de Texto, Foto, Video).
- Interação/Informação com/de posts (Data de criação, Autor, Likes, Comentários).
- Página de Feed (Posts de todos os users, Posts de users seguidos).
- SearchBar (Pesquisa no feed por caracteres presentes nos posts)
- Seguidores (Interação entre perfis de users)
- Perfil de User (Posts, Seguidores, Seguindo, Informações, Posts Media/Texto)
- Personalização de Perfil (Banner, Avatar)
- Interação com posts (Like, Comentários)
- Sistema de notificações (Novo seguidor, Novo comentário, Novo like, Admin apagou post)
- Admin (Apagar post, Apagar comentário)


## To-Do List (Recursos Futuros)

Funcionalidades a adicionar no futuro:
- **Chat ou Mensagens Diretas**: Introduzir um recurso de chat ou mensagens diretas para que os users possam se comunicar uns com os outros de forma mais direta e privada.

## How to run
**Option 1**
- Aceder ao site [https://rodrigograc4.pythonanywhere.com/](https://rodrigograc4.pythonanywhere.com/)

**Option 2**
- Correr localmente:
1. pipenv shell
2. pip install -r requirements.txt
3. python manage.py runserver 0.0.0.0:8000

## Test Accounts
- User
    ```
    username: Amelia
    password: Olaolaola
    ```

- Administrator:
    ```
    username: neyterra
    password: Olaolaola
    ```

## Notas
- O projeto presente no pythonanywhere apresenta algumas modificações em relação ao codigo aqui presente, sao apenas modificações de estilo e a adição de um butao junto da barra de pesquisa para dar "clear" dos filtros de pesquisa.

## Comandos Uteis
- django-admin startproject mysite .
- django-admin startapp blabla 
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser