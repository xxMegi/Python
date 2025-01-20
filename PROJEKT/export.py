def export_to_file(file_format, data):

    if file_format == "txt":
        with open("books_database.txt", "w") as file:
            for record in data:
                file.write(f"{record}\n")

    elif file_format == "csv":
        import csv
        with open("books_database.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "TYTUŁ", "KATEGORIA", "AUTOR", "ROK"])
            writer.writerows(data)

    elif file_format == "json":
        import json
        with open("books_database.json", "w") as file:
            json.dump([{"ID": r[0], "TYTUŁ": r[1], "GATUNEK": r[2], "AUTOR": r[3], "ROK": r[4]} for r in data], file, indent=4)

    else:
        print("Ten format pliku jest nieobsługiwany. Przepraszamy!")
