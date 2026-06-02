import random
from js import setTimeout, document

GAME_TURNS = 30
INTERVAL = 1000
WIDTH = 50

info = document.getElementById("info")
canvas = document.getElementById("canvas")
context = canvas.getContext("2d")

game = {
    "turns": GAME_TURNS,
    "score": 0,
    "mx": 0,
    "my": 0,
    "hide": True,
}

def next_turn():
    if game["turns"] <= 0:
        game_over()
        return
    game["turns"] -= 1
    update_mogura()
    update_screen()
    setTimeout(next_turn, INTERVAL)

def update_mogura():
    game["hide"] = not game["hide"]
    if not game["hide"]:
        game["mx"] = random.randint(0, canvas.width - WIDTH)
        game["my"] = random.randint(0, canvas.height - WIDTH)

def update_screen():
    context.clearRect(0, 0, canvas.width, canvas.height)

    if not game["hide"]:
        context.fillStyle = "brown"
        context.fillRect(game["mx"], game["my"], WIDTH, WIDTH)

        info.innerText = (f"スコア: {game['score']}点 /"
                          f"残り時間: {game['turns']}")

def game_over():
    info.innerText = f"モグラ叩き終了: スコア {game['score']}点"
    document.getElementById("start_button").disabled = False