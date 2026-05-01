from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "tickets.json"


# ------------------ HELPERS ------------------

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_tickets():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_tickets(tickets):
    with open(DATA_FILE, "w") as f:
        json.dump(tickets, f, indent=4)


# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tickets", methods=["GET"])
def get_tickets():
    tickets = load_tickets()
    return jsonify(tickets)


@app.route("/tickets", methods=["POST"])
def create_ticket():
    tickets = load_tickets()

    data = request.get_json()

    new_ticket = {
        "id": len(tickets) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "status": "Open",
        "created_at": current_time()
    }

    tickets.append(new_ticket)
    save_tickets(tickets)

    return jsonify(new_ticket)


@app.route("/tickets/<int:ticket_id>/close", methods=["POST"])
def close_ticket(ticket_id):
    tickets = load_tickets()

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
            ticket["updated_at"] = current_time()
            save_tickets(tickets)
            return jsonify({"message": "Ticket closed", "ticket": ticket})

    return jsonify({"error": "Ticket not found"}), 404


# ------------------ RUN ------------------

if __name__ == "__main__":
    app.run(debug=True)