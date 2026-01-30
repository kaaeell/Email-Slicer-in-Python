print("\nEMAIL SLICER TOOL\n")
while True:
    email = input("Enter your email address: ").strip()

    if "@" not in email or email.count("@") != 1:
        print("Invalid email format")
    else:
     username, domain = email.split("@")

    if "." not in domain:
        print("Invalid email domain")
    else:
        domain_name, extension = domain.split(".", 1)

        print("\nEmail Details:")
        print(f"Username      : {username}")
        print(f"Domain Name   : {domain_name}")
        print(f"Extension     : {extension}")

        choice = input("\nDo you want to check another email? (y/n): ").lower()

    if choice != "y":
        print("Goodbye!")
        break

           
