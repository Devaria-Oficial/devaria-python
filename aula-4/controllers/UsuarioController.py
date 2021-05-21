import json

from flask import Blueprint, Response, request

from enums.TipoUsuario import TipoUsuario
from model.Usuario import Usuario
from service.UsuarioService import UsuarioService

usuario_controller = Blueprint('usuario_controller',  __name__)

usuarioService = UsuarioService()

@usuario_controller.route('/login', methods=["POST"])
def login():
    parametros = request.get_json()
    resposta = {
        "mensagem": ""
    }
    usuario = Usuario(parametros["usuario"], parametros["senha"], TipoUsuario.COMUM.value)

    if(usuario.nome == "Filipe" and usuario.senha == "KOA!@#S1K321DO"):
        usuario.token = "KSDAOKDSAO54656SAD1213!@#!@#5as59dsa5ASD"

        return Response(json.dumps(usuario.__dict__), status=200, mimetype="application/json")

    else:
        resposta["mensagem"] = "Usuário ou Senha incorretos!"

        return Response(json.dumps(resposta), status=401, mimetype="application/json")

@usuario_controller.route('/consultar', methods=["GET"])
def consultar_usuario():
    nome_usuario = request.args.get("nome_usuario")

    resposta_consulta = usuarioService.consultarUsuario(nome_usuario)

    if(resposta_consulta):
        return Response(json.dumps(resposta_consulta.__dict__), status=200, mimetype="application/json")
    else:
        reposta = {
            "mensagem": "Usuario não encontrado!"
        }
        return Response(json.dumps(reposta), status=404, mimetype="application/json")
