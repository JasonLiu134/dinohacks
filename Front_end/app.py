from flask import Flask
from views import file_name

app = Flask(__name__)
app.register_blueprint(file_name, url_prefix = "/")

if __name__ == '__main__':
    app.run(debug=True)