import csv

# Открываем CSV файл для записи
with open("large_file.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Записываем заголовок
    writer.writerow(
        [
            "Column1",
            "Column2",
            "Column3",
        ]
    )

    # Записываем данные
    for i in range(10**6):
        writer.writerow([f"Row{i}", f"Value{i}", f"Value{i+1}"])
