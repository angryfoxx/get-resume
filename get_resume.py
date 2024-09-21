import argparse
import json
import textwrap

BOLD = "\033[1m"
RESET = "\033[0m"


def print_profile(json_data):
    print(f"\n{BOLD}{json_data['name']} ― {json_data['title']} 🚀{RESET}\n")

    description = textwrap.fill(
        json_data["description"],
        width=100,
        subsequent_indent="  ",
    )
    print(f"  {description}\n")

    print(f"{BOLD}Abilities and Tech Stack 💻{RESET}\n")

    for ability, items in json_data["abilities"].items():
        print(f"  • {BOLD}{ability}{RESET}: {', '.join(items)}")

    print(f"\n{BOLD}Education 🎓{RESET}\n")
    for education in json_data["educations"]:
        school, degree, duration = (
            education["school"],
            education["degree"],
            education["duration"],
        )
        print(f"  • {BOLD}{degree}{RESET}: {school}, {duration}")

    print(f"\n{BOLD}Contact ☎️{RESET}\n")
    for contact_type, contact_value in json_data["contacts"].items():
        print(f"  • {BOLD}{contact_type}{RESET}: {contact_value}")


def main():
    parser = argparse.ArgumentParser(
        description="Print profile information dynamically from JSON file"
    )
    parser.add_argument(
        "--username",
        "-u",
        help="The username of the profile",
        type=str,
    )
    args = parser.parse_args()

    with open("profiles.json") as f:
        data = json.load(f)

    username = args.username
    if username not in data:
        print(f"Profile for {username} not found.")
        return

    print_profile(data[username])
    print()


if __name__ == "__main__":
    main()
