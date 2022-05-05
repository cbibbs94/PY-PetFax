from flask import Flask
from flask_migrate import Migrate

#Factory
def create_app():
    app = Flask(__name__)

    #Postgres Connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kyuubichan15!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models
    models.db.init_app(app)
    
    #index route
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'


    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    migrate = Migrate(app, models.db)


    from . import fact
    app.register_blueprint(fact.bp)
    
    return app