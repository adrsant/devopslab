from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/', methods=(['GET']))
@csrf.exempt
def pagina_inicial():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
