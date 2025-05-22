from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ← This allows requests from other origins

# Sample designers data — replicate the 2 cards in your HTML
designers = [
    {
        "id": 1,
        "name": "Epic Designs",
        "rating": 3.5,
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 57,
        "years": 8,
        "price": "$$",
        "contacts": ["+91 - 984532853", "+91 - 984532854"],
        "shortlisted": False,
        "hidden": False,
    },
    {
        "id": 2,
        "name": "Studio - D3",
        "rating": 4.5,
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 43,
        "years": 6,
        "price": "$$$",
        "contacts": ["+91 - 984532853", "+91 - 984532854"],
        "shortlisted": False,
        "hidden": False,
    },
]

@app.route('/designers', methods=['GET'])
def get_designers():
    # Return all designers except hidden ones
    visible_designers = [d for d in designers if not d["hidden"]]
    return jsonify(visible_designers)

@app.route('/designers/<int:designer_id>', methods=['GET'])
def get_designer(designer_id):
    designer = next((d for d in designers if d["id"] == designer_id), None)
    if not designer or designer["hidden"]:
        abort(404, description="Designer not found")
    return jsonify(designer)

@app.route('/designers/<int:designer_id>/shortlist', methods=['POST'])
def toggle_shortlist(designer_id):
    designer = next((d for d in designers if d["id"] == designer_id), None)
    if not designer or designer["hidden"]:
        abort(404, description="Designer not found")
    # Toggle shortlist
    designer["shortlisted"] = not designer["shortlisted"]
    return jsonify({"id": designer_id, "shortlisted": designer["shortlisted"]})

@app.route('/designers/<int:designer_id>/hide', methods=['POST'])
def hide_designer(designer_id):
    designer = next((d for d in designers if d["id"] == designer_id), None)
    if not designer:
        abort(404, description="Designer not found")
    # Hide the designer
    designer["hidden"] = True
    return jsonify({"id": designer_id, "hidden": True})

if __name__ == '__main__':
    app.run(debug=True)
