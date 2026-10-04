from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Jarvis 2.0 está online!"

@app.route("/comando", methods=["POST"])
def comando():
    dados = request.get_json()
    texto = dados.get("texto", "").lower()

    if "olá" in texto or "oi" in texto:
        resposta = "Olá! Eu sou o Jarvis 2.0."
    elif "quem é você" in texto:
        resposta = "Sou seu assistente virtual."
    elif "sair" in texto:
        resposta = "Até mais!"
    else:
        resposta = f"Recebi seu comando: {texto}"

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
