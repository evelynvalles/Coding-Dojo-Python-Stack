from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = "dojo_survey_schema"

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.langauge = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # def __repr__(self):
    #     rep = 'Survey(' + self.name + ',' + self.location + self.langauge + self.comment + ')'
    #     return rep

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        return Survey(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language")
        if len(survey['comment']) < 3:
            is_valid = False
            flash("Comment must be at least 3 characters")
        return is_valid