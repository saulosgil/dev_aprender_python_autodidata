# O que são APIs?

API é a sigla para Application Programming Interface, que em português significa Interface de Programação de Aplicações. De uma maneira muito simples, uma API é um programa que envia e recebe informações entre um site ou aplicação e os seus utilizadores. As APIs funcionam como um elo entre as diferentes aplicações a serviço do utilizador.

Elas possibilitam a comunicação entre plataformas por meio de uma série de padrões e protocolos.

Por exemplo, se um desenvolvedor quiser criar um aplicativo de fotos para Android, ele poderá ter acesso à câmera do celular através da API do sistema operacional, sem ter a necessidade de criar uma nova interface de câmera do zero. Portanto, as APIs são essenciais para a criação de softwares, aplicativos, programas e plataformas diversas.

Fonte: [O que é API e para que serve?](https://www.techtudo.com.br/listas/2020/06/o-que-e-api-e-para-que-serve-cinco-perguntas-e-respostas.ghtml)

## Onde encontrar APIs oficiais e não oficiais

- APIs que possuem documentação em Python:

[List of Python API Wrappers](https://github.com/realpython/list-of-python-api-wrappers)

- Lista de API's públicas:

[Public APIs - A collective list of free APIs for use in software and web development](https://github.com/public-apis/public-apis)

[Public APIs - an attempt to categorise different APIs scoured from the web](https://github.com/n0shake/Public-APIs)

[Public APIs - search from Github](https://github.com/search?q=api+list&type=Reposito...)

## Consultando APIs usando Postman

O Postman é uma ferramenta que dá suporte à documentação das requisições feitas pela API. Ele possui ambiente para a documentação, execução de testes de APIs e requisições em geral.

Ao utilizá-lo, você passará a trabalhar com APIs de modo mais eficiente, construindo solicitações rapidamente e, ainda, poderá guardá-las para uso posterior, além de conseguir analisar as respostas enviadas pela API, tudo por meio de uma interface gráfica.

Para isso, basta instalar o Postman utilizando o link abaixo:

- [Site do Postman](https://www.postman.com)

## GET(Obter recursos) e Como Criar uma API com Flask

1 - Definir o objetivo da API:
ex: Iremos montar uma api de blog, onde podera consultar, editar, criar e excluir postagens em um blog usando API

2 - Qual sera o URL base do API?
ex: Quando é criado uma aplicação local ela terá um url do tipo http://localhost:5000 , porem quando for subir para nuvem, terá que comprar ou usar um domínio como url base, IMAGINE devaprender.com/api

3 - Quais os endpoints?
ex: Se o requisito é de poder consultar, editar, criar e excluir, terá que disponibilizar os endpoints para essas questões >/postagens

4 - Quais recursos será disponibilizado pelo api?
ex: informações sobre as postagens

5 - Quais verbos http serão disponibilizados?
ex: GET - POST - PUT - DELETE

6 - Quais são os URL completos para cada um?
ex: http://localhost:5000
GET - http://localhost:5000/postagens - para obter todos recursos;

     GET id - http://localhost:5000/postagens/1 - para obter recurso especifico;

     POST - http://localhost:5000/postagens - para criar novo recurso;

     PUT - http://localhost:5000/postagens - para alterar um recurso;

     DELETE - http://localhost:5000/postagens - para deletar um recurso;

Essa lista é importante pois podera ser passada para uma documentação para que pessoas saibam quais recursos tem disponiveis para acesso
