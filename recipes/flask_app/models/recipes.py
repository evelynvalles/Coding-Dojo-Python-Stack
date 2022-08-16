from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User
from flask import flash
DATABASE = "recipes_schema"

class Recipe:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for row in results:
                this_recipe = Recipe(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at':row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                this_user = User(user_data)
                this_recipe.person = this_user
                all_recipes.append(this_recipe)
            return all_recipes
        return results

    @classmethod
    def save(cls,data):
        query= "INSERT INTO recipes (name, under, description, instructions, date, user_id) VALUES (%(name)s,%(under)s,%(description)s,%(instructions)s, %(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, under = %(under)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        row = result[0]
        print(row)
        this_recipe = Recipe(row)
        user_data = {
            **row,
            'id': row['users.id'],
            'created_at': row['users.created_at'],
            "updated_at": row['users.updated_at']
        }
        person = User(user_data)
        this_recipe.person = person
        return this_recipe

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters long", "err_name")
        if len(form_data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters long", "err_description")
        if len(form_data['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters long", "err_instructions")
        if len(form_data['date']) < 1:
            is_valid = False
            flash("Date field is required", "err_date")
        if "under" not in form_data:
            is_valid = False
            flash("Under 30 minutes field is required", "err_under")
        return is_valid