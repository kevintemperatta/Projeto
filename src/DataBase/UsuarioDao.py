from DataBase.Connection import session
from Models.Usuario import Usuario

class UsuarioDao:

    @staticmethod
    def inserir_usuario(nome_pessoa) -> bool:

        try:

            novo_usuario = Usuario(None, nome_pessoa)

            usuarios = session.query(Usuario).filter_by(nome=nome_pessoa).first()

            if usuarios is None:
                session.add(novo_usuario)
                session.commit()
                return True

            if usuarios.nome == novo_usuario.nome:
                return False
        except:
            print('Ocorreu um erro inesperado')
        
    
    @staticmethod
    def buscar_por_nome(nome_digitado):
        usuario = session.query(Usuario).filter_by(nome=nome_digitado).first()
        return usuario
