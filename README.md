#templates_ssr

Blog estático com Python!
---------------------------------------------------------------------------------------------------------------------------------------
Gerando páginas HTML para um blog usando o template do html estático e rendirizando dinâmicamente em tempo de real.

Efetuamos a renderização para entregar ao client o resultado do HTML.
O blog utiliza SQLITE como banco de dados, logo, utilizamos Python para conectar a um banco de dados, criar a tabela para armazenar as postagens e alimentar com alguns posts de exemplo.

O programa gera uma pasta site e podemos servir esta pasta com o servidor HTTP do Python.

Parte 1:
---------------------------------------------------------------------------------------------------------------------------------------
Todas as etapas para fazer a renderização das postagens que estão no banco de dados e preencher os templates HTML.

1) Buscamos os posts no banco de dados
2) Criamos a pasta site que será o destino do site final
3) Renderizamos a página index.html
4) Renderizamos uma página para cada post
5) Fechamos a conexão

Parte 2:
---------------------------------------------------------------------------------------------------------------------------------------

Construímos um formulário para a requisição POST e servimos ele usando o protocolo CGI Common Gateway Interface.

1) A tag <form> no html estrutura os campos que pretendemos receber no backend
2) O script em Python é executado pelo webserver que tem suporte a CGI
3) No script podemos capturar os valores do formulário
4) Neste ponto podemos fazer o que quiser, ex: enviar e-mail ou guardar em um banco de dados
5) Todos os prints que fazemos no CGI são retornados para o cliente, a saida padrão é impressa no stream de response.
