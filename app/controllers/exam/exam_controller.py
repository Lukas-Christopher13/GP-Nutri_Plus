import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, send_from_directory
from ...models.models import Exam, db
from ...models.nuticionista_model import Notification
from ...models.cliente_model import Cliente
from flask_login import current_user
from . import exam

EXTENSOES_PERMITIDAS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'}

def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSOES_PERMITIDAS

@exam.route('/sendExam', methods=['GET', 'POST'])
def sendExam():
    if request.method == 'POST':
        nome_paciente = request.form['nome_paciente']
        resultado_exame = request.form['resultado_exame']
        
        if 'arquivo_exame' not in request.files:
            flash('Nenhum arquivo enviado!', 'danger')
            return redirect(request.url)

        arquivo = request.files['arquivo_exame']

        if arquivo.filename == '':
            flash('Nome de arquivo inválido!', 'danger')
            return redirect(request.url)

        if arquivo and arquivo_permitido(arquivo.filename):
            filename = secure_filename(arquivo.filename)
            uploads_dir = os.path.join(current_app.root_path, 'uploads')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            arquivo.save(os.path.join(uploads_dir, filename))

            cliente = Cliente.query.get(current_user.id)
            nutricionista = cliente.nutricionista

            exam = Exam(
                nome_paciente=nome_paciente,
                resultado=resultado_exame,
                arquivo=filename,
            )
            db.session.add(exam)
            db.session.commit()

            notification = Notification(
                message=f'Novo exame enviado por {cliente.full_name}.',
                nutricionista_id=nutricionista.id
            )
            db.session.add(notification)
            db.session.commit()

            flash('Exame enviado com sucesso para análise!', 'success')
            return redirect(url_for('home.cliente_home_page'))
        else:
            flash('Por favor, envie um arquivo PDF, DOC, DOCX, JPG ou JPEG!', 'danger')
            return redirect(request.url)

    return render_template('registerExam/exam.html')



@exam.route('/history')
def exam_history():
    exams = Exam.query.all()
    return render_template('registerExam/history.html', exams=exams)

@exam.route('/download/<filename>')
def download_file(filename):
    uploads_dir = os.path.join(current_app.root_path, 'uploads')
    filepath = os.path.join(uploads_dir, filename)
    
   
    if os.path.exists(filepath): #verificar se o arquivo existe no diretório
        return send_from_directory(uploads_dir, filename, as_attachment=True)
    else:
        flash('O arquivo solicitado não foi encontrado.', 'danger')
        return redirect(url_for('exam.exam_history'))
    
@exam.route('/notificacoes')
def view_notifications():
    nutricionista = current_user
    notifications = Notification.query.filter_by(nutricionista_id=nutricionista.id).all()
    return render_template('registerExam/notificacoes.html', notifications=notifications)

