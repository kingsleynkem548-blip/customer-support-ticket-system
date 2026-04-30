from ticket_manager import (
    create_ticket,
    view_tickets,
    update_ticket_status,
    search_tickets,
    delete_ticket,
    add_response,
    view_conversation
)


def menu():
    while True:
        print("\n=== Customer Support System ===")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Status")
        print("4. Search Tickets")
        print("5. Delete Ticket")
        print("6. Add Response")
        print("7. View Conversation")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket_status()
        elif choice == "4":
            search_tickets()
        elif choice == "5":
            delete_ticket()
        elif choice == "6":
            add_response()
        elif choice == "7":
            view_conversation()
        elif choice == "8":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
