from flask import Flask

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False  # Sensitive
csrf = CSRFProtect()
csrf.init_app(app)


@app.route('/')
def pagina_inicial():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
