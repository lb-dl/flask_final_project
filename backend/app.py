from flask import Flask

from config import DevelopmentConfig, ProductionConfig, Config
from modules.database.settings import db
from routes import Users


app = Flask(__name__)

if debug_app := Config.is_development_config():
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(ProductionConfig())

# add rules for user view
user_view = Users.as_view('users')
app.add_url_rule('/api/v1/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
app.add_url_rule('/api/v1/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/api/v1/users/<int:user_id>', view_func=user_view, methods=['GET', 'PATCH', 'DELETE'])


db.init_app(app)

with app.app_context():
    db.create_all()


# test endpoint
@app.route('/')
def test_endpoint():
    return f'test endpoint works'


if __name__ == '__main__':
    app.run(port=8000, debug=debug_app)
