from flask import Flask
import os
from dotenv import load_dotenv
from Controllers.UsuarioController import usuario_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("CHAVE")

app.register_blueprint(usuario_bp)

key_path = os.getenv("SSL_KEY_PATH")
cert_path = os.getenv("SSL_CERT_PATH")

def main():
    # Verifica se os arquivos foram encontrados antes de tentar iniciar
    if not (key_path and cert_path and os.path.exists(key_path) and os.path.exists(cert_path)):
        print("Erro: Arquivos de certificado não encontrados. Verifique o .env e a pasta /certs.")
        return

    # Inicia o servidor com o contexto SSL
    app.run(debug=True,
            host='0.0.0.0',
            port=8000,
            ssl_context=(cert_path, key_path)
            )

if __name__ == '__main__':
    main()

