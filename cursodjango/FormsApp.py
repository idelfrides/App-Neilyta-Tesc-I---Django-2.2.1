from django.forms import ModelForm
from cursodjango.models import Professores, Alunos
from cursodjango.models import Cursos


class ProfForm(ModelForm):
    class Meta:
        model = Professores
        fields = [
            'nome_Prof', 
            'formacao', 
            'titulo_Academico', 
            'curso_Leciona', 
            'ano_Inicio', 
            'turmas', 
            'membro_Organizacao'
        ]



class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = [
            'nome_aluno', 
            'ano', 
            'curso', 
            'genero', 
            'idade', 
            'eh_destaque'
        ]


class CursoForm(ModelForm):
    class Meta:
        model = Cursos
        fields = [
            'nome_Curso', 
            'data_Inicio', 
            'num_Alunos', 
            'num_Prof', 
            'alunos_Formados', 
            'descricao'
        ]
