from tabulate import tabulate  # install using "pip install tabulate"
import sys
import csv
import glob
import pandas as pd  # install using "pip install pandas"


def main():
    key = get_key()
    switch(key)


def get_key():
    instruction_list = [
        ["C", "CREATE NEW WATCHLIST"],
        ["A", "ADD TO A WATCHLIST"],
        ["V", "VIEW A WATCHLIST"],
        ["D", "DELETE FROM WATCHLIST"],
        ["U", "UPDATE A WATCHLIST"],
        ["E", "EXIT PROGRAM"],
    ]
    keys_list = ["A", "V", "D", "U", "E", "C"]
    print()
    print("INFO:")
    print(
        tabulate(
            instruction_list, headers=["KEY", "ACTION"], tablefmt="rounded_outline"
        )
    )
    key = input("Please Input a key: ").upper()
    if key in keys_list:
        return key
    else:
        sys.exit("Invalid Key")


def switch(key) -> None:
    if key == "C":
        name = input("Name the Watchlist: ")
        if check_input(name):
            key_C(name)
            main()
        else:
            sys.exit("CSV File already exists")

    elif key == "A":
        name = input("Watchlist to add to: ")
        if check_input(name):
            sys.exit("File Doesnt exist")
        print(view(name))
        sno = int(input("Enter SNO: "))
        _name = input("Enter the name of the Show/Movie: ")
        status = input("Status (Completed, On Hold, Dropped): ")
        rating = float(input("Rate the Show/Movie: "))
        key_A(name, sno, _name, status, rating)
        main()

    elif key == "V":
        name = input("Watchlist to View: ")
        if check_input(name):
            sys.exit("Watchlist does not exist")
        print(view(name))
        main()

    elif key == "D":
        name = input("Watchlist Name: ")
        if check_input(name):
            sys.exit("Watchlist does not exist")
        print(view(name))
        row = int(input("Enter the SNo to Delete: "))
        key_D(name, row)
        main()

    elif key == "U":
        name = input("Watchlist to Update: ")
        if check_input(name):
            sys.exit("Watchlist does not exist")
        print(view(name))
        update = input("What to Update(Name, Status, Rating): ").capitalize()
        sno = int(input(f"SNO of the {update}: "))
        update_ = input(f"Update {update} on SNo.{sno} to: ")
        key_U(name, update, sno, update_)
        main()

    elif key == "E":
        sys.exit("You've exited the program")


def key_A(name, sno, _name, status, rating) -> None:
    try:
        with open(f"{name}.csv", "a") as file:
            writer = csv.DictWriter(
                file, fieldnames=["SNO", "Name", "Status", "Rating"]
            )
            writer.writerow(
                {"SNO": sno, "Name": _name, "Status": status, "Rating": rating}
            )
    except:
        sys.exit("Invalid Entry")


def key_C(name) -> None:
    with open(f"{name}.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["SNO", "Name", "Status", "Rating"])
        writer.writerow(
            {"SNO": "SNO", "Name": "Name", "Status": "Status", "Rating": "Rating"}
        )


def view(name):
    contents = []
    with open(f"{name}.csv") as file:
        reader = csv.reader(file)
        for i in reader:
            contents.append(i)
    return tabulate(contents, headers="firstrow", tablefmt="rounded_outline")


def key_D(name, row) -> None:
    df = pd.read_csv(f"{name}.csv", index_col="SNO")
    df = df.drop(row)
    df.to_csv(f"{name}.csv", index=True)


def key_U(name, update, sno, update_) -> None:
    df = pd.read_csv(f"{name}.csv", index_col="SNO")
    df.at[sno, update] = update_
    df = df.reset_index()
    df.to_csv(f"{name}.csv", index=False)


def check_input(name):
    List_Of_Files = glob.glob("*.csv")
    if len(List_Of_Files) > 0:
        if f"{name}.csv" not in List_Of_Files:
            return True
    else:
        return True


if __name__ == "__main__":
    main()
