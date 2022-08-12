from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.emails import Email

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/register', methods=["POST"])
def register():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template("success.html", emails=emails)

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Email.destroy_email(data)
    return redirect('/success')