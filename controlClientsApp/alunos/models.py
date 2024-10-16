from app import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200))
    pacote_aulas = db.Column(db.String(10), nullable=False)  # '8 aulas' ou '12 aulas'
    foto_url = db.Column(db.String(200))

# Criar o banco de dados
db.create_all()
