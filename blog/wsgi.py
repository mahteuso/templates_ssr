import cgi
from database import conn

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("templates"))


    
def get_post_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]

def render_template(template_name, **context):
    template = env.get_template(template_name)
    return template.render(**context).encode("utf-8")


def add_new_post(post):
    cursor = conn.cursor()
    cursor.execute(
        """\
            INSERT INTO post (title, content, author)
            VALUES (:title, :content, :author)
        """,
        post,
    )
    conn.commit()

def application(environ, start_reponse):
    body = b"Content Not Found"
    status = "404 Not Found"
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]

    # roteamento de URL's
    if path == "/" and method == "GET":
        posts = get_post_from_database()
        body = render_template(
            "list.template.html", post_list=posts
        )
        print()
        status = "200 ok"

    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html",
            post=get_post_from_database(post_id=post_id)[0],
        )
        status = "200 ok"

    elif path == "/new" and method == "GET":
        body = render_template("form.template.html")
        status = "200 ok"

    elif path == "/new" and method == "POST":
        form = cgi.FieldStorage(
            fp=environ["wsgi.input"], environ=environ, keep_blank_values=1
        )
        post = {item.name: item.value for item in form.list}
        add_new_post(post)
        body = b"Novo post criado com sucesso!"
        status = "201 Created"

    # Criar o response
    headers = [("Content-type", "text/html")]
    start_reponse(status, headers)
    return [body]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()