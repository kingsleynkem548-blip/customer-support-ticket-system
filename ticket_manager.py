import json
import os
from datetime import datetime

FILE_NAME = "tickets.json"


def load_tickets():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tickets(tickets):
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_ticket():
    title = input("Enter issue title: ")
    description = input("Enter issue description: ")

    print("Select priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(input("Choose priority: "), "Medium")

    tickets = load_tickets()

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "status": "Open",
        "priority": priority,
        "created_at": current_time(),
        "updated_at": current_time(),
        "messages": []
    }

    tickets.append(ticket)
    save_tickets(tickets)

    print("✅ Ticket created.")


def view_tickets():
    tickets = load_tickets()

    if not tickets:
        print("No tickets found.")
        return

    # Sort by priority
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tickets.sort(key=lambda t: priority_order.get(t["priority"], 3))

    for t in tickets:
        print(f"\nID: {t['id']} | {t['priority']} | {t['status']}")
        print(f"Title: {t['title']}")
        print(f"Created: {t['created_at']}")


def update_ticket_status():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for t in tickets:
        if t["id"] == ticket_id:
            print("1. Open | 2. In Progress | 3. Closed")
            status_map = {
                "1": "Open",
                "2": "In Progress",
                "3": "Closed"
            }

            choice = input("Select new status: ")
            t["status"] = status_map.get(choice, t["status"])
            t["updated_at"] = current_time()

            save_tickets(tickets)
            print("✅ Status updated.")
            return

    print("Ticket not found.")


def add_response():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for t in tickets:
        if t["id"] == ticket_id:
            message = input("Enter response: ")

            t["messages"].append({
                "time": current_time(),
                "message": message
            })

            t["updated_at"] = current_time()
            save_tickets(tickets)

            print("💬 Response added.")
            return

    print("Ticket not found.")


def view_conversation():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for t in tickets:
        if t["id"] == ticket_id:
            print(f"\n=== Conversation for Ticket {ticket_id} ===")

            if not t["messages"]:
                print("No messages yet.")
                return

            for msg in t["messages"]:
                print(f"[{msg['time']}] {msg['message']}")
            return

    print("Ticket not found.")


def search_tickets():
    keyword = input("Search keyword: ").lower()
    tickets = load_tickets()

    results = [
        t for t in tickets
        if keyword in t["title"].lower() or keyword in t["description"].lower()
    ]

    if not results:
        print("No results.")
        return

    for t in results:
        print(f"\nID: {t['id']} | {t['status']} | {t['priority']}")
        print(f"Title: {t['title']}")


def delete_ticket():
    tickets = load_tickets()

    try:
        ticket_id = int(input("Enter ticket ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    updated = [t for t in tickets if t["id"] != ticket_id]

    if len(updated) == len(tickets):
        print("Ticket not found.")
        return

    save_tickets(updated)
    print("🗑️ Deleted.")
