# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from alunos import Aluno
import database as db

app = Flask(__name__)
app.secret_key = "chave-secreta"  # Necessário para usar mensagens flash

# Garante que a tabela exista ao iniciar o servidor
db.criar_tabela()

@app.route('/')
def index():
    dados = db.listar_alunos()
    alunos = [Aluno(*d) for d in dados]
    return render_template('index.html', alunos=alunos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        matricula = request.form['matricula']
        nome = request.form['nome']
        idade = request.form['idade']
        curso = request.form['curso']

        if not matricula or not nome or not idade or not curso:
            flash('⚠️ Todos os campos são obrigatórios!')
            return redirect(url_for('cadastrar'))

        db.inserir_aluno(matricula, nome, idade, curso)
        flash('✅ Aluno cadastrado com sucesso!')
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    aluno = None
    if request.method == 'POST':
        matricula = request.form['matricula']
        dado = db.buscar_aluno(matricula)
        if dado:
            aluno = Aluno(*dado)
        else:
            flash('⚠️ Nenhum aluno encontrado com essa matrícula.')
    return render_template('buscar.html', aluno=aluno)

@app.route('/remover/<matricula>')
def remover(matricula):
    if db.remover_aluno(matricula):
        flash('✅ Aluno removido com sucesso!')
    else:
        flash('⚠️ Aluno não encontrado.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
