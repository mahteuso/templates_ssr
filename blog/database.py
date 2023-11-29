# 1 - Conectar com o banco de dados
from sqlite3 import connect


conn = connect("blog.db")
cursor = conn.cursor()

# 2 - Definir e criar a table caso ela não exista

conn.execute(
    """\
    CREATE TABLE IF NOT EXISTS post(
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );    
    """
)

# 3 - Criar os posts iniciais para alimentar o banco de dados

posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
        A linguem Python foi eleita a linguagem mais popular pela revista
        tech masters e segue dominando o mundo.
        """,
        "author": "Satoshi Namamoto",
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": """\
        Neste tutorial você aprenderá como criar um blog utilizando Python.
        <pre> import make_a_blog </pre>
        """,
        "author": "Guido Van Rossum",
    },
]

# 4 - Inserir os posts caso o banco de dados esteja vazio

count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author)    
        """,
        posts,
    )
    conn.commit()

    # 5 - Verificar se os dados foram inseridos

    posts = cursor.execute("SELECT * FROM post;")
    assert len(posts) >= 2
