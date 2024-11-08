from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(120))

    def __repr__(self):
        return f"<Item {self.nome}>"

with app.app_context():
    db.create_all()


@app.route('/items', methods=['POST'])
def criar_item():
    data = request.get_json()
    novo_item = Item(nome=data['nome'], descricao=data.get('descricao'))
    db.session.add(novo_item)
    db.session.commit()
    return jsonify({"message": "Item criado com sucesso!"}), 201

@app.route('/items', methods=['GET'])
def obter_itens():
    items = Item.query.all()
    return jsonify([{"id": item.id, "nome": item.nome, "descricao": item.descricao} for item in items])

@app.route('/items/<int:id>', methods=['GET'])
def obter_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({"id": item.id, "nome": item.nome, "descricao": item.descricao})

@app.route('/items/<int:id>', methods=['PUT'])
def atualizar_item(id):
    data = request.get_json()
    item = Item.query.get_or_404(id)
    item.nome = data['nome']
    item.descricao = data.get('descricao')
    db.session.commit()
    return jsonify({"message": "Item atualizado com sucesso!"})

@app.route('/items/<int:id>', methods=['DELETE'])
def deletar_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deletado com sucesso!"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
