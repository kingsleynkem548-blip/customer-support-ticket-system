from ticket_manager import (
    create_ticket,
    view_tickets,
    update_ticket_status,
    search_tickets,
    delete_ticket
)


def menu():
    while True:
        print("\n=== Customer Support Ticket System ===")
        print("1. Create new ticket")
        print("2. View all tickets")
        print("3. Update ticket status")
        print("4. Search tickets")
        print("5. Delete ticket")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
