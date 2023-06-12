from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Привет, мой первый проект!'


if __name__ == '__main__':
    app.run()
