from database import conn
from pathlib import Path


def get_post_from_database(post_id=None):
   
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")

    return [dict(zip(fields, post)) for post in results]   

def render_template(template_name, **context):
    template = Path(template_name).read_text()
    return template.format(**context).encode("utf-8")

def get_post_list(posts):
    post_list = [
        f"""<li><a href="/{post['id']}">{post['title']}</a></li>"""
        for post in posts
    ]
    return "\n".join(post_list)


def application(environ, start_reponse):
    body = b"Content Not Found"
    status = "404 Not Found"
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]

    # roteamento de URL's
    if path == "/" and method == "GET":
        posts = get_post_from_database()
        body = render_template(
            "list.template.html",
            post_list=get_post_list(posts)
        )
        print()
        print(body)
        status = "200 ok"

    elif path.split("/")[-1].isdigit() and method == "GET":
        post_id = path.split("/")[-1]
        body = render_template(
            "post.template.html",
            post=get_post_from_database(post_id=post_id)[0]
        )
        print(body)
        status = "200 ok"


    # Criar o response
    headers = [("Content-type", "text/html")]
    start_reponse(status, headers)
    return [body]