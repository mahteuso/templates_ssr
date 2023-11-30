#templates_ssr

Blog dinâmico com Jinja2!
---------------------------------------------------------------------------------------------------------------------------------------
Um dos template engines mais famosos e utilizados chama-se Jinja2, ele virou um padrão para templates que é inclusive seguido fora da web como por exemplo no Ansible (ferramenta de automação de infra estrutura e configurações da Red Hat), o Jinja também inspirou o Twig do PHP, o Tera do Rust, entre outros.


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

Construímos um formulário para a requisição POST utilizando Macros. Uma das vantagens de usar Jinja é possibilidade de reaproveitar código HTML através de macros, que são funções definidas dentro do HTML.
---------------------------------------------------------------------------------------------------------------------------------------

Detalhes:

Ao trabalhar com templates estabelecemos um limite sobre o que é lógica de apresentação e o que é lógica de negócio. Ex: Iterar objetos, transformar para maiusculo, adicionar opções de formatação etc, são ok de ir ao lado HTML. No caso da filtragem, ordenação, permissões etc, foram feitas no nível de função ao invés de ser feito no template.

