from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


DATABASE = "email_schema"

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query= "INSERT INTO emails (email_address, created_at, updated_at) VALUES (%(email_address)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        emails = []
        for u in results:
            emails.append( cls(u) )
        return emails

    @classmethod
    def destroy_email(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email_address']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            flash("Congratulations on creating a successful email!")
        return is_valid
