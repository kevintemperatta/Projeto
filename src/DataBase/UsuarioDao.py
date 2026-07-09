from DataBase.Connection import session
from Models.Usuario import Usuario

class UsuarioDao:

    @staticmethod
    def inserir_usuario(nome_pessoa):
        novo_usuario = Usuario(None, nome_pessoa)
        session.add(novo_usuario)
        session.commit()
        return '', 200
    
    @staticmethod
    def buscar_por_nome(nome_digitado):
        usuario = session.query(Usuario).filter_by(nome=nome_digitado).first()
        return usuario
