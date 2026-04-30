from flask import Flask, request, jsonify
from ticket_manager import load_tickets, save_tickets, current_time

app = Flask(__name__)


@app.route("/")
def home():
    return "Customer Support System is running"


@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(load_tickets())


@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.json
    tickets = load_tickets()

    ticket = {
        "id": len(tickets) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "status": "Open",
        "priority": data.get("priority", "Medium"),
        "created_at": current_time(),
        "updated_at": current_time(),
        "messages": []
    }

    tickets.append(ticket)
    save_tickets(tickets)

    return jsonify({"message": "Ticket created", "ticket": ticket})


@app.route("/tickets/<int:ticket_id>/response", methods=["POST"])
def add_response(ticket_id):
    data = request.json
    tickets = load_tickets()

    for t in tickets:
        if t["id"] == ticket_id:
            t["messages"].append({
                "time": current_time(),
                "message": data.get("message")
            })
            t["updated_at"] = current_time()
            save_tickets(tickets)
            return jsonify({"message": "Response added"})

    return jsonify({"error": "Ticket not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
