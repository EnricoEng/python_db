import psycopg2

post_teste = {
    "coleta_data_hora": "2025-03-21 10:30:00",
    "url": "https://forum.com/discussao/1",
    "post_data_hora": "2025-03-20 10:00:00",
    "usuario": "usuario_teste",
    "titulo": "Como aprender Python?",
    "conteudo": "Estou começando a aprender Python e gostaria de dicas de recursos e melhores práticas!",
    "comentarios": [
        {
            "autor": "usuario_comentario1",
            "comentario_data_hora": "2025-03-21 10:15:00",
            "conteudo": "Recomendo começar com o site oficial de Python e assistir tutoriais no YouTube.",
            "reacoes": 10
        },
        {
            "autor": "usuario_comentario2",
            "comentario_data_hora": "2025-03-21 10:20:00",
            "conteudo": "Livros como 'Automate the Boring Stuff with Python' são ótimos para iniciantes.",
            "reacoes": 7
        }
    ]
}


def conectar():
    return psycopg2.connect(
        host="localhost",
        database="forum_db",
        user="seu_usuario",
        password="sua_senha"
    )


def inserir_post(post):
    conn = conectar()
    cur = conn.cursor()
    query_post = """
    INSERT INTO posts (coleta_data_hora, url, post_data_hora, usuario, titulo, conteudo)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING post_id;
    """
    cur.execute(query_post, (post['coleta_data_hora'], post['url'], post['post_data_hora'],
                             post['usuario'], post['titulo'], post['conteudo']))
    post_id = cur.fetchone()[0]
    for comentario in post['comentarios']:
        query_comentario = """
        INSERT INTO comentarios (post_id, autor, comentario_data_hora, conteudo, reacoes)
        VALUES (%s, %s, %s, %s, %s);
        """
        cur.execute(query_comentario, (post_id, comentario['autor'], comentario['comentario_data_hora'],
                                       comentario['conteudo'], comentario['reacoes']))
    conn.commit()
    cur.close()
    conn.close()


def consultar_posts_e_comentarios():
    conn = conectar()
    cur = conn.cursor()
    query = """
    SELECT p.titulo, p.usuario, c.autor, c.conteudo
    FROM posts p
    LEFT JOIN comentarios c ON p.post_id = c.post_id;
    """
    cur.execute(query)
    resultados = cur.fetchall()
    conn.close()
    return resultados





def pesquisar_posts_por_titulo(palavra_chave):
    conn = conectar()
    cur = conn.cursor()
    query = """
    SELECT * FROM posts
    WHERE titulo ILIKE %s;
    """
    cur.execute(query, ('%' + palavra_chave + '%',))
    resultados = cur.fetchall()
    conn.close()
    return resultados




def pesquisar_posts_por_titulo(palavra_chave):
    conn = conectar()
    cur = conn.cursor()
    query = """
    SELECT * FROM posts
    WHERE titulo ILIKE %s;
    """
    cur.execute(query, ('%' + palavra_chave + '%',))
    resultados = cur.fetchall()
    conn.close()
    return resultados



def posts_mais_comentados():
    conn = conectar()
    cur = conn.cursor()
    query = """
    SELECT p.titulo, COUNT(c.comentario_id) as total_comentarios
    FROM posts p
    LEFT JOIN comentarios c ON p.post_id = c.post_id
    GROUP BY p.titulo
    ORDER BY total_comentarios DESC;
    """
    cur.execute(query)
    resultados = cur.fetchall()
    conn.close()
    return resultados


inserir_post(post_teste)
print(consultar_posts_e_comentarios())
print(pesquisar_posts_por_titulo('Python'))
print(posts_mais_comentados())
