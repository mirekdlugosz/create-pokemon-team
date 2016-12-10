from flask import Flask, Response, json
app = Flask(__name__)

@app.route('/pokemon')
def api_root():
    pokemon = [
            {
                "name": "bulbasaur",
                "type": ["Grass", "Poison"]
            },
            {
                "name": "charmander",
                "type": ["Fire"]
            },
            {
                "name": "squirtle",
                "type": ["Water"]
            },
            {
                "name": "pikachu",
                "type": ["electric"]
            },
        ]
    js = json.dumps(pokemon)
    return Response(js, status=200, mimetype='application/json')

@app.route('/pokemon/<pokemon_name>/moves')
def api_articles(pokemon_name):
    if pokemon_name == "bulbasaur":
        moves = [
                    {
                        "name": "Tackle",
                        "type": "Normal",
                        "category": "physical"
                    },
                    {
                        "name": "Stun Spore",
                        "type": "Grass",
                        "category": "status"
                    }
                ]
    elif pokemon_name == "charmander":
        moves = [
                    {
                        "name": "Ember",
                        "type": "Fire",
                        "category": "special"
                    },
                    {
                        "name": "Dragon Rage",
                        "type": "Dragon",
                        "category": "special"
                    }
                ]
    elif pokemon_name == "squirtle":
        moves = [
                    {
                        "name": "Bite",
                        "type": "Dark",
                        "category": "physical"
                    },
                    {
                        "name": "Water Pulse",
                        "type": "Water",
                        "category": "special"
                    }
                ]
    elif pokemon_name == "pikachu":
        moves = [
                    {
                        "name": "Volt Tackle",
                        "type": "Electric",
                        "category": "physical"
                    },
                    {
                        "name": "Electro Ball",
                        "type": "Electric",
                        "category": "special"
                    }
                ]
    js = json.dumps(moves)
    return Response(js, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()
