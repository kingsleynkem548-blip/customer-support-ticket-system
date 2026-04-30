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

    tickets = load_tickets()

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "description": description,
        "status": "Open"
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

            if choice == "1":
                ticket["status"] = "Open"
            elif choice == "2":
                ticket["status"] = "In Progress"
            elif choice == "3":
                ticket["status"] = "Closed"
            else:
                print("Invalid choice.")
                return

            save_tickets(tickets)
            print("✅ Ticket updated.")
            return

    print("Ticket not found.")
