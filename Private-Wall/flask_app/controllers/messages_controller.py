from flask_app import app
from flask import render_template,redirect,request,session,flash
import re
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.messages_model import Message

@app.route('/send_message', methods=["POST"])
def send_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id'],
        'content': request.form['content']
    }
    Message.save(data)
    return redirect('/dashboard')

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Message.destroy(data)
    return redirect('/dashboard')