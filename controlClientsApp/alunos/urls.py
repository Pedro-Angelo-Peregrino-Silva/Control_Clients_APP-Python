from flask import Blueprint
from alunos.views import adicionar_aluno, listar_alunos, atualizar_aluno, deletar_aluno

alunos_bp = Blueprint('alunos', __name__)

alunos_bp.add_url_rule('/alunos', 'listar_alunos', listar_alunos)
alunos_bp.add_url_rule('/alunos/adicionar', 'adicionar_aluno', adicionar_aluno, methods=['GET', 'POST'])
alunos_bp.add_url_rule('/alunos/atualizar/<int:aluno_id>', 'atualizar_aluno', atualizar_aluno, methods=['GET', 'POST'])
alunos_bp.add_url_rule('/alunos/deletar/<int:aluno_id>', 'deletar_aluno', deletar_aluno, methods=['POST'])
