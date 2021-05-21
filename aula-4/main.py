from flask import Flask

from controllers.UsuarioController import usuario_controller

app = Flask(__name__)

app.register_blueprint(usuario_controller, url_prefix='/api/v1/usuario')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
