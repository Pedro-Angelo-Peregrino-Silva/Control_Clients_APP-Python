from flask import render_template, request, redirect, url_for, flash
from app import db
from alunos.models import Aluno


# Create - Adicionar novo aluno
def adicionar_aluno():
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        data_nascimento = request.form['data_nascimento']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        pacote_aulas = request.form['pacote_aulas']
        foto_url = request.form['foto_url']  # Foto opcional

        # Verifica se os campos obrigatórios estão preenchidos
        if not nome_completo or not data_nascimento or not email or not telefone:
            flash('Campos obrigatórios estão faltando!', 'error')
            return render_template('alunos/adicionar_aluno.html')

        # Criar novo aluno
        novo_aluno = Aluno(nome_completo=nome_completo, data_nascimento=data_nascimento,
                           email=email, telefone=telefone, endereco=endereco,
                           pacote_aulas=pacote_aulas, foto_url=foto_url)

        try:
            db.session.add(novo_aluno)
            db.session.commit()
            flash('Aluno adicionado com sucesso!', 'success')
            return redirect(url_for('alunos.listar_alunos'))
        except Exception as e:
            flash(f'Erro ao adicionar aluno: {str(e)}', 'error')
            return render_template('alunos/adicionar_aluno.html')

    return render_template('alunos/adicionar_aluno.html')


# Read - Listar alunos
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template('alunos/listar_alunos.html', alunos=alunos)


# Update - Atualizar aluno existente
def atualizar_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)

    if request.method == 'POST':
        aluno.nome_completo = request.form['nome_completo']
        aluno.data_nascimento = request.form['data_nascimento']
        aluno.email = request.form['email']
        aluno.telefone = request.form['telefone']
        aluno.endereco = request.form['endereco']
        aluno.pacote_aulas = request.form['pacote_aulas']
        aluno.foto_url = request.form['foto_url']

        try:
            db.session.commit()
            flash('Aluno atualizado com sucesso!', 'success')
            return redirect(url_for('alunos.listar_alunos'))
        except Exception as e:
            flash(f'Erro ao atualizar aluno: {str(e)}', 'error')

    return render_template('alunos/atualizar_aluno.html', aluno=aluno)


# Delete - Deletar aluno
def deletar_aluno(aluno_id):
    aluno = Aluno.query.get_or_404(aluno_id)

    try:
        db.session.delete(aluno)
        db.session.commit()
        flash('Aluno deletado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar aluno: {str(e)}', 'error')

    return redirect(url_for('alunos.listar_alunos'))
