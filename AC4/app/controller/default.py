from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from app.model.tables import Aluno

@app.route("/")
def index():
    #selecionar todos - select * from
    alunos = Aluno.query.all()
    return render_template("index.html", alunos=alunos)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # crio um objeto aluno com os dados do formulario
        aluno = Aluno(request.form['nome'], request.form['email'], request.form['cep'], request.form['rua'], request.form['numero'], request.form['complemento'], request.form['bairro'], request.form['cidade'], request.form['uf'])
        # adiciono o aluno (insert into)
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")
    
@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit(ra):
    # select from
    aluno = Aluno.query.get(ra)
    if request.method == 'POST':
        aluno.name = request.form['nome']
        aluno.email = request.form['email']
        aluno.cep = request.form['cep']
        aluno.rua = request.form['rua']
        aluno.bairro = request.form['bairro']
        aluno.cidade = request.form['cidade']
        aluno.uf = request.form['uf']
        aluno.numero = request.form['numero']
        aluno.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", aluno = aluno)
 
@app.route("/delete/<int:ra>")
def delete(ra):
    aluno = Aluno.query.get(ra)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('index'))
