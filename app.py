from flask import Flask
from flask_restful import Resource, Api
from logic import search, complex_search

app = Flask(__name__)
api = Api(app)

class Dictionary(Resource):
    def get(self, word):
        if '_' in word:
            result = complex_search(word)
        else:
            result = search(word)
        return result

api.add_resource(Dictionary, '/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)
