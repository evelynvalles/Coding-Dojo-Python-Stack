from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route("/users")
def users():
    return render_template("new_users.html")

@app.route('/create_user', methods=["POST"])
def create_user():

    print(request.form)
    User.save(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)