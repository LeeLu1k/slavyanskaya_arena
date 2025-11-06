from flask import Flask, request, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder="webapp")

heroes_data = [
    {'name': 'Богатырь', 'hp': 100, 'atk': 15, 'def': 10, 'spd': 5},
    {'name': 'Валькирия', 'hp': 90, 'atk': 18, 'def': 8, 'spd': 7},
    {'name': 'Стрелок', 'hp': 80, 'atk': 12, 'def': 5, 'spd': 10},
    {'name': 'Маг', 'hp': 70, 'atk': 20, 'def': 5, 'spd': 6}
]

def auto_battle(user_hero, enemy_hero):
    log = []
    hp_user = user_hero['hp']
    hp_enemy = enemy_hero['hp']
    turn = 'user' if user_hero['spd'] >= enemy_hero['spd'] else 'enemy'

    while hp_user > 0 and hp_enemy > 0:
        if turn == 'user':
            damage = max(user_hero['atk'] - enemy_hero['def'], 0)
            hp_enemy -= damage
            log.append(f"{user_hero['name']} наносит {damage} урона {enemy_hero['name']}. HP врага: {max(hp_enemy,0)}")
            turn = 'enemy'
        else:
            damage = max(enemy_hero['atk'] - user_hero['def'], 0)
            hp_user -= damage
            log.append(f"{enemy_hero['name']} наносит {damage} урона {user_hero['name']}. Ваш HP: {max(hp_user,0)}")
            turn = 'user'

    result = 'Победа' if hp_user > 0 else 'Поражение'
    return result, log

# Endpoint Web App для боя
@app.route("/battle")
def battle():
    user_id = request.args.get("user_id")
    user_hero = heroes_data[0]  # бесплатный герой для игрока
    enemy_hero = random.choice(heroes_data)
    result, log = auto_battle(user_hero, enemy_hero)
    return jsonify({"result": result, "log": log})

# Сервируем Web App
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
