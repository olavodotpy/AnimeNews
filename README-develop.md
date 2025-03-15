## Stack

Vai ser utilizado o framework python fastapi + Uvicorn ASGI + jinja2 + Railway + RSS Crunchyroll 

## APIs

Para as APIs e também no contexto do template estou usando os métodos ```get_posts``` e o ```get_post_by_id``` da minha classe ```Post```, todas as vezes que esse método for chamado a biblioteca feedparser vai fazer um "response" dos 50 posts do RSS, todos em formato XML que será lixo, então esse metodo vai fazer todo o processo de tratamento para a utilização dos dados, e seu retorno nas APIs é o dicionário que vai ser convertido automaticamente em JSON no método HTTP do fastapi.

Internamente para a formação dos templates não é necessário as APIs, o dicionário é chamado internamente para o contexto.

O endpoint ```/api/posts``` utilizando o método ```get_posts``` vai pegar todos os posts ja filtrados e formatados em: ID, title, description, media, content. os ID vão estar em ordem crescente e começar por 1.


```/api/post/{id}``` Nesse endpoint vai ser usado o método ```get_post_by_id```. O cliente vai colocar com parametro o ID de 1 a 50 dos posts e esse método vai retonar esse dicionário pelo ID correspondente em JSON pelo fastapi.

## Clone, implemente em localhost

Faça ```git clone``` da aplicação em HTTPS, SSH ou CLI:

Exemplo em SSH

```git clone git@github.com:olavodotpy/AnimeNews.git```

Depois mude a branch para a develop pois a Master é apenas de leitura:

```git checkout develop```

Crie um ambiente virtual:

```python -m venv name_here```

Faça install do arquivo de manifesto:

```pip install -r requirements.txt```

execute ```main.py``` usando o fastapi:

```fastapi dev main.py```

Faça uma boa implementação e envie um para essa mesma branch PR 😊