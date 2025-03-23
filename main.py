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

post_avioes_teste = {
    "coleta_data_hora": "2025-03-23 15:00:00",
    "url": "https://forum.com/discussao/avioes",
    "post_data_hora": "2025-03-22 18:00:00",
    "usuario": "apaixonado_por_avioes",
    "titulo": "Por que os aviões são incríveis?",
    "conteudo": "Sempre fui fascinado por aviões! Desde a aerodinâmica até as complexas tecnologias envolvidas, cada voo é uma obra-prima da engenharia. O que vocês mais admiram nos aviões? Alguma história marcante de viagens aéreas?",
    "comentarios": [
        {
            "autor": "engenheiro_aeroespacial",
            "comentario_data_hora": "2025-03-23 16:00:00",
            "conteudo": "Para mim, a parte mais incrível é a sustentação gerada pelas asas! A física por trás disso é espetacular.",
            "reacoes": 15
        },
        {
            "autor": "viajante_frequente",
            "comentario_data_hora": "2025-03-23 16:30:00",
            "conteudo": "Minha melhor experiência foi voar pela primeira vez sobre as montanhas, a vista era de tirar o fôlego.",
            "reacoes": 20
        }
    ]
}


post_motores_teste = {
    "coleta_data_hora": "2025-03-23 14:00:00",
    "url": "https://forum.com/discussao/motores",
    "post_data_hora": "2025-03-22 12:00:00",
    "usuario": "fanatico_por_carros",
    "titulo": "Qual o motor mais icônico da história?",
    "conteudo": "Motores são o coração dos carros, e há tantos modelos icônicos por aí! Na sua opinião, qual motor marcou a história do automobilismo ou da engenharia automotiva? Gosto muito do V8 HEMI, mas quero saber o que vocês acham!",
    "comentarios": [
        {
            "autor": "engenheiro_automotivo",
            "comentario_data_hora": "2025-03-23 15:00:00",
            "conteudo": "O V12 Ferrari é um dos mais icônicos por sua potência e som inconfundível. Ele redefine performance automotiva.",
            "reacoes": 18
        },
        {
            "autor": "mecanico_experiente",
            "comentario_data_hora": "2025-03-23 15:30:00",
            "conteudo": "Os motores inline-6 da BMW são clássicos. Durabilidade, potência e suavidade na condução são incomparáveis.",
            "reacoes": 12
        }
    ]
}

post_nvidia_teste = {
    "coleta_data_hora": "2025-03-23 16:00:00",
    "url": "https://forum.com/discussao/chips_nvidia",
    "post_data_hora": "2025-03-22 20:00:00",
    "usuario": "entusiasta_de_tecnologia",
    "titulo": "Chips da NVIDIA: Revolução na Computação?",
    "conteudo": "Os chips da NVIDIA, especialmente as GPUs, têm transformado setores como IA, jogos e renderização gráfica. Qual o impacto desses chips no futuro da tecnologia? Gostaria de saber a opinião de vocês sobre avanços como o DLSS e a arquitetura Hopper!",
    "comentarios": [
        {
            "autor": "gamer_pro",
            "comentario_data_hora": "2025-03-23 16:10:00",
            "conteudo": "O DLSS 3 é um divisor de águas para gamers. É incrível ver como a NVIDIA está melhorando o desempenho e os gráficos.",
            "reacoes": 20
        },
        {
            "autor": "cientista_de_dados",
            "comentario_data_hora": "2025-03-23 16:15:00",
            "conteudo": "As GPUs da NVIDIA tornaram projetos de IA mais acessíveis. Modelos que levavam dias para treinar agora são feitos em horas!",
            "reacoes": 18
        },
        {
            "autor": "engenheiro_hardware",
            "comentario_data_hora": "2025-03-23 16:20:00",
            "conteudo": "A arquitetura Hopper é impressionante. A interconexão NVLink 4.0 é um avanço incrível para supercomputadores.",
            "reacoes": 15
        },
        {
            "autor": "designer_3d",
            "comentario_data_hora": "2025-03-23 16:25:00",
            "conteudo": "Os chips RTX tornam o Ray Tracing muito mais eficiente. Renderizar cenas realistas nunca foi tão rápido!",
            "reacoes": 12
        },
        {
            "autor": "critico_tecnologico",
            "comentario_data_hora": "2025-03-23 16:30:00",
            "conteudo": "Embora sejam líderes no mercado, os preços altos da NVIDIA limitam o acesso de muitos consumidores.",
            "reacoes": 10
        },
        {
            "autor": "entusiasta_ia",
            "comentario_data_hora": "2025-03-23 16:35:00",
            "conteudo": "A combinação de GPUs NVIDIA com frameworks como TensorFlow é o futuro da Inteligência Artificial.",
            "reacoes": 14
        },
        {
            "autor": "estudante_de_tecnologia",
            "comentario_data_hora": "2025-03-23 16:40:00",
            "conteudo": "Queria que GPUs NVIDIA fossem mais acessíveis para estudantes como eu. Seria ótimo aprender com o que há de melhor.",
            "reacoes": 7
        },
        {
            "autor": "analista_financeiro",
            "comentario_data_hora": "2025-03-23 16:45:00",
            "conteudo": "As ações da NVIDIA dispararam nos últimos anos devido à crescente demanda por chips em IA e jogos.",
            "reacoes": 9
        },
        {
            "autor": "curioso_tecnologico",
            "comentario_data_hora": "2025-03-23 16:50:00",
            "conteudo": "Alguém sabe explicar como funciona o DLSS em termos simples? Parece incrível, mas não entendo os detalhes técnicos.",
            "reacoes": 6
        },
        {
            "autor": "desenvolvedor_games",
            "comentario_data_hora": "2025-03-23 16:55:00",
            "conteudo": "As GPUs NVIDIA estão mudando completamente o desenvolvimento de jogos. O suporte a APIs como Vulkan é fantástico.",
            "reacoes": 8
        },
        {
            "autor": "tecnico_informatico",
            "comentario_data_hora": "2025-03-23 17:00:00",
            "conteudo": "Os chips da NVIDIA são incrivelmente poderosos, mas o consumo de energia das GPUs top de linha é algo a ser considerado.",
            "reacoes": 5
        }
    ]
}



def conectar():
    return psycopg2.connect(
        host="localhost",
        database="python_db",
        user="postgres",
        password="enrico"
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



def remover_post_e_comentarios(post_id):
    conn = conectar()
    cur = conn.cursor()
    try:
        # Remover os comentários associados ao post
        query_remover_comentarios = """
        DELETE FROM comentarios WHERE post_id = %s;
        """
        cur.execute(query_remover_comentarios, (post_id,))
        
        # Remover o próprio post
        query_remover_post = """
        DELETE FROM posts WHERE post_id = %s;
        """
        cur.execute(query_remover_post, (post_id,))
        
        conn.commit()  # Confirmar as alterações
        print(f"Post com ID {post_id} e seus comentários foram removidos com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        conn.rollback()  # Reverter alterações em caso de erro
    finally:
        cur.close()
        conn.close()




conectar()
inserir_post(post_teste)
inserir_post(post_avioes_teste)
inserir_post(post_motores_teste)
inserir_post(post_nvidia_teste)
#remover_post_e_comentarios(4)  # ID do post a ser removido
print("\n ------------------------------------------------------------------ \n")
print("Consultando posts e comentários")
for linha in consultar_posts_e_comentarios():
    print(linha)
print("\n ------------------------------------------------------------------ \n")
print("Pesquisando por posts com a palavra 'Python':")
for linha in pesquisar_posts_por_titulo("Python"):
    print(linha)
print("\n ------------------------------------------------------------------ \n")
print("Procurando posts mais comentados:")
for linha in posts_mais_comentados():
    print(linha)
