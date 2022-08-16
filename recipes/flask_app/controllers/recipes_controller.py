from flask_app.models.recipes import Recipe
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import User


@app.route('/recipes/new')
def display_create():
    if not "user_id" in session:
        return redirect('/')
    return render_template('recipe_new.html')

@app.route('/recipes/create', methods=["POST"])
def create():
    if not "user_id" in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.save(data)

    return redirect('/recipes')

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe = Recipe.get_by_id(data)
    return render_template('recipe_edit.html', recipe=recipe)

@app.route('/recipes/update/<int:id>', methods=["POST"])
def update(id):
    if not "user_id" in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        **request.form,
        'id': id
    }
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/recipes/destroy/<int:id>')
def destroy(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
        'id': id 
    }
    #optional security features
    to_be_deleted = Recipe.get_by_id(data)
    if not session['user_id'] == to_be_deleted.user_id:
        flash("Quit trying to delete other people's recipes", "err_destroy")
        return redirect('/')
    Recipe.destroy(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_one(id):
    if not "user_id" in session:
        return redirect('/')
    data = {
        'id': id
    }
    data2 = {
        'id': session['user_id']
    }
    recipe = Recipe.get_by_id(data)
    user = User.get_one_user(data2)
    return render_template('recipe_one.html', recipe=recipe, user=user)