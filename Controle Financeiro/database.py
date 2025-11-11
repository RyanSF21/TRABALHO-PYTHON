import sqlite3
def conectar():
    return sqlite3.connect("alunos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_aluno(matricula, nome, idade, curso):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO alunos (matricula, nome, idade, curso) VALUES (?, ?, ?, ?)",
                       (matricula, nome, idade, curso))
        conn.commit()
    except sqlite3.IntegrityError:
        print("⚠️ Matrícula já cadastrada!")
    conn.close()

# Listar alunos
def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    conn.close()
    return dados

# Buscar aluno por matrícula
def buscar_aluno(matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE matricula = ?", (matricula,))
    dado = cursor.fetchone()
    conn.close()
    return dado

# Remover aluno
def remover_aluno(matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE matricula = ?", (matricula,))
    conn.commit()
    removidos = cursor.rowcount
    conn.close()
    return removidos > 0
