from flask import Flask, render_template, request

app = Flask('__name__')

games = [
    {'name':'Bloodborne',
     'year': 2015,
     'ready':True,
     'id':0
    },
    {'name':'Assassin\'s Creed II',
     'year': 2009,
     'ready': False,
     'id':1
    },
    {'name':'Half-Life',
     'year': 1998,
     'ready': True,
     'id':2
    },
    {'name':'Doom Eternal',
     'year': 2020,
     'ready': False,
     'id':3
    }
]

@app.route('/')
def main():
    return render_template('index.html', games_list=games)

@app.route('/ready/<int:game_id>', methods=['PATCH'])
def modify(game_id):
    global games
    ready = request.json['ready']
    for game in games:
        if game['id'] == game_id:
            game.update({'ready': ready})
    return 'Ok'

@app.route('/game', methods=['POST'])
def create_task():
    data = request.json['']
    last_id = games[-1]['id']
    new_id = last_id + 1
    data['id'] = new_id
    games.append(data)
    return 'Ok'

if __name__ == '__main__':
    app.run(debug=True)