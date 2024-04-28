import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, send_from_directory
from ...models.models import Exam, db
from . import exam

@exam.route('/sendExam', methods=['GET', 'POST'])
def sendExam():
    if request.method == 'POST':
        nome_paciente = request.form['nome_paciente']
        resultado_exame = request.form['resultado_exame']
        
        # Verificar se foi enviado um arquivo
        if 'arquivo_exame' not in request.files:
            flash('Nenhum arquivo enviado!', 'danger')
            return redirect(request.url)

        arquivo = request.files['arquivo_exame']

        # Verificar se o nome do arquivo está vazio
        if arquivo.filename == '':
            flash('Nome de arquivo inválido!', 'danger')
            return redirect(request.url)

        # Verificar se é um arquivo PDF
        if arquivo and arquivo.filename.endswith('.pdf'):
            # Salvar o arquivo no diretório de uploads
            arquivo.save(os.path.join('uploads', arquivo.filename))

            # Salvar os dados do exame no banco de dados
            exam = Exam(nome_paciente=nome_paciente, resultado=resultado_exame, arquivo=arquivo.filename)
            db.session.add(exam)
            db.session.commit()

            flash('Exame enviado com sucesso para análise!', 'success')
            return redirect(url_for('home.cliente_home_page'))
        else:
            flash('Por favor, envie um arquivo PDF!', 'danger')
            return redirect(request.url)

    return render_template('registerExam/exam.html')


@exam.route('/history')
def exam_history():
    exams = Exam.query.all()
    return render_template('registerExam/history.html', exams=exams)

@exam.route('/download/<filename>')
def download_file(filename):
    uploads_dir = os.path.join(current_app.root_path, 'uploads')
    return send_from_directory(directory=uploads_dir, filename=filename, as_attachment=True)