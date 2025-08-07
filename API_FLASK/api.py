from flask import Flask, jsonify, request

app = Flask(__name__)

utilisateurs = {
    1: {"nom": "Ali", "âge": 25},
    2: {"nom": "Sofia", "âge": 30}
}

@app.route("/api/utilisateurs", methods=["GET"])
def get_utilisateurs():
    return jsonify(utilisateurs)

@app.route("/api/utilisateurs/<int:id>", methods=["GET"])
def get_utilisateur(id):
    user = utilisateurs.get(id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"erreur": "Utilisateur non trouvé"}), 404

@app.route("/api/utilisateurs", methods=["POST"])
def ajouter_utilisateur():
    data = request.json
    nouvel_id = max(utilisateurs.keys()) + 1
    utilisateurs[nouvel_id] = data
    return jsonify({"message": "Utilisateur ajouté", "id": nouvel_id}), 201

if __name__ == "__main__":
    app.run(debug=True)
