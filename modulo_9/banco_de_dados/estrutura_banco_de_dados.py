from flask import Flask # criar API
from flask_sqlalchemy import SQLAlchemy # criar banco de dados

# Criar um API flask
app = Flask(__name__)

# Criar um instância de SQLAlchemy
app.config['SECRET_KEY'] = 'fsd2323F#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela de postagem
# id_postagem, titulo, autor
class Postagem(db.Model):
  __tablename__ = 'postagem'
  id_postagem = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String)
  id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela de autor
# id_autor, nome, email,senha, admin, postagens
class Autor(db.Model):
  __tablename__ = 'autor'
  id_autor = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String)
  email = db.Column(db.String)
  senha = db.Column(db.String)
  admin = db.Column(db.Boolean)
  postagens = db.relationship('Postagem')

# Executar o comando para criar o banco de dados
with app.app_context():
  db.drop_all() # apaga qualquer estrutura previa que possa existir
  db.create_all() # permite criar todas as tabelas, no caso, 2 (Postagem, Autor)
  # criar usuários administradores
  autor = Autor(nome='Saulo',email='saulogil@hotmail.com',senha='12345', admin=True)
  db.session.add(autor)
  db.session.commit()