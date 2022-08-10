from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

# displays all users
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

# displays the new user form
@app.route("/users")
def users():
    return render_template("new_users.html")

# route that processes create new user form
@app.route('/create_user', methods=["POST"])
def create_user():

    print(request.form)
    User.save(request.form)
    return redirect('/')

# route that shows one user at a time
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id': id
    }
    users = User.get_one(data)
    return render_template('show_user.html',users=users)

# route that displays edit form
@app.route('/user/edit/<int:id>')
def edit_display(id):
    data = {
        "id": id
    }
    users = User.get_one(data)
    return render_template("edit_user.html", users = users)

# route that processes user updates
@app.route("/user/edit_user/<int:id>", methods=["POST"])
def edit_user(id):
    data = {
        "id": id, "first_name": request.form["first_name"], "last_name": request.form["last_name"], "email": request.form["email"]
    }
    User.update(data)
    return redirect('/')

# route that deletes a user
@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)