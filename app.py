from flask import Flask, render_template

from controllers.teams_controller import teams_blueprint
from controllers.fixtures_controller import fixtures_blueprint

app = Flask(__name__)

app.register_blueprint(teams_blueprint)
app.register_blueprint(fixtures_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)