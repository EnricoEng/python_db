CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    coleta_data_hora TIMESTAMP NOT NULL,
    url TEXT NOT NULL,
    post_data_hora TIMESTAMP NOT NULL,
    usuario TEXT NOT NULL,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL
);

CREATE TABLE comentarios (
    comentario_id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(post_id),
    autor TEXT NOT NULL,
    comentario_data_hora TIMESTAMP NOT NULL,
    conteudo TEXT NOT NULL,
    reacoes INT NOT NULL
);
