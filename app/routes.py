from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Message
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            new_message = Message(content=content)
            db.session.add(new_message)
            db.session.commit()
        return redirect(url_for('main.index'))

    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template('index.html', messages=messages)

# API – GET
@main.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.id.desc()).all()
    return jsonify([{"id": m.id, "content": m.content} for m in messages])

# API – POST
@main.route('/api/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({"error": "Champ 'content' manquant"}), 400

    new_msg = Message(content=content)
    db.session.add(new_msg)
    db.session.commit()
    return jsonify({"id": new_msg.id, "content": new_msg.content}), 201

