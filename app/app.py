from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Calculadora API',
          description='API para operações matemáticas', doc='/swagger')

ns = api.namespace('calc', description='Operações matemáticas')

numeros_model = api.model('Numeros', {
    'a': fields.Float(required=True, description='Primeiro número'),
    'b': fields.Float(required=True, description='Segundo número')
})

@ns.route('/soma')
class Soma(Resource):
    @ns.expect(numeros_model)
    def post(self):
        data = request.json
        return {'resultado': data['a'] + data['b']}

@ns.route('/multiplicacao')
class Multiplicacao(Resource):
    @ns.expect(numeros_model)
    def post(self):
        data = request.json
        return {'resultado': data['a'] * data['b']}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
