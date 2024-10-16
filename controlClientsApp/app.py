from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Registrar rotas do aplicativo 'alunos'
from alunos.urls import alunos_bp
app.register_blueprint(alunos_bp)

if __name__ == '__main__':
    app.run(debug=True)
