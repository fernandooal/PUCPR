from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Conteúdo da Página Inicial!"

@app.route('/sensors')
def sensors():
    return "Listar sensores"

@app.route('/actuators')
def actuators():
    return "Listar atuadores"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)