![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
<img src="https://komarev.com/ghpvc/?username=deh0&label=%20Views&color=0e75b6&style=flat" alt="deh0">

## Plataforma SaaS Multi-Tenant Demo

Este repositório tem como intuito ajudar aqueles que querem aprender sobre Django multi-tenant e desejam criar o sua própria plataforma SaaS sozinho, ou em equipe. Aqui vamos descrever desde os primeiros passos, até decisões de negócio, boas práticas, levantamento dos requisitos do sistema, modelagem de dados, testes e deploy. O projeto é uma versão reduzida do projeto original, ou seja, algumas coisas vão precisar de mais pesquisas por fora do que o restante (será sinalizado quando necessário). 

Solução multi-tenant monorepo construída com Django, que permite utilizar uma versão para armazenar múltiplas empresas ao mesmo tempo e no mesmo projeto, com o mesmo banco de dados, mas que compartilham schemas diferentes. Isso permite que cada empresa tenha o seu próprio esquema e suas próprias configurações, garantindo total segurança e independência entre as empresas. O projeto é organizado como monorepo com dois projetos, o backend e o frontend, que se comunicam através de uma API Core central, que fica armazenada no backend.

### Backend: 
O Backend é o coração do nosso repositório, é ele que dá vida a tudo. Ele é responsável por armazenar a API Core, os modelos de dados, os apps modulares, as configurações, os caminhos e a lógica por trás do sistema, porque é nele que vai ficar toda a estrutura da plataforma SaaS. Basicamente ele determina o que o projeto poderá fazer, vamos utilizar a maior parte dos recursos disponíveis pelo próprio Django, como o django-tenants, django-rest-framework, django-sites, entre vários outros arquivos que vão nos ajudar muito no momento do desenvolvimento. Você vai ver quais são esses arquivos e bibliotecas do Django em [primeiros passos](docs/django/primeiros_passos.md).

### Frontend:
O Frontend é a nossa parte visual, onde vamos criar nossos desings e tudo mais. Aqui vamos utilizar React, e ficará fora do projeto Django, por esse exato motivo que para utilizar os modelos de dados do backend, vai ser preciso chamar via API REST disponível no projeto Django. 

## Stack

* Back-end: Django (Python), Django REST Framework e django_tenants.
* Front-end: React, HTML, CSS e JavaScript.
* Banco de dados: PostgreSQL com separação por schemas.
* Autenticação: Sessão Django + JWT.
* Conteinerização: Docker + Docker Compose.
* Infraestrutura: Digital Ocean.
* APIs Externas: Mercado Pago, Focus NF-e e Correios.

## Funcionalidade principais

* E-commerce completo com carrinho, checkout e rastreio de pedidos.
* ERP com gestão em vendas, estoque, produção, financeiro e clientes.
* Emissão automática de NF-e.
* Sistema de notificações e e-mails transacionais.
* Painel de métricas e dashboard por tenant. 

> Lembrando que esse projeto é apenas uma simulação, muitas dessas coisas precisam de uma pesquisa muito mais aprovunda para ter um bom desempenho, como as integração com APIs externas: emissão de notas fiscais que precisam estar regulamentadas com a Receita Federal, sistema de pagamento e de envio. 

## Status 

Este repositório é a versão demo pública, ele serve apenas como um protótipo do projeto real, para mostrar como foi feito e desenvolvido.

O projeto real se trata da empresa Bribatti Tech. Plataforma completa de e-commerce com ERP integrado, desenvolvida para pequenas e médias empresas que precisam de um site com gateway de pagamento, logística de entrega, e emissão de notas fiscais em um só lugar, junto com o sistema de gestão completo. 

## Deseja clonar esse repositório?



## Quer criar um projeto igual a esse para você?

Acesse já aos [Primeiros Passos!](docs/django/primeiros_passos.md)

## Quer visualizar como foi feita a modelagm de dados?

Acesse já aos documentos do ecommerce: 

[Descrição textual Detalhada do Ecommerce](docs/ecommerce/descricao/geral.md) - 
[Requisitos Funcionais do Ecommerce](docs/ecommerce/requisitos_funcionais/) - 
[Requisitos Não Funcionais do Ecommerce](docs/ecommerce/requisitos_n_funcionais/) -
[Modelagem de dados](docs/ecommerce/modelagem/)

Acesse já aos documentos do sistema de gestão:

[Descrição textual Detalhada do ERP](docs/erp/descricao/geral.md) - 
[Requisitos Funcionais do ERP](docs/erp/requisitos_funcionais/) - 
[Requisitos Não Funcionais do ERP](docs/erp/requisitos_n_funcionais/) - 
[Modelagem de dados](docs/erp/modelagem/)
