from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<html>
    <head>
        <title>Casa Conectada</title>
    </head>
    <body>
        <h2>Minha Casa</h2>
        <h3>Menu Principal:</h3>
        <ul>
            <li><a href="/bedroom">Quarto</a></li>
            <li><a href="/bathroom">Banheiro</a></li>
        </ul>
    </body>
</html>
"""

@app.route('/bedroom')
def bedroom():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h2>Minha Casa</h2>
        <h3>Quarto:</h3>
        <ul>
            <li><a href="/bedroom-sensors">Listar Sensores</a></li>
            <li><a href="/bedroom-actuators">Listar Atuadores</a></li>
        </ul>
        <p>Voltar para o <a href="/">Menu Principal</a>!</p>
    </body>
</html>
"""

@app.route('/bedroom-sensors')
def bedroom_sensors():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h1>Sensores do Quarto:</h1>
        <ul>
            <li>Sensor de Luminosidade</li>
            <li>Sensor de Temperatura</li>
        </ul>
        <p>Voltar para o <a href="/bedroom">Menu do Quarto</a>!</p>
    </body>
</html>
"""

@app.route('/bedroom-actuators')
def bedroom_actuators():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h1>Atuadores do Quarto:</h1>
        <ul>
            <li>Ar Condicionado</li>
            <li>Lâmpada Inteligente</li>
        </ul>
        <p>Voltar para o <a href="/bedroom">Menu do Quarto</a>!</p>
    </body>
</html>
"""

@app.route('/bathroom')
def bathroom():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h2>Minha Casa</h2>
        <h3>Banheiro:</h3>
        <ul>
            <li><a href="/bathroom-sensors">Listar Sensores</a></li>
            <li><a href="/bathroom-actuators">Listar Atuadores</a></li>
        </ul>
        <p>Voltar para o <a href="/">Menu Principal</a>!</p>
    </body>
</html>
"""

@app.route('/bathroom-sensors')
def bathroom_sensors():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h1>Sensores do Banheiro:</h1>
        <ul>
            <li>Sensor de Luminosidade</li>
            <li>Sensor de Umidade</li>
        </ul>
        <p>Voltar para o <a href="/bathroom">Menu do Banheiro</a>!</p>
    </body>
</html>
"""

@app.route('/bathroom-actuators')
def bathroom_actuators():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    </head>
    <body>
        <h1>Atuadores do Banheiro:</h1>
        <ul>
            <li>Piso Aquecido</li>
            <li>Encher Banheira</li>
        </ul>
        <p>Voltar para o <a href="/bathroom">Menu do Banheiro</a>!</p>
    </body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)