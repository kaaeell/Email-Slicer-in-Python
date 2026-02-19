import re
import argparse
import json
from datetime import datetime


def is_valid_email(email: str) -> bool:
    """Check if the email format looks valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def parse_email(email: str):
    """Split email into username, domain and extension."""
    username, rest = email.split("@")
    domain, extension = rest.rsplit(".", 1)
    return username, domain, extension


def mask_username(username: str) -> str:
    """Hide part of the username for privacy."""
    if len(username) <= 2:
        return "*" * len(username)
    return username[0] + "*" * (len(username) - 2) + username[-1]


def save_to_json(data: dict):
    """Append results to a JSON file."""
    filename = "email_results.json"
    try:
        with open(filename, "a") as file:
            json.dump(data, file)
            file.write("\n")
        print(f"Saved to {filename}")
    except Exception as e:
        print("Something went wrong while saving:", e)


def show_result(username, domain, extension, mask=False):
    if mask:
        username = mask_username(username)

    print("\n--- Email Info ---")
    print(f"Username  : {username}")
    print(f"Domain    : {domain}")
    print(f"Extension : .{extension}")


def process_email(email: str, mask=False, save=False):
    if not is_valid_email(email):
        print("Invalid email format.")
        return

    username, domain, extension = parse_email(email)
    show_result(username, domain, extension, mask)

    if save:
        data = {
            "email": email,
            "username": username,
            "domain": domain,
            "extension": extension,
            "time": datetime.now().isoformat()
        }
        save_to_json(data)


def interactive_mode():
    print("Email Slicer (type 'exit' to quit)\n")
    while True:
        email = input("Enter an email: ").strip()
        if email.lower() == "exit":
            print("Bye 👋")
            break
        process_email(email)


def main():
    parser = argparse.ArgumentParser(description="Simple Email Slicer Tool")
    parser.add_argument("-e", "--email", help="Email address to process")
    parser.add_argument("-m", "--mask", action="store_true", help="Mask the username")
    parser.add_argument("-s", "--save", action="store_true", help="Save result to JSON")

    args = parser.parse_args()

    if args.email:
        process_email(args.email, args.mask, args.save)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
