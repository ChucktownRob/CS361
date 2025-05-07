# Used text-ASCII art gen at url: https://www.asciiart.eu/text-to-ascii-art

from vault import VideoVault
import time, sys
import os


def main():

    vault = VideoVault()

    banner()

    while True:
        print("\nOptions:")
        print("1. Add a new video")
        print("2. Search videos")
        print("3. List all videos")
        print("4. About")
        print("5. Exit\n")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            # clear_lines(8) - suppressed for now
            print("Enter the following information to add to the catalog.")
            print("Please be as accurate as you can...")
            title = input("Title: ")
            format_ = input("Format (DVD, Blu-Ray, VHS): ")
            year = input("Year of Film Release: ")
            adds = vault.add_video(title, format_, year)
            if adds == 1:
                print("\nVideo added!")
            else:
                print("\nVideo already exists by that title. Try Option #2 or")
                print("Option #3 in the menu.")

        elif choice == '2':
            query = input("Search by Title, Format, or Year: ")
            results = vault.search(query)
            if len(results) == 0:
                print(f"\nThere were no results found from '{query}'.")
            else:
                print(f"\nFound {len(results)} result(s):")
                print_dict_table(results)

        elif choice == '3':
            # clear_lines(8) - suppressed for now
            videos = vault.list_all()
            if len(videos) == 0:
                print("\nSorry, but the vault is empty!")
            else:
                print_dict_table(videos)

        elif choice == '4':
            # clear_lines(8) - suppressed for now
            with open('about_text.txt', 'r') as file:
                file_content = file.read()
            print_letter_by_letter(file_content)

        elif choice == '5':
            print("Goodbye! Hope to see you again, soon!\n")
            break
        else:
            print("\nInvalid option. Try again!")


def banner():
    store_sign = """
    +========================================================+
    | _____  _             _____             _    _  _       |
    ||_   _|| |__    ___  |_   _|__ _   ___ | |_ (_)| |  ___ |
    |  | |  | '_ \  / _ \   | | / _` | / __|| __|| || | / _ \|
    |  | |  | | | ||  __/   | || (_| || (__ | |_ | || ||  __/|
    |  |_|  |_| |_| \___|   |_| \__,_| \___| \__||_||_| \___||
    |  ____  _                      _      _  _              |
    | / ___|(_) _ __    ___  _ __  | |__  (_)| |  ___        |
    || |    | || '_ \  / _ \| '_ \ | '_ \ | || | / _ \       |
    || |___ | || | | ||  __/| |_) || | | || || ||  __/       |
    | \____||_||_| |_| \___|| .__/ |_| |_||_||_| \___|       |
    |                       |_|                              |
    +========================================================+
    """
    print(store_sign)


def clear_lines(n):
    if os.name == 'nt':  # For Windows
        os.system(f'mode con: cols=79 lines={n}')
        for _ in range(n):
            print("\033[F\033[K", end="")
    else:  # For Unix-like systems (Linux, macOS)
        print(f"\033[{n}F\033[J", end="")


def print_dict_table(data):
    headers = list(data[0].keys())
    column_widths = {header: len(header) for header in headers}
    for row in data:
        for header, value in row.items():
            column_widths[header] = max(column_widths[header], len(str(value)))

    # Print header
    for header in headers:
        print(f"{header:<{column_widths[header]}}", end="  ")
    print()

    # Print separator
    for header in headers:
        print("-" * column_widths[header], end="--")
    print()

    # Print data
    for row in data:
        for header in headers:
            print(f"{str(row.get(header, '')): <{column_widths[header]}}",
                  end="  ")
        print()


def print_letter_by_letter(text, delay=0.1):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(1)
    print()


if __name__ == "__main__":
    main()
