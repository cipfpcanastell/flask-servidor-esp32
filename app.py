from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    print("Datos recibidos:", datos)
    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)