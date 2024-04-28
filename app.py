from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# games = [
#     {'name':'Bloodborne',
#      'year': 2015,
#      'ready':True,
#      'id':0
#     },
#     {'name':'Assassin\'s Creed II',
#      'year': 2009,
#      'ready': False,
#      'id':1
#     },
#     {'name':'Half-Life',
#      'year': 1998,
#      'ready': True,
#      'id':2
#     },
#     {'name':'Doom Eternal',
#      'year': 2020,
#      'ready': False,
#      'id':3
#     }
# ]

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    year = db.Column(db.String(10))
    ready = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Game {self.id} / {self.year}> {self.name}'


@app.route('/')
def main():
    games = Game.query.all()
    return render_template('index.html', games_list=games)

@app.route('/ready/<int:game_id>', methods=['PATCH'])
def modify(game_id):
    game = Game.query.get(game_id)
    game.ready = request.json['ready']
    db.session.commit()
    return 'Ok'

@app.route('/game', methods=['POST'])
def create_task():
    data = request.json
    game = Game(**data)
    db.session.add(game)
    db.session.commit()
    return 'Ok'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)