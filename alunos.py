# alunos.py
# Paradigma Orientado a Objetos

class Aluno:
    def __init__(self, matricula, nome, idade, curso):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __str__(self):
        return f"{self.matricula} - {self.nome} ({self.idade} anos) - Curso: {self.curso}"
