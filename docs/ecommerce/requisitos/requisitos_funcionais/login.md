# E-commerce 

Pode ser dito que a primeira coisa que é vista em e-commerces seria a sua página inicial, onde possui diversas subpastas. Os requisitos funcionais tem como objetivo descrever as funcionalidades que o sistema possui, neste caso vamos explicar por partes, começando pelo login, que é uma das partes mais importantes do e-commerce. 

## Login
Página de login e tudo que precisa estar configurado para que o usuário tenha uma boa experiência e que o sistema seja extremamente seguro e eficaz. Neste tópico iremos analisar somente a experiência do usuário, e descrever com precisão as funcionalidade. 

As questões relacionadas a segurança, escalabilidade, usabilidade, conformidade com as leis, e outras coisas relacionadas a esses tópicos. Serão vistas nos [requisitos não funcionais](../requisitos_n_funcionais/login.md)

### __ID:__ RF001 

__Descrição:__ O sistema deve autenticar usuários através de CPF e senha, validando as credenciais no banco de dados e iniciando uma sessão segura em caso de sucesso. 

__Racional:__ O CPF foi escolhido como identificador de login (em vez de e-mail) por ser um dado único e obrigatório no cadastro do cliente brasileiro, reduzindo ambiguidade de identidade e evitando duplicidade de contas por variações de e-mail. 

__Fonte:__ Decisão do projeto original (Bribatti Tech) e modelagem de dados do __*Usuário*__, onde CPF é definido como identificador único. 

__Prioridade:__ Essencial

__Dependências:__
- RF004 (opção "cadastre-se" visível na tela de login);
- RF010.1 (validação de formato do CPF);
- RNF002 (criptografia de senha no banco);

__Critério de aceitação:__
- Login com CPF e senhas corretos redireciona o usuário para o Perfil do Cliente em até 2 segundos (conforme, RFNF001).
- Login com CPF ou senha incorretos exibe a mensagem genérica "CPF ou senha inválidos", sem indicar qual dos dois campos está incorreto (requisito de segurança, evita enumeração de contas).
- A sessão criada deve ser registrada como segura (cookie/token válido), conforme padrão de autenticação do sistema. 

### __ID:__ RF002

