![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
<img src="https://komarev.com/ghpvc/?username=deh0&label=%20Views&color=0e75b6&style=flat" alt="deh0">

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
<img src="https://komarev.com/ghpvc/?username=deh0&label=%20Views&color=0e75b6&style=flat" alt="deh0">

# Plataforma SaaS Multi-Tenant Demo

Este repositório tem como intuito ajudar aqueles que querem aprender sobre Django multi-tenant e desejam criar o sua própria plataforma SaaS sozinho, ou em equipe. Aqui vamos descrever desde os primeiros passos, até decisões de negócio, boas práticas, levantamento dos requisitos do sistema, modelagem de dados, testes e deploy. O projeto é uma versão reduzida do projeto original, ou seja, algumas coisas vão precisar de mais pesquisas por fora do que o restante (será sinalizado quando necessário). 

### Para quem esse projeto foi feito?

* Desenvolvedores Python que desejam aprender Django.
* Desenvolvedores que desejam criar um SaaS real.
* Desenvolvedores Front-end que desejam integrar React com uma API.
* Analistas de Dados interessados em modelagem de banco de dados.
* Engenheiros de Requisitos que desejam visualizar um projeto completo.
* Empresas que desejam estudar decisões arquiteturais.

## Descritivo sobre o projeto
<!-- deixar com um tom mais profissional, falar com os estudantes no "guia para estudantes" -->

Neste repositório vamos desenvolver um Saas que vende planos de sites com sistema de gestão integrado, então vamos desenvolver um e-commerce e um ERP completo e com todas as suas funcionaliaddes, você pode utilizar esse projeto para conseguir uma renda extra, ou para conseguir experiência em um projeto real que realmente vende. Falando em vendas, imagina ficar alguns meses desenvolvendo um projeto nesta complexidade e vender apenas para uma empresa, não é isso que nós queremos! Queremos vender para muitas empresas, e administrar isso em um só lugar. 

Então vamos utilizar o Django, já que o mesmo possuí vários recursos que vão nós ajudar no desenvolvimento, escolhemos ele exatamente por esse motivo, para ser mais fácil e prático. O Django não deixa de ser difícil ou complicado para iniciantes ou para quem nunca pesquisou sobre ele, mas fique tranquilo neste projeto tudo será explicado e justificado para que você possa ter autonomia para escolher o que de fato você quer fazer no seu próprio projeto, ele pode servir apenas como um guia, para te mostrar todos os caminhos e para onde cada um pode levar.

O Django Tenants, permite você ter mútliplos inquilínos com base em schemas diferentes no PostgreSQL. Eles podem utilizar os mesmos modelos de dados, mas cada um vai possuir o seu próprio "esquema", ou seja, você vai possui um Saas que vende um e-commerce e um ERP, ambos tem dados fixos, como catalogo de produtos, carrinho, checkout de compras, gerenciamento de estoque, gerenciamento de pedidos,e etc. Todas as empresa que contratarem o seu serviço vai precisar ter esses mesmos modelos de dados, então a lógica é todas utilizarem os mesmos modelos mas não possuírem acesso aos dados uma das outras. 

E é ai que entra os schemas diferentes, se cada empresa possuir o seu próprio esquema no banco de dados, as suas tabelas (modelos) ficaram armazenadas somente no seu esquemas e outra empresa não irá poder acessá-lo. Isso permite que cada empresa suas próprias configurações, até porque uma empresa pode ter mais modelos que a outra, vice versa, assim como garante mais segurança e independência entre as empresa e até mesmo para o seu próprio projeto. 

[Clique neste link para acessar a documentação oficial do Django-Tenants!](https://django-tenants.readthedocs.io/en/latest/install.html#)

Como esse projeto que eu desenvolvi é focado para analises e desenvolvimento real, 

### Objetivos do Projeto

- Aplicar Engenharia de Requisitos
- Aplicar UML
- Aplicar Modelagem de Dados
- Construir uma arquitetura SaaS Multi-Tenant
- Desenvolver APIs REST com Django
- Integrar Frontend React/Next.js
- Demonstrar práticas de deploy e documentação

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

### Metodologias Utilizadas:

1. Descrição Textual
2. Casos de Uso
3. Requisitos Funcionais
4. Requisitos Não Funcionais
5. Diagramas UML
6. Modelo Conceitual
7. Modelo Lógico
8. Implementação Django
9. APIs REST
10. Frontend React


## Funcionalidade principais

* E-commerce completo com carrinho, checkout e rastreio de pedidos.
* ERP com gestão em vendas, estoque, produção, financeiro e clientes.
* Emissão automática de NF-e.
* Sistema de notificações e e-mails transacionais.
* Painel de métricas e dashboard por tenant. 

!!! Note "Observação"

    Lembrando que esse projeto é apenas uma simulação, muitas dessas coisas precisam de uma pesquisa muito mais aprovunda para ter um bom desempenho, como as integração com APIs externas: emissão de notas fiscais que precisam estar regulamentadas com a Receita Federal, sistema de pagamento e de envio. 

## Status 

Este repositório é a versão demo pública, ele serve apenas como um protótipo do projeto real, para mostrar como foi feito e desenvolvido.

O projeto real se trata da empresa Bribatti Tech. Plataforma completa de e-commerce com ERP integrado, desenvolvida para pequenas e médias empresas que precisam de um site com gateway de pagamento, logística de entrega, e emissão de notas fiscais em um só lugar, junto com o sistema de gestão completo. Pode acessar mais informações no site oficial da empresa: [bribatti.com.br](https://bribatti.com.br/)

## Deseja clonar esse repositório?

## Quer criar um projeto igual a esse para você?

Acesse já aos [Primeiros Passos](docs/django/primeiros_passos.md) ou [Guia do Estudante](docs/geral/guia_estudante.md)!

# Quer visualizar toda documentação e descobrir como tudo foi feito?

Acesse já aos descritivos que explicam o sistema, na ordem recomendada: 

---------
[Descritivo sobre Descrição Textual](docs/geral/descricao_textual_geral.md) - 

----------
[Descitivo sobre Casos de Uso](docs/geral/caso_de_uso.md) - Serve para exibir o que o autor quer fazer, qual é o fluxo

----------
[Descritivo sobre Requisitos do Sistema](docs/geral/requisitos_geral.md) - Se você tem interesse em analisar e aprender como realizar o levantamento dos requisitos de um sistema, e descobrir para o quê ele serve. Esse é o tópico perfeito.  

----------
[Descritivo sobre Diagramas do Sistema](docs/geral/diagramacao.md) - A Diagramação é uma parte muito importante, é onde conseguimos visualizar o fluxo, entender as regras de negócio de uma forma mais clara e objetiva. Então se deseja saber como ele é utilizada atualmente, esse tópico pode te interessar. 

----------
[Descritivo sobre Modelagem de Dados](docs/geral/modelagem.md) - Esse tópico que explica sobre modelagem de dados, ensina e demonstra na prática como é utilizada, se deseja saber mais informações, esse tópico é perfeito para você. 

### Documentação do E-commerce:

Acesse já aos documentos com conteúdo prático do e-commerce, na ordem recomendada: 

---------
[Descrição Textual Detalhada do E-commerce](docs/ecommerce/descricao/) - Resumo dos requisitos do sistema, explicação sobre a descrição textual, e demonstração prática de acordo com as funcionalidades do sistema. Se te interessa, aprte no link azul.

----------
[Requisitos Funcionais do Ecommerce](docs/ecommerce/requisitos_funcionais/) - Pasta com todos os requisitos funcionais do sistema, tendo todos os seus relacionamentos, restrições, casos de uso, etc. Se esse tópico te interessa, aperte no link azul. 

----------
[Requisitos Não Funcionais do Ecommerce](docs/ecommerce/requisitos_n_funcionais/) - Os requisitos não funcionais são tão importante quanto os funcionais, eles garantem segurança, usabilidade, escalabilidade, entre outros ao sistema.  Aperte no link azul para ver mais detalhes. 

----------
[Diagrama do E-commerce](docs/ecommerce/diagramas/atividade/) - Pasta com todos os diagramas, sendo eles de Classe, Atividade e Sequência. Todos foram separados de acordo com os módulos dos requisitos listados anteriormente. Se esse assunto te interessa, esse tópico é para você. 

----------
[Modelagem de dados](docs/ecommerce/modelagem/) - A modelagem de dados é responsável por nós dar garantia e segurança, que a [ORM]() do Django sozinha não é capaz. Esse tópico ajuda na criação dos modelos para o banco de dados, que é a chave principal para o nosso projeto. Se te interessa, aperte o link azul. 

### Documentação do Sistema de Gestão: 

Acesse já aos documentos com conteúdo prático do sistema de gestão, na ordem recomendada: 

[Descrição Textual Detalhada do ERP](docs/erp/descricao/) - 

---------
[Requisitos Funcionais do ERP](docs/erp/requisitos/requisitos_funcionais/) -

---------
[Requisitos Não Funcionais do ERP](docs/erp/requisitos/requisitos_n_funcionais/) - 

---------
[Diagramas do Sistema de Gestão](docs/erp/diagramas/) -

---------
[Modelagem de Dados](docs/erp/modelagem/) - 


