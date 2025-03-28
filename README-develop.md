## Stack

Utilizando o framework python fastapi + Uvicorn ASGI + jinja2 + Railway + RSS Crunchyroll Notícias

## Documentação

Para as APIs e também no contexto do template está sendo usado os métodos ```get_posts``` e o ```get_post_by_id``` da classe ```Posts```, todas as vezes que esse métodos forem chamados a biblioteca feedparser vai fazer response dos 50 posts do RSS, todos em formato XML que será o lixo para ser filtrado inicialmente pelo método ```set_posts```.

Esse processo vai ser dividido em ID, title, description, media e content, sendo a primeira parte do tratamento, o método ```set_posts```.

O ```get_posts``` vai ser o método que vai entregar o JSON completo, fazendo todo a segunda e último etapa do processo de tratamento para a utilização dos dados. Os dados vão passar pela formatação de parágrafos, a classe ```Formatter``` e seu método ```filter_content```. Que vai usar o content do ```set_posts``` para facilitar, já que eles vão estar no formato certo e com o tipo "str", e depois removê los para não ter dados desnecessários, atrasar a requisição e gastar memória. Cada parágrafo vai ser dividido em initial, iddle e final Seu retorno nas APIs é o dicionário que vai ser convertido automaticamente em JSON no return do método HTTP do fastapi. O endpoint ```/api/posts``` utilizando desse mesmo método e retorna o JSON de todo os posts formatados. 

Internamente, para a formação dos templates, não é necessário as APIs, o dicionário é chamado internamente para o contexto.

```/api/post/{id}``` Nesse endpoint vai ser usado o método ```get_post_by_id```, que vai pegar todos o posts por ID, sendo atribuido por um contador dentro do laço for. Que vão estar em ordem crescente e começar por 1. O cliente vai colocar como parâmetro o ID de 1 a 50 dos posts e esse método vai retonar o dicionário pelo ID correspondente em JSON pelo fastapi.

## Clone, implemente em localhost

Faça ```git clone``` da aplicação em HTTPS, SSH ou CLI:

Exemplo em SSH

```git clone git@github.com:olavodotpy/AnimeNews.git```

Crie uma branch develop que rastreia a origin/develop do repositório:

```git checkout -b develop origin/develope```

Crie um ambiente virtual:

```python -m venv name_here```

Entre/ative seu ambiente com:

```source name_here/bin/activate```

Para sair/desativar execute:

```deactivate```

Faça um install do arquivo de manifesto:

```pip install -r requirements.txt```

execute ```main.py``` usando o fastapi:

```fastapi dev main.py```

Faça uma boa implementação e envie um PR para a branch develop 😊