import json
import os

FILE_NAME = "tickets.json"


def load_tickets():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tickets(tickets):
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


def create_ticket():
    title = input("Enter issue title: ")
    description = input("Enter issue description: ")

    print("Select priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Choose priority: ")

    priority_map = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    priority = priority_map.get(priority_choice, "Medium")

    tickets = load_tickets()

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "status": "Open",
        "priority": priority
    }

    tickets.append(ticket)
    save_tickets(tickets)

    print("✅ Ticket created successfully.")


def view_tickets():
    tickets = load_tickets()

    if not tickets:
        print("No tickets found.")
        return

    for ticket in tickets:
        print(f"\nID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")
        print(f"Status: {ticket['status']}")
        print(f"Priority: {ticket['priority']}")


def update_ticket_status():
    tickets = load_tickets()

    if not tickets:
        print("No tickets to update.")
        return

    try:
        ticket_id = int(input("Enter ticket ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            print("1. Open")
            print("2. In Progress")
            print("3. Closed")

            choice = input("Select new status: ")

            status_map = {
                "1": "Open",
                "2": "In Progress",
                "3": "Closed"
            }

            ticket["status"] = status_map.get(choice, ticket["status"])

            save_tickets(tickets)
            print("✅ Ticket updated.")
            return

    print("Ticket not found.")


def search_tickets():
    keyword = input("Enter keyword to search: ").lower()
    tickets = load_tickets()

    results = [
        t for t in tickets
        if keyword in t["title"].lower() or keyword in t["description"].lower()
    ]

    if not results:
        print("No matching tickets found.")
        return

    for ticket in results:
        print(f"\nID: {ticket['id']}")
        print(f"Title: {ticket['title']}")
        print(f"Status: {ticket['status']}")
        print(f"Priority: {ticket['priority']}")


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
    print("🗑️ Ticket deleted.")
