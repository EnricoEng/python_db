# **Python DB** 🐍💾
**Exercício utilizando o banco de dados PostgreSQL**

---

## **Descrição**
Neste projeto, será utilizado o banco de dados **PostgreSQL** devido às suas vantagens:
- Banco de dados relacional que suporta dados estruturados com esquemas definidos.
- Funcionalidades avançadas para consultas complexas.
- Escalabilidade vertical e horizontal para gerenciar volumes crescentes de dados.

> **Nota:** Caso a estrutura de dados fosse muito variável, o MongoDB seria uma opção mais adequada.

---

## **Passos para Configuração**

### **1. Atualizar os Pacotes do Sistema**
Antes de instalar o PostgreSQL, atualize os pacotes do sistema:
```bash
sudo apt update
sudo apt upgrade -y



Instale o PostgreSQL utilizando o gerenciador de pacotes "apt":
sudo apt install postgresql postgresql-contrib -y

O pacote postgresql-contrib inclui utilitários adicionais.


Instalar development libraries:
sudo apt-get install libpq-dev


Acesse o PostgreSQL:
Por padrão, o PostgreSQL cria um papel chamado postgres. Para acessar o banco de dados, execute:

sudo -i -u postgres
psql

Trocar senha:
ALTER USER postgres PASSWORD 'enrico'; 

Esta senha para fins de teste, será utilizada no arquivo main.py.



Crie um banco de dados:
CREATE DATABASE python_db;

Para listar as databases:
\l

Caso de erro na criação da database, saia do psql com o comando:
\q
e execute:
createdb -U postgres python_db


Conecte-se ao banco:
psql -U postgres -d python_db



Execute o Script: Dentro do psql, use o comando:
\i caminho_para_o_script/script_criar_tabelas.sql



Já quanto as dependências do main.py, instale:
pip install psycopg2

