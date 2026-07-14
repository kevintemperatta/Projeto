from flask import render_template, request, Blueprint, redirect, flash, url_for
from DataBase.UsuarioDao import UsuarioDao

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/', methods=['GET'])
def root():
    return redirect('/index')

@usuario_bp.route('/index', methods=['GET'])
def home_page():
    return render_template('index.html')

@usuario_bp.route('/usuarios/form', methods=['GET'])
def user_form():
    return render_template('usuario/cadastro.html')

@usuario_bp.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    usuario = request.form
    resposta = UsuarioDao.inserir_usuario(usuario['userName'])
    if resposta is True:
        flash('Usuário cadastrado com sucesso!')
    else: 
        flash('Esse usuário já está cadastrado.')

    return redirect(url_for('usuario_bp.user_form'))

@usuario_bp.route('/usuarios/buscar')
def buscar_usuario_form():
    return render_template('usuario/buscar.html')

@usuario_bp.route('/usuarios/verificar', methods=['POST'])
def verificar_usuario():
    nome_digitado = request.form.get('userName')
    
    # Chama o método que busca no banco
    # O método deve retornar o objeto usuário se encontrar, ou None se não existir
    usuario = UsuarioDao.buscar_por_nome(nome_digitado)
    
    if usuario:
        # Se encontrou, passa o nome do usuário encontrado para o template
        return render_template('usuario/bem_vindo.html', nome=usuario.nome)
    else:
        # Se não encontrou, dispara o flash e volta para a tela de busca
        flash(f"Usuário '{nome_digitado}' não encontrado no sistema!")
        return redirect(url_for('usuario_bp.buscar_usuario_form'))



