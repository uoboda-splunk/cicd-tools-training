from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return get_info_string()


def get_info_string():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
