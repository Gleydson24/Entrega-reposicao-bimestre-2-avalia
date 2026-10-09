from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "").strip()

        if not nome or not email or not senha:
            flash("Todos os campos são obrigatórios.")
            return render_template("registro.html")

        if database.buscar_usuario_por_email(email):
            flash("E-mail já cadastrado no sistema.")
            return render_template("registro.html")

        senha_hash = generate_password_hash(senha)
        database.criar_usuario(nome, email, senha_hash)

        flash("Cadastro realizado com sucesso! Faça login.")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "").strip()

        if not email or not senha:
            flash("E-mail e senha são obrigatórios.")
            return render_template("login.html")

        usuario = database.buscar_usuario_por_email(email)

        if not usuario or not check_password_hash(usuario.senha_hash, senha):
            flash("E-mail ou senha incorretos.")
            return render_template("login.html")

        session["usuario_id"] = usuario.id
        session["usuario_nome"] = usuario.nome

        flash("Login efetuado com sucesso!")
        return redirect(url_for("leituras.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()

    flash("Você saiu do sistema.")
    return redirect(url_for("auth.login"))