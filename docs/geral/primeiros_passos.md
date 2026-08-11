# Primeiros Passos do Django

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![DRF](https://img.shields.io/badge/DRF-3.16-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)
![Django Tenants](https://img.shields.io/badge/Django_Tenants-Multi--Tenant-success)
![Docker](https://img.shields.io/badge/Docker-Latest-2496ED)
![Git](https://img.shields.io/badge/Git-Latest-orange)

Neste arquivo vamos disponibilizar um tutorial prático e completo do Django do zero para iniciantes. 
## Como funciona o Django

O Django é um framework web de código aberto escrito em Python. Ele é usado por grandes sites pelo motivo de ser um framework full-stack, robusto, com sistemas integrados de:

* Autenticação;
* ORM (Object-Relational Mapping);
* Painel Administrativo;
* Segurança integrada;
* Django Rest Framework (DRF);

## Índice do Back-end: 
* 1° Passo: [Primeiros passos](#primeiros-passos-do-django);
* 2° Passo: [Configurar o Ambiente Virtual](#2-configurar-o-ambiente-virtual);
* 3° Passo: [Instalar as dependências](#3-instalar-as-dependências);
* 4° Passo: [Criar Projeto multi-tenant em Django](#4-criar-os-projetos-multi-tenant-no-django);
* 5° Passo: [Criar e configurar os apps modulares](#5-criar-e-configurar-os-apps-modulares);
* 6° Passo: [Arrumar as configurações](#6-arrumar-as-configurações-do-projeto-principal)
* 7° Passo: [Organizar os caminhos](#7-organizar-todos-os-caminhos);
* 8° Passo: [Criar um super usuário para acessar o painel admin](#8-criar-um-super-usuário-para-acessar-o-painel-do-admin);
* 9° Passo: [Explicar sobre boas práticas sobre git/branches](#9-explicar-boa-práticas-sobre-gitbranches);
* 10° Passo: [Primeiro Commit Local para salvar tudo no Github](#10-primeiro-commit-local-para-salvar-tudo-no-github);
* 11° Passo: [Criar os primeiros modelos de dados](#11-criar-os-primeiros-modelos-de-dados-modelspy);
* 12° Passo: [Realizar as migrações dos models](#12-realizar-as-migrações-dos-modelos-da-forma-correta-para-multi-tenant);
* 13° Passo: [Configurar o Docker](#13-configurar-o-docker);

## 1° Primeiros Passos:
Esse documento é para iniciantes, ou aqueles que desejam aprender sobre multi-tenants utilizando Django. Se você já tem conhecimento em Docker você pode pular os passos 2° e 3° e ir direto para o passo 13°, depois voltar para os tópicos 4° e sequência. 

Lembre-se que você tem completo poder de escolha, pode mudar os nomes das pastas e arquivos para o que você desejar, assim como também poderá mudar a estrutura, já que ela foi criada com base em pesquisas onde eu concluí que era a melhor opção para a minha plataforma original, porém existem diversas possibilidades com o Django. 

Você pode criar uma estrutura só com projetos e apps modulares, onde não precisa possuir uma API Core para compartilhar dados de um projeto para outro, essa forma condiz muito mais com a realidade daqueles que desejam utilizar esse projeto como base para criar um projeto para faculdade. É muito mais fácil e simples, os apps se comunicam entre si atráves de importações, inclusive os apps dos outros projetos. 

Se a ideia é criar um projeto acadêmico que possui CRUD, interface gráfica, integração com APIs externas, testes de integrações, e CI/CD. Eu suguri: O painel do admin do Django é perfeito para a criação de CRUD automático, você pode ver isso no [tópico 8°](#8-criar-um-super-usuário-para-acessar-o-painel-do-admin), e pode criar API REST como um sistema de avaliação, pode exportar APIs externas simples como VIACEP, a interface pode ser feita atráves de templates e static do Django (HTML/CSS/JS), testes de integrações em cada app, e utilizar YML para CI/CD.  


## 2° Configurar o Ambiente virtual:
O ambiente virtual (venv) serve para isolar o seu projeto Python dos outros projetos do sistema operacional, é como se fosse uma gaveta específica que você utiliza para trabalhar apenas com as ferramentas daquele projeto. Neste caso, vamos utilizar django então iremos [instalar todas as suas dependências](#instalar-as-dependências) e armazena-lás nesse ambiente virtual.

### Criar um ambiente virtual:

`python -m venv venv` 

### Ativar ambiente virtual:

**Windows**
`venv\Scripts\activate`

**Linux/MacOS**
`source venv/bin/activate`

??? Note "Nota!"

    Precisa ser ativado o venv antes de instalar qualquer dependência!

## 3° Instalar as dependências:
As dependências do seu projeto multi-tenant ficará armazenada de forma separada conforme o ambiente que você estiver programando. Assim terá uma pasta com o nome requirements e dentro dela os seus arquivos txt, sendo eles: 

!!! info inline end "Informação Adicional"

    Dentro de cada um desses arquivos deverá conter suas dependências, tais como: django, django-rest-framework, django-multi-tenant, etc. Você pode acessar o conteúdo que está dentro de cada um desses arquivos apertando o link que está sob ele.

- requirements/
    - [base.txt](../../backend/requirements/base.txt) 
    - [development.txt](../../backend/requirements/development.txt)
    - [production.txt](../../backend/requirements/production.txt)

Essa pasta será armazenada dentro do seu projeto, mas antes dele se criado você poderá deixar ela na pasta principal do seu repositório, como: saas-multi-tenant-demo. 

### Comandos para criar as dependênicas:

    Abra o seu terminal, e verifique se você está dentro da pasta mãe ex: saas-multi-tenant-demo/
Em seguida digite esses comando um por vez:

`mkdir requirements` - 
`touch base.txt` - 
`touch development.txt` - 
`touch production.txt`  

Copie e cole as mesmas dependências que estão nos arquivos (base.txt, etc) que você viu no tópico acima. 

`pip install -r requirements/base.txt` - 
`pip install -r requirements/development.txt` - 
`pip install -r requirements/production.txt`

Agora para listar e atualizar os seus arquivos, você pode usar o código abaixo:

`pip freeze > requirements/base.txt` -
`pip freeze > requirements/development.txt` - 
`pip freeze > requirements/production.txt`

Esse comando serve para listar todas as dependências instaladas no seu ambiente virtual e sobrescrever o arquivo com a versão atual de caad uma. 

> Esse processo de atualizar os arquivos do requirements deve ser feito sempre que for instalado uma nova dependência.  

## 4° Criar os projetos multi-tenant no Django:
Antes de sair criando diversos projetos sem necessidade, devemos entender primeiro a estrutura. Então temos nossa pasta principal que é a do nosso repositório, a segunda pasta principal já seria o nosso projeto principal. Neste caso é a pasta "backend", observe o exemplo a baixo. 

- saas-multi-tenant-demo/

- backend/
    - api-central/  
    - [config/](#6-arrumar-as-configurações-do-projeto-principal)
    
        !!! info inline end "Informação Adicional"
                
            Clique em cima do link para visualizar o que tem dentro desses arquivos.

    - [requirements/](#3-instalar-as-dependências)  
    - [apps-modulares/](#5-criar-e-configurar-os-apps-modulares)
    - middleware/
    - static/
    - tests/
    - utils/
    - venv/
    - .env
    - manage.py

- frontend/
    - arquivos do React

Pode observar que as outras pastas que possuem algum projeto dentro não estão dentro de backend e sim dentro da pasta mãe do nosso repositório. Já que queremos que a comunicação seja feita por API para ter mais escalabilidade futura no momento que for criar novos projetos, ao invés de importar os modelos de dados do projeto principal.

### Comandos para criar essa estrutura:
Abra o seu terminal, e verifique se você está dentro da pasta mãe ex: saas-multi-tenant-demo/
> Se não estiver na pasta mãe, utilize o comando: "`cd ..`" para voltar.

`mkdir backend` 

`cd backend` - Vai para a pasta que você acabou de criar.

`mkdir api` - 
`mkdir middleware` - 
`mkdir static` -
`mkdir tests` - 
`mkdir utils`

`django-admin startproject config .` - Criar o projeto django.

!!! Success "Sucesso!"

    Projeto em django com os arquivos settings, asgi , wsgi, urls, manage.py. Criado com sucesso!
    Vamos migrar o manage.py de config para backend de forma manual, arrastando para a pasta backend

`cd ..` - Voltar para a pasta mãe.

`mkdir frontend`

Todos os arquivos que estão dentro dessas novas pastas que foram criadas, você pode visualizar neste repositório.

## Para o que serve cada arquivo dentro do projeto Django?
Agora que você acabou de criar o seu projeto, eu vou te explicar o que são e para que serve essas pastas que foram criadas automaticamente e também explicar as pastas que a gente acabou de criar dentro do nosso projeto. 

- config/ - Projeto principal
    - __init__.py - Serve para dizer para o Django que esta pasta é um pacote python (pode ficar vazia sempre)
    - asgi.py - É um servidor assincrônico, é utilizado quando você deseja um chat em tempo real no e-commerce, ter notificações push, atualizações em tempo real, aqui ficam as aplicações que precisam de alta performance. 
    - settings/ - Pasta que criamos para armazenar os arquivos de configurações, será explicado com mais detalhes no tópico 6°. 
    - urls.py - Esse arquivo é o roteador principal do nosso proejto, será explicado com mais detalhes no tópico 7°.
    - wsgi.py - É padrão para servir aplicações Python na Web, ele será uma interface entre seu projeto e o servidor web. Normalmente é utilizado na produção, para realizar deploy para um local de hospedagem. 
    - api/ - Armazenar tudo que será compartilhado entre os projetos.
    - middleware/ - 
    - requirements/ - 
    - static/ - 
    - tests/ - Pasta para armazenar testes automatizados.
    - utils/ - 
    - venv/ - Nosso ambiente virtual que serve para isolar o nosso projeto Python dos outros projetos.
    - .env - Esse é o nosso arquivo secreto, onde não pode ser compartilhado em nenhum lugar, nele terá todos os dados sensíveis do nosso projeto, como senhas secretas, chaves de APIs, tokens, entre outros. Deve estar sempre dentro do seu arquivo .gitignore.
- manage.py - É o arquivo principal da nossa aplicação, pelo menos no ambiente de desenvolvimento, já que não utilizamos ele para produção. Ele é como um "assitente virtual" que executa os comandos do Django. No ambiente de produção utilizamos [Docker](#13-configurar-o-docker), ele automatiza esses comandos. 

## 5° Criar e configurar os apps modulares:
Os apps modulares são apps que podem conversar entre si de forma prática e fácil. Na nossa estrutura vamos separar esses apps para que não tenhamos um arquivo gigante responsável por toda a estrutura do app, por isso vamos criar pastas para organizar os apps, cada pasta terá uma função. 

- backend/ 
    - config/
        - apps/
            - modules/ - Aqui fica os apps comportilhados, onde todos os Tenants terão acesso, porém cada um terá acesso dentro do seu próprio schema
                - catalog/
                    - urls.py
                - inventory/
                    - urls.py

            - management/ - sistema de gestão, ou melhor, onde guarda todos os modelos do ERP
                - dashboard/

            - integrations/ - Aqui é onde irá ficar todas as integrações que iremos fazer para o nosso sistema
                - amazon/

            - shared/  - dentro dessa pasta ficará os nossos apps que serão schemas públicos, ou seja, 
                - core/
                - tenants/
                - users/

        - _init__.py
    - settings/
    - urls.py
- manage.py

Os apps modulares é um conjunto de apps dentro de um único projeto ou como nosso caso, dentro de uma única pasta por motivos de organização. Todos os nossos apps vão [redirecionar o seu caminho](#7-organizar-todos-os-caminhos) para a url principal que fica dentro no nosso projeto principal - config/

## Comandos para criar os apps modulares em Django:

`cd backend` - Ir para a pasta backend/

`mkdir apps` - Criar a pasta de apps modulares
 
`cd apps` - Ir para a pasta apps/

`mkdir modulos` - 
`mkdir management` - 
`mkdir integrations` - 
`mkdir shared` 

`cd modulos` - Ir para a pasta modulos

`mkdir catalog` - Criar a pasta que vai ficar o app dentro

`cd ..` - 
`cd ..` - Voltar para a pasta backend/ para digitar os comandos django

!!! Warning "Atenção!"

    Sempre que for realizar os comandos django, você precisa voltar para a pasta que possui o manage.py, que neste caso é backend/

`python manage.py startapp catalog apps/modules/catalog` - Criar o app

!!! Info "Informação"

    Por conta que estamos na pasta backend/ precisamos informar o caminho para chegar até a pasta do app. Porém normalmente se você quer criar um app na mesma pasta que possui o manage.py, você não precisa informar o caminho, somente "python manage.py startapp catalog" e pronto o mesmo já vai ser criado. 

Pode realizar os mesmos comandos só que alterando o nome do app de acordo com a pasta que você criou para ele.

Todos os apps precisam ser listados nas configurações e precisam de alguns ajustes em alguns arquivos especificos.

## Configurações dos apps:
Todos os apps precisam de alguns ajustes, eles sendo:
- apps.py - arrumar o caminho do app, normalmente está apenas com o nome do app, mas deve estar com o seu caminho, já que priorizamos a organização e criamos os nossos apps dentro de várias pastas.

>Caminho correto: (apps.modules.catalog) - Ajustar de acordo com o nome da pasta, e nome do aplicativo.


Exemplo:

- apps/
    - modules/
        - catalog/
            - apps.py 
            Dentro do arquivo:
            Ajustar isso: name = "catalog"
            Para isso: name = "apps.modules.catalog"

Isso deve ser feito com todos os apps, sem excessão. 

## Para que serve cada arquivo dos apps Django?
Vamos especificar para que serve cada arquivo do app, todos os que foram gerados automaticamente e outros que podemos criar caso faça sentido para a nossa aplicação.

- catalog/
    - admin.py - Aqui serão as configurações do painel do admin que o django cria automaticamente. Esse arquivo é utilizado para gerenciar os dados que foram adicionados, ou seja, você pode adicionar algum modelo que deseja possuir um CRUD (create, read, update, delete).

    !!! Example "Exemplo:"
        
        Se você deseja que o seu modelo de produto tenha a opção de cadastrar, visualizar, atualizar e deletar, você pode adicionar esse modelo no seu arquivo admin.py. 
    
    - apps.py - Define configurações específicas do app, conf. cache, ou verifica as dependências.
    - models.py - Onde ficará todos os seus modelos de dados, a estrutura das tabelas do banco de dados. Aqui você irá determinar os valores de cada atributo das entidades.
        
    !!! Example "Exemplo:"
        
        Vamos supor que você tenha um app chamado "Vida" e dentro dele possui o arquivo "models.py", dentro deste arquivo terá as entidades: orgaos, corpo, sentimentos, etc. Cada entidade possui os seus próprios atributos, ou seja, na entidade orgaos, terá os seguintes atributos: coracao, cerebro, pulmao, etc. Na entidade corpo, terá os seguintes atributos: braco, perna, pescoco, cabeca, orelha, boca, etc. E por último os atributos da entidade sentimentos: tristeza, alegria, raiva, medo, etc. Cada entidade terá o seu próprio valor, assim como também terá a sua própria lógica (que fica no arquivo views.py).

    - views.py - Onde fica a lógica do app, todos os sistemas possuem suas funcionalidades, e cada funcionalidade possui uma lógica. 
        
    !!! Example "Exemplo:"
        
        Seguindo o mesmo exemplo anterior, sobre o app chamado "Vida". A entidade orgaos possui o atributo coracao, onde ele possui uma funcionalidade para o app, que seria bombear o sangue para o corpo, onde corpo é um atributo de outra entidade. No arquivo views.py é onde a lógica do app é construída de acordo com suas necessidades e funcionalidades.

    -  urls.py - Esse é o caminho do seu app, onde define as rotas específicas do seu app. A views e a urls dentro do seu app sempre vão estar ligadas uma na outra, ou seja, todos os dados que você adicionar na views irá precisar configurar dentro da urls do seu app. 
    
    !!! Tip "Dica:"
        
        Todas as vezes que você adicionar um modelo novo no seu app, já adicione a sua lógica e seu caminho, para evitar perder tempo no futuro tentando adivinhar quais eram as funcionalidades daquele modelo que você já não se lembra mais.

!!! Example "Exemplo:"

    Para entender bem essa parte, vamos fazer uma pausa e ver como realmente funciona esse fluxo na vida real.
    Problema: Você criou um app de ecommerce e adicionou um produto com o id 123.
    
     1- O usuário se interessou por esse produto e apertou nele;
    
    2- O Django vai receber a solicitação para acessar um arquivo ( produto id 123), então ele vai acessar: meu_projeto/urls.py (vai acessar a URL principal do seu projeto);

    3 - Em seguida ele vai ser redirecionado para: `path(''. include('ecoomerce.urls'));

    4 - Com isso ele vai acessar as urls.py do seu app "ecommerce";

    5 - Nesta parte o Django vai procurar se existe a urls do produto para saber onde direcionar o usuário, ele precisa encontrar algo como: `path('produto/int:produto_id/', views.detalhes_produto)`. O Django vai acessar todos os produtos e todos os ids, por conta desta parte "path('produto/int:produto_id/". Então vamos supor que esteja assim em JSON: produto/111, produto/122, produto/123 e bingo ele achou o que estava procurando. Agora ele precisa seguir com a segunda parte "views.detalhes_produto", descobrir qual é a lógica que precisa ser acessada;

    6 - A lógica correta seria "detalhes_produto", que deverá ter algo parecido com isso: "views.detalhes_produto(request, produto_id=123)". Por último direcionar o usuário para essa lógica;


 Agora vamos seguir com os outros arquivos que o seu app pode possuir, e para que cada um deles serve.

- catalog/
    - serializer.py - Serve para criar APIs REST com base nos arquivos do models.py. Esse arquivo precisa instalar uma nova dependênica e configura-lá no setttings.py, essa dependência seria: Django REST Framework (DRF).
    - forms.py - É utilizada para organizar formulários da sua aplicação, eles também utilizam como base os arquivos models.py. Serve para receber dados de usuários de forma segura.
    -signals.py - Ele automatiza processos, mas deve ser utilizado com moderação, para eventualmente não travar a sua aplicação.
    - utils.py - Aqui você pode armazenar dados úteis que são utilizados em diferentes partes do seu projeto, mas que não pertence a models, views e forms. Enão com o utils você pode validar identidade de usuários, validar idade mínima, formatar telefone ou textos, pode também redimensionar imagens, calcular valor de frete ou calcular descontos. 
        
    !!! Tip "Dica:"
        
        Quando estiver adicionando a mesma informação em diferentes arquivos, mude para o arquivo utils e import ele nos arquivos que você estava utilizando. Isso vai facilitar e poupar tempo quando tiver adicionando de novo a mesma função.

    - permissions.py - Controle de acesso, definem o que cada um pode fazer, especialmente em API REST, para proteger endpoints.
    - filters.py - Utilizado para filtros de busca, ele é mais utilizado para APIs REST, já que ele cria parâmetros de URL automáticos.
    - constants.py - Armazena valores fixos que são usados em vários lugares diferentes do sistema, como valores fixos, configurações gerais (padrnonizar 20 produtos por página), mensagens padrões, configurações de email, ou caminhos de uploads.
    - managers.py - Cria consultas otimizadas para os seus models, adicionando um método especial no .object. Deixando apenas produtos ativos, produtos em promoção, mais vendidos, mais baratos, ou status do pedido (entregue, pendente, enviado). Ele é importado nos models e usados na view, sendo assim ele adiciona consultas personalizadas ou predefinidas.  

## 6° Arrumar as configurações do projeto principal:
As configurações do projeto principal se encontra somente dentro de um arquivo que se chama settings, porém como queremos escalabilidade, fácil manuteniabilidade, etc. Vamos separar esses arquivos em quatro partes, elas sendo: 

- backend/
    - config/
    - settings/
        - 1° parte: [base.py](../../backend/config/settings/base.py) 

            !!! info inline end "Informação Adicional"
                
                Clique em cima do link para visualizar o que tem dentro desses arquivos.

        - 2° parte: [development.py](../../backend/config/settings/development.py)
        - 3° parte: [production.py](../../backend/config/settings/production.py)
        - 4° parte: [test.py](../../backend/config/settings/test.py)
- .env

!!! Danger "Perigo!"

    Antes de você excluir e migrar para essa estrutura, você precisa anotar a senha secreta do seu projeto que está no seu settings.py, adiciona-lá no arquivo secreto .env, desta forma:

    `touch .env`

    Dentro do arquivo você digita:

    `SECRECT_KEY= senha secreta do settings`

    Lembrando que todos os dados sensíveis do seu projeto deve ficar armazenadas dentro do arquivo .env. E ele não pode ser compartilhado no Github de forma alguma, por isso você precisa criar um arquivo `.gitignore` e mencionar o .env dentro dele. 

    Na documentação original do [Django Tenants](https://django-tenants.readthedocs.io/en/latest/) você pode visualizar como deve ser feito, porque usar esquemas (schemas), como funcionam os aplicativos compartilhados (schemas_public), como instalar/configurar corretamente no seu projeto, entre várias outras coisas muito importantes para você aprender.

    Visualize os arquivos de configurações deste projeto, junto com a documentação oficial do Django tenants, e arrume suas configurações no mesmo padrão. 

## 7° Organizar todos os caminhos:
Os caminhos no django com apps modulares é um pouco complicado quando se vê pela primeira vez, mas ao decorrer do processo quando você passa a entender o fluxo, fica fácil de entender. Vamos começar explicando sobre o básico, o django possui uma URL principal e esse arquivo fica dentro do projeto django (config/urls.py), para conseguirmos exibir os dados dos nossos apps precisamos criar um arquivo `urls.py` dentro de cada app que a gente criar, e referenciar ele dentro do nosso arquivo urls.py principal.

- config/
    - apps-modulares/
        - modulos/
            - catalog/
                - [urls.py](../../backend/apps/modules/catalog/urls.py) 

            !!! info inline end "Informação Adicional"
                
                Clique em cima do link para visualizar o que tem dentro desses arquivos.

            - estoque/
                - [urls.py](../../backend/apps/modules/inventory/urls.py)
            - pagamento/
                - [urls.py](../../backend/apps/modules/payments/urls.py)
            - envio/
                - [urls.py](../../backend/apps/modules/shipping/urls.py)

- [urls.py](../../backend/config/urls.py)

## Comandos para criar os arquivos urls.py:
Você pode fazer isso de forma manual, apenas apertando em cima de cada app e adicionando um `New File`, em seguida `urls.py`. Ou você pode digitar os seguintes comandos dentro da pasta backend:

`cd catalog` - ir para o app que deseja

`touch urls.py` - criar o arquivo urls.py dentro do app catalog, deve se repitir isso em todos os outros apps. 

## 8° Criar um super usuário para acessar o Painel do Admin:
O painel do admin é criado pelo próprio Django, as coisas que aparecem dentro do admin é o que você adiciona dentro dos seus apps/admin.py. Neste caso, temos alguns apps principais e eles ficam dentro de shared, já que são o nosso schemas_public. Poderiamos configurar os arquivos admin.py dos outros apps também, caso tenha algum modelo que você deseje possuir um CRUD rápido, como por exemplo: Produto (apps/modules/catalog), para adicionar, ler, atualizar e excluir os produtos do sistema de forma rápida e fácil atráves do painel do admin.

- apps/
    - shared/

        !!! info inline end "Informação Adicional"
                
            Clique em cima do link para visualizar o que tem dentro desses arquivos.

        - tenants/
            - [admin.py](../../backend/apps/shared/tenants/admin.py)
    - modules/
        - catalog/
            - [admin.py](../../backend/apps/modules/catalog/admin.py)

## Comando para criar o super usuário no Django:
No terminal, dentro da pasta backend, rodar o seguinte comando:

`python manage.py createsuperuser`

Em seguida o terminal vai te pedir para adicionar um nome de usuário, um email e depois uma senha. Esse usuário e senha vai ser o que você irá utilizar para acessar o painel do admin. Para acessar o painel, é só adicionar o "admin" no seu http. Desta forma:

`http://127.0.0.1:8000/admin/`

## 9° Explicar boa práticas sobre Git/Branches:
Cada commit que você faz na sua aplicação fica visível, então se você realizar um commit com dados sensíveis (.env exposto) e tiver o repositório público, qualquer pessoa poderá visualizar esses dados sensíves, por isso é de extrema importância visualizar o que está sendo commitado antes de só sair dando push para o seu repositório. 
Provavelmente você está construíndo essa aplicação sozinho e deve achar que pode commitar de qualquer jeito já que só você terá acesso, mas quando você entende que existe um padrão correto para isso e que muitas empresas utilizam. Com isso podemos dizer que é melhor você segui-lós até mesmo quando está trabalhando sozinho, porque isso ajuda você a entender o que cada commit fez ou corrigiu. 

As Branches permitem criar linhas de desenvolvimento paralelas e independentes dentro de um mesmo repositório. 

## O que são Branches?

Um Branch ou ramo em português, é essencialmente um ponteiro móvel para um commit específico, ou seja, quando você cria uma brach você está criando uma nova linha de desenvolvimento que deverge do ponto atual. Isso permite trabalhar em diferentes funcionalidade ou testes sem afetar o código principal, que é armazenado na branch principal, a branch main/master. Nenhum código com erros ou sem ter feitos os devidos testes podem ir para a branch principal, e é por isso que existem outras branches. 

## Como utilizar as Branches?
* A branch principal: Geralmente é chamada de main ou master, contém o código estável, sem erros. Essa branch que mantém o site/app funcionando independente se está sendo desenvolvido outras funcionalidades, enquanto não encaminhar as alterações para a main, ela continuará igual;
* Branch de development: A branch de desenvolvimento é utilizada em casos de sites maiores ou que precisam de uma estabilidade maior, onde é feito a integração das novas funcionalidades, para ter certeza que o código está apto para ir para a branch main;
* Branch feature: Essa é branch das novas funcionalidades, por exemplo, quero criar um ecommerce vou começar pela página inicial, ai você cria uma branch de feature/pagina-inicial, se quiser adicionar campo de produtos dentro desse e-commerce, terá que criar uma nova feature/produtos, e assim por diante, todas as novas funcionalidades sejam elas quais forem, terão que ser registradas em uma branch feature;
* Branch bugfix: Essa branch é utilizada para correção de erros específicos, para ficar registrado o que você teve que mexer para arrumar esse erro, e também serve para identificar de onde veio esse erro;
* Branch hotfix: Aqui são registrados os problemas urgentes, que precisam ser corrigidos o quanto antes, poderia ter utilizado a branch acima, porém isso serve para saber quantas vezes tiveram problemas críticos e urgentes no projeto, para saber o que deve ser feito a respeito disso;
* Branch refactor: Essa branches servem para deixar registrado as melhorias, seja no estilo do botão, em algum documento, ou deixou o código mais limpo, mas sem de fato alterar o código, tudo isso é registrado na branch refactor;

!!! abstract "Resumo"

    As mudanças em uma branch em específico não altera nenhuma outra, assim podem ser feitos testes sem quebrar o código principal. Quando está trabalhando em equipe esse é um ótimo método, porque diferentes pessoas podem trabalhar em funcionalidades diferentes no projeto de forma simultânea. Além de ter uma branch para cada funcionalidade permite uma organização mais eficiente, também gera um entendimento mais claro do projeto para quem entrar nele depois do projeto já ter começado, simplesmente analisando os commits e o que foi feito.

Conventional Commits é uma especificação para padronizar mensagens de commit, facilitando a leitura do histórico e automatização de processos.
Exemplo: `git commit -m "feat: Criação da página inicial"`

## Como e quando utilizar cada Conventional Commit?
* feat: nova funcionalidade para o usuário, serve para quando você adicionar algo novo que o usuário final possa usar;
* fix: correção de bugs, resolve os problemas existentes no código;
* hotfix: Correção urgente em produção, somente as correções emergenciais que não podem esperar a nova atualização do development;
refactor: Mudança no código que não adiciona funcionalidade nem corrige bugs, servem para melhorar a qualidade do código sem alterar de fato o código;
* perf: Aqui são as mudanças que melhoram a performance, mas focado em velocidade e eficiência;
* style: Mudança na formatação, como espaços, vírgulas, ou mudar o estilo do css, ou javascript, ou seja, alterações que não afetam o significado do código;
* docs: Mudanças apenas na documentação; 
* test: Adicionar testes ou modificar testes;
* chore: Pode parecer que aqui vai ser registrado o fim, mas não é (piada a parte), aqui são registrada as mudanças em ferramentas, configurações ou dependências;
* build: Mudanças no sistema de build ou dependências externas;
* ci: Mudanças nos arquivos de CI/CD (integração contínua/entrega contínua), esse tópico vai ser explicado futuramente, porque é muito útil para o Django, são os arquivos do actions os workflows;
* revert: Quando você fizer um commit e por algum motivo não era isso que você queria fazer, pode usar o revert para reverter o commit anterior;

!!! Note "Observação"

    Pode usar parênteses para especificar ainda mais o que você acabou de fazer.

    !!! Example "Exemplo:"

        fix(api): corrigir validação de email da API REST

## Por que utilizar esse método de commit e de Branches?
Isso vai facilitar o entendimento do histórico de commits, sabendo exatamente qual commit que acabou resultando em erro no projeto, o time todo segue o mesmo padrão e todo mundo vai se entender de uma maneira muito mais fácil. A ideia é que cada commit tenha um propósito claro e seja facilmente identificável, isso torna o histórico do projeto muito mais legível e permite automatizar processos. 

## 10° Primeiro commit local para salvar tudo no Github:
Esse é o passo onde você respira de alívio por finalmente ter tudo salvo no Github e sabe que não precisa mais se preocupar. Eu aposto que você deve ter mais de 400 alterações te implorando para realizar um commit, porém a gente vai fazer mais do que isso, seguindo as boas práticas que vimos anteriormente, vamos realizar vários commits conforme o que foi realizado. 

Alguns exemplos seriam: Criar uma feature para registrar os apps do backend, e selecionar todos os arquivos que se encaixam nessa feature. 

!!! Note "Observação"
 
    Os commits servem para organização do projeto pelo Github, ou seja, é recomendado que todas as alterações que você faz no ambiente virtual, deve conter um commit detalhando o que foi feito e por quê. 

## Comandos para fazer o primeiro commit:
Dentro da pasta principal do seu repositório (estar fora da sua pasta do seu projeto). Exemplo: saas-multi-tenant-demo/

`cd ..` - Comando para voltar uma casa, serve para mudar o caminho.

`git init` - Esse comando serve para inicializar o seu repositótio do Github e organizar ele.

!!! info inline end "Informação Adicional"

    Você precisa ter criado um repositório no Github com o mesmo nome da sua pasta principal, neste caso: saas-multi-tenant-demo. Esse repositório deve ficar vázio, para conseguir levar tudo que acabamos de criar pra lá. 

`git branch` - Esse comando serve para você visualizar em qual branch você está.

`git branch development` - Esse comando serve para criar a branch development.

`git checkout -b feature/apps_backend` - Esse comando serve para criar uma branch de feature (funcionalidade) com o objetivo de registrar todos os apps do backend.

`git add .` - Esse comando serve para adicionar tudo que você fez até agora, mas como a gente quer adicionar somente os arquvios dos apps do backend, vamos utilizar os comandos a seguir.

`git add backend/apps/modules backend/apps/integrations backend/apps/management backend/apps/shared` 

`git status` - Comando para visualizar quais dados serão commitados, aqui você também pode aproveitar para ver se não vai commitar o .env sem querer. 

`git restore --staged` - Comando que retira da lista do commit, o arquivo continua com as alterações, mas não irá constar mais no commit atual.

`git commit -m "feat: Adicionando os apps do backend, com toda a sua estrutura padrão configurada` - Realizando o commit, tudo que você escrever aqui vai ficar salvo, então quanto mais claro e objetivo você for no seu commit é melhor. 

`git push origin feature/apps_backend` - Comando para enviar os dados que você acabou de commitar para o Gihub.

`git checkout development` - Voltando para a branch development.

Aqui é o momento no qual você pode ou adicionar mais commits, ou já mandar esses para a branch development. Se desejar adicionar mais, você pode fazer todo o processo de criar um nova branch feature com o que deseja, e seguir os passos seguintes tudo novamente. Se desejar prosseguir, siga os passoa a seguir:

`git merge feature/apps_backend` - o comando merge serve para combinar o conteúdo de uma branch para outra, com isso agora você sabe que as branchs não estão sincronizadas e precisa ser feito merge para adicionar as suas alterações para a branch desejada. Exemplo: como é seu primeiro commit a suas alterações são na realidade a estrutura do django que você acabou de criar, então pode jogar na branch principal (main), mas quando são coisas que precisam ser passadas por um teste ou uma verificação antes, precisa ser passado para a branch development antes, por motivos de segurança, para não quebrar o código na branch principal.

`git push origin development` - Comando que manda os dados que você acabou de receber da merge para o Github.

> Também tem a opção de fazer uma merge via Pull Request no GitHub, é mais comum em projetos colaborativos.

`git log --oneline` - Comando para verificar o histórico resumido, serve para visualizar todos os commits já realizados. 

## 11° Criar os primeiros modelos de dados (models.py):
Os modelos de dados é uma das partes mais importantes da nossa aplicação, já que com ele podemos levá-la para outro nível. Seria interessante realizar uma modelagem de dados antes de sair criando models, porque o Django possui ORM, mas ela não garante que tudo ocorra bem se você esqucer de alguma coisa.

!!! Info inline end "Informação Adicional"

    Clique em cima do link para visualizar o que tem dentro desses arquivos.

- modules/
    - catalog/
        - [models.py](../../backend/apps/modules/catalog/models.py) - 
        Arquivos onde os modelos de dados ficarão dentro 


Acredito que a parte de levantamento de requisitos é uma parte muito importante quando se trata de criar um sistema do zero, ela serve para armazenar suas ideias, entender a lógica do negócio, e principalmente manter a organização no momento do desenvolvimento. 
É por isso que eu fiz questão de deixar uma pasta reservada somente para isso neste projeto, a pasta "doc/" possui duas outras subpastas "ecommerce/" e "erp/", ambas são para descrever os requisitos funcionais e não funcionais de um SaaS. 
Fora isso ainda possui a descrição textual de cada uma, onde tem o foco em ajudar no momento da criação da modelagem de dados, e entender os relacionamentos e o tipo daquela tabela. O que é muito importante para a ORM do Django. 

- [docs/](../../docs/)
    - ecommerce/
        - descricao/ - Descrição textual 
            - geral.md
        - requisitos_funcionais/ - Requisitos funcionais do sistema 

        !!! Info inline end "Informação Adicional"

            Clique em cima do link para visualizar o que tem dentro desses arquivos.

        - [login.md](../../docs/ecommerce/requisitos_funcionais/login.md) 
            - cadastro.md
        - requisitos_n_funcionais/ - Requisitos não funcionais 
            - login.md
            - cadastro.md
            - segurança.md 

    - erp/
        - descricao/ 
            - geral.md
        - requisitos_funcionais/
            - login.md
            - dashboard.md
        - requisitos_n_funcionais/
            - nível_acesso.md
            - desempenho.md
        

Você pode visualizar dentro dos apps em `models.py` o que possui dentro, está tudo comentado, então é de fácil entendimento.

- modules/
    - catalog/
        - [models.py](../../backend/apps/modules/catalog/models.py)


O recomendado é você ler a documentação, ou até mesmo criar uma que condiz mais com a sua ideia do que deseja fazer, e desenvolver os seus próprios modelos de dados. A modelagem é indispensável neste projeto, por ele se tratar de uma plataforma SaaS, onde realmente precisa de muita constância, já que uma coisa errada ou faltante, pode gerar em erros desnecessários o que resulta em perdas de horas de desenvolvimento. 

## 12° Realizar as migrações dos modelos da forma correta para multi-tenant:
A forma como você realizar as migrações dos seus modelos, tanto modelos públicos como modelos modelos compartilhados, vai dizer se realmente vai existir separação de dados entre tenants ou se os dados não estão extremamente seguros. A nossa abordagem desse projeto é criar um SaaS, onde cada empresa possui os seus próprios dados e as outras empresas cadastradas nesse SaaS não podem acessar os dados de terceiros, para isso acontecer precisa ser feita uma boa separação, e isso começa no momento das migrações dos modelos, que devem seguir alguma regras. 

`python manage.py makemigrations` - 

`python manage.py showmigrations` - Mostrar status das migrações

Migrar os schemas públicos antes dos que podem ser compartilhados entre tenants. Cada empresa terá o seu próprio schema mas também utilizará os mesmos modelos de dados que as outras empresa. Então todos os apps que estão em "shared" são os modelos públicos e os que estão em "modules, management, e integrations" são modelos compartilhados, cada um vai ter o seu, mas todos terão os mesmo modelos. 

!!! Example "Exemplo:"

    - apps/
        - modules/
        - catalog/
    - integrations/
        - tiktok/
    - management/
        - erp/
    - shared/
        - tenant/
        - Ex: Tenant "Moda"
        - Tenant "Móveis"

    
A empresa "Moda" irá possuir o modelo que está dentro de catalog, a integração com o tik tok se a acaso desejar, e acesso ao erp. Entretanto ela terá o seu próprio schema, domínio, email corporativo, etc. Assim como a empresa "Móveis", ele também terá acesso a todos esses modelos, mas ele não irá ter acesso aos dados dos modelos da empresa Moda, porque cada um pertence a um schema diferente. 

- database
    - schemas(3)
        - Moda
            - catalog
            - inventory
            - orders
            - etc...
        - Móveis
            - catalog
            - inventory
            - orders 
            - etc...
        - public
            - plano
            - domínio
            - empresa
            - usuario
            - etc...

Todas as empresas tem o seu próprio schemas mas utilizam os mesmos modelos, mas não possuem acesso aos dados de outras empresas. Neste exemplo acima podemos ver que cada empresa possui as mesmas tabelas de dados (catalog, inventory, orders, etc), isso se dá por causa que configuramos dessa maneira lá em [settings](#6-arrumar-as-configurações-do-projeto-principal). Todas as empresas possui um plano, domínio, usuários, etc e isso é único para cada uma delas, uma empresa não pode ter o mesmo domínio e nome que outra empresa, e por ai vai.

Comandos para migrar somente os dados públicos primeiro, já que não pode migrar tudo de uma vez só, precisa ser primeiro os schemas público, o restante será migrado automáticamente no momento em que você criar um Tenant. O django possui um modelo que gera Tenant e com ele migra os modelos de dados configurados automaticamente.   

`python manage.py migrate_schemas users --shared` - 

`python manage.py migrate_schemas tenants --shared` - 

`python manage.py migrate_schemas admin --shared` - 

`python manage.py migrate_schemas contenttypes --shared` - 

`python manage.py migrate_schemas auth --shared` - 

`python manage.py migrate_schemas sessions --shared` - 

Se você realizou corretamente os outros tópicos e prestou atenção, vai notar que esses são exatamente alguma das aplicações que estão dentro de "SHARED APP" em [settings](../../backend/config/settings/base.py). 

    SHARED_APPS = [ 
        'django_tenants', 

        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.admin',
        'django.contrib.staticfiles',
        'django.contrib.sites',  

        'apps.shared.core',
        'apps.shared.tenants',
        'apps.shared.users',
    ]

!!! Failure "Cuidado, perigo de Falha!"

    Não utilizamos o comando `python manage.py migrate`, porque ele realiza a migração de todos os modelos de dados de uma vez, e não é isso que queremos. Primeiro é o schema_public e só depois quando o tenant for criado que os outros modelos vão ser migrados. 

## 13° Configurar o Docker:
O Docker é uma plataforma aberta para desenvolver, lançar e executar aplicações. O Docker permite separar suas aplicações da infraestrutura para que você possa entregar software rapidamente. Com ele você pode gerenciar sua infraestrutura da mesnma forma que você gerencia suas aplicações. 

Algumas empresas de hospedagem de site web, realiza o deploy da sua aplicação utilizando arquivos Docker e Ngnix. Então ter esses arquivos instalados e configurados no seu projeto desde o ínicio podem facilitar tanto o seu desenvolvimento quanto para o momento de deploy em produção. 

Os container do Docker, ele informa todos os dados do seu site em Django, então todos os projetos e apps que foram cirados ele armazena nesse container, assim como o banco de dados, as dependências e o arquivo Ngnix. 

!!! Note "Observação"

    O Docker serve para facilitar a vida de novos desenvolvedores, ao invés deles instalaram as dependências necessárias, ativar o ambiente virtual e instalar os pacotes necessários para trabalhar naquela aplicação. Ele só precisa instalar o Docker e rodar o comando do docker para baixar todas as dependências e configurações que o projeto precisa para funcionar normalmente.

Utilizar os containers possui diversas vantagens para o seu projeto, até mesmo se for um projeto simples para a faculdade, porque isso garante que o seu código rode em todos os servidores. Sem perigo de rodar na sua máquina mas não rodar na máquina da faculdade ou do colega, porque o Docker faz o sistema rodar nele e não na sua IDE, como o VsCode por exemplo. 

Deixar o Django rodando o seu código é ótimo para processar lógica Python, mas péssimo para servir arquivos estáticos, como CSS, JS, imagens. Utilizar o Nginx para fazer isso é extremamente eficiente, ele analisa todas as requisições e decide onde enviar, então ele serve mais rápido arquivos esses arquivos estáticos. Fazendo a distribuição desses arquivos de uma forma muito superior se fosse deixar o Django fazendo isso. 

!!! Info "Informação"

    O Nginx também gerencia certificados, criptografia, reduz o tamanho dos arquivos enviados, guarda respostas para não processar de novo e sabe lidar com milhares de conexões simultâneas. 

Ter apenas uma pasta de Docker na pasta mestre não seria uma boa ideia se você não quer que seus projetos fiquem dependentes um do outro. Quando um falha, os dois vão estar falhando ou com algum problema relacionado. 
Se um projeto tiver mais tráfego que o outro, você só irá precisar atualizar ele, se algum bug ou ataque acontecer no site oficial, não irá afetar o site de gestão. Os dois projetos vão ser totalmente independentes e poderão ter os seus próprios domínios em servidores diferentes. 

Então dentro do nosso projeto Backend vamos ter uma pasta focada para o Docker, com o docker-compose.yml, o Dockerfile e .dockerignore. Assim será feito nos outros projetos também. 

- backend/
    - [docker/](../../backend/docker/)
        - [Dockerfile](../../backend/docker/Dockerfile) - "Receita para construir a imagem Docker"
        - [docker-compose-backend.yml](../../backend/docker/docker-compose-backend.yml) - Orquestra múltiplos containers 
        - .dockerignore - Ignora os dados sensíveis do Docker
- frontend/ 
    - docker/
        - Dockerfile
        - docker-compose-frontend.yml
        - .dockerignore

## Comandos básicos do Docker: 
'FROM', 'RUN', 'COPY'. São utilizados para criar camadas, já que o Docker reutiliza camadas que não mudaram (cache).

Layer 1: FROM python:3.11-slim 
Layer 2: ENV variáveis
Layer 3: RUN apt-get install 
Layer 4: COPY requirements  //  Se mudar aqui, refaz daqui pra baixo
Layer 5: RUN pip install 
Layer 6:COPY código  //  Se mudar código, só refaz daqui pra baixo

## Imagem do Docker
Uma imagem Docker é um arquivo imutável e reutilizável que contém tudo o que é necessário para executar uma aplicação. Ela serve como um modelo somente leitura que inclui o sistema operacional, bibliotecas, dependências, código-fonte e configurações necessárias para criar um container. 
As imagens são criadas a partir de um Dockerfile, que é um arquivo de texto contendo instruções para conseguir a imagem. Cada instrução no Dockerfile gera uma camada na imagem, tornando-a eficiente e reutilizável. Por exemplo, se várias imagens compartilham a mesma base (como ubuntu), elas podem reutilizar essas camadas. 
As imagens são armazenadas em registros, como o Docker Hub, que funciona como um repositório público ou privado. Para utilizá-la, você pode baixá-la com o comando docker pull e instanciar containers com docker run. Por exemplo: 

!!! Quote "Citação"

    As cinco etapas mais importantes no desenvolvimento de um sistema: 
    Analisar + Desenvolver + Implantação + Testes + Implementação.

