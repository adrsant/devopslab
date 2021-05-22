from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/")
@csrf.exempt
def pagina_inicial():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
