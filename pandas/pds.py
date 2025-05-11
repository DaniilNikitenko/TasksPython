import pandas as pd
import re

# data = {
#     "Имя": ["Аня", "Борис", "Виктор"],
#     "Возраст": [23, 34, 45],
#     "Город": ["Москва", "Петербург", "Новосибирск"],
# }

# products = {
#     "Товар": ["Телевизор", "Ноутбук", "Телефон", "Кухонный комбайн", "Микроволновка"],
#     "Цена": [1500, 2500, 800, 1200, 3000],
#     "Дата покупки": [
#         "2025-02-01",
#         "2025-01-15",
#         "2025-03-10",
#         "2025-01-20",
#         "2025-01-20",
#     ],
# }


# df = pd.DataFrame(data)

# df2 = pd.DataFrame(products)
# df2["Дата покупки"] = pd.to_datetime(df2["Дата покупки"])
# print(df2)
# filtered_df = df2[(df2["Цена"] > 2000) & (df2["Дата покупки"] > "2025-01-01")]
# # filtered_df = df[df["Возраст"] > 30]

# print(filtered_df)


# data = {
#     "Студент": ["Аня", "Борис", "Виктор", "Аня", "Виктор"],
#     "Предмет": ["Математика", "Математика", "Математика", "Физика", "Физика"],
#     "Оценка": [5, 4, 3, 5, 4],
# }

# df = pd.DataFrame(data)

# # Группировка по предмету и вычисление среднего балла
# average_scores = df.groupby("Студент")["Оценка"].mean()

# print(average_scores)


# data1 = {
#     "Имя": ["Аня", "Борис", "Виктор"],
# }


# df1 = pd.DataFrame(data1)
# print(f"df1:\n{df1}\n\n")
# # Второй DataFrame
# data2 = {
#     "Город": ["Москва", "Петербург", "Новосибирск"],
# }

# df2 = pd.DataFrame(data2)
# print(f"df2:\n{df2}\n\n")

# # Объединение DataFrame по ID
# merged_df = pd.concat([df1, df2], axis=1)
# merged_df = df1.merge(df2, how="cross")

# print(merged_df)


# data = {
#     "Имя": ["Аня", "Борис", "Виктор", "Алекс"],
#     "Возраст": [23, None, 45, 34],
#     "Город": ["Москва", "Петербург", None, "Новосибирск"],
# }

# df = pd.DataFrame(data)

# # Заполнение пропусков средним значением для числовых столбцов
# df["Возраст"] = df["Возраст"].fillna("Не указан")

# # Заполнение пропусков строками
# df["Город"] = df["Город"].fillna("Не указан")

# print(df)


# data = {
#     "Имя": ["Аня", "Борис", "Виктор", "Михаил"],
#     "Возраст": [23, None, 45, 34],
#     "Город": [None, None, None, None],
# }

# df = pd.DataFrame(data)

# print(f"firstdf\n\n{df}\n\n\n\n")
# # Удаление строк с пропущенными значениями


# # Удаление столбцов, в которых все значения NaN
# df_cleaned = df.dropna(axis=1, how="all")

# print(df_cleaned)

# # df_filled = df.fillna(
# #     {"Имя": "Неизвестно", "Возраст": "Не указан", "Город": "Не указан"}
# # )


# wine_reviews = pd.read_csv("large_file.csv")


# # Чтобы получить столбец с помощью iloc, можно сделать следующее:

# print(wine_reviews.iloc[:, 0])


# # только для первой, второй и третьей строки, нужно сделать так:
# print(wine_reviews.iloc[:3, 0])


# # Или, чтобы выбрать только вторую и третью записи, можно использовать:
# print(wine_reviews.iloc[1:3, 0])


# # Также можно передавать список:
# print(wine_reviews.iloc[[0, 1, 2], 0])


# # чтобы получить последние пять элементов из набора данных:
# print(wine_reviews.iloc[-5:])


# Например, чтобы получить первую запись из reviews, мы используем:

# print(wine_reviews.loc[0, "Column1"])


# Поскольку в вашем наборе данных обычно есть осмысленные индексы, проще использовать loc.
# Например, вот операция, которая гораздо проще с использованием loc:

# print(wine_reviews.loc[:, ["Column2", "Column3"]])

# print(wine_reviews["Column1"] == "Row0")

# print(wine_reviews.loc[wine_reviews["Column1"] == "Row0"])

# print(wine_reviews.loc[wine_reviews["Column1"].isin(["Row9", "Row999995"])])


# CSV
# df = pd.read_csv("pokemon_data.csv")
# print(df)

# print(df.head(3))

# print(df.tail(3))


# XLSX
# df_xlsx = pd.read_excel("pokemon_data.xlsx")

# print(df_xlsx)


# TXT
# df_text = pd.read_csv("pokemon_data.txt", delimiter="\t")
# print(df_text.head(3))


# Read headers
# df = pd.read_csv("pokemon_data.csv")
# print(df.columns)


df = pd.read_csv("pokemon_data.csv")
print(df)

# Read each column
print(df["Name"])
print(df["Name"][0:5])
print(df[["Name", "Type 1", "HP"]][0:3])

# Read each row

print(df.iloc[0])
print(df.iloc[1:4])

# Just a name
# for index, row in df.iterrows():
#     print(index, row["Name"])

# Read a specific Location
print(df.iloc[2, 1])


# loc
# Выводим всех у кого Type 1 Fire
print(df.loc[df["Type 1"] == "Fire"])


# describe()

print(df.describe())

new_df = df.loc[df["Type 1"] == "Fire"]
print(new_df.describe())


# sort

print(df.sort_values("Name"))
print(df.sort_values("Name", ascending=False))
print(df.sort_values(["Name", "HP"]))


# Making changes to the data

df["Total"] = (
    df["HP"]
    + df["Attack"]
    + df["Defense"]
    + df["Sp. Atk"]
    + df["Sp. Def"]
    + df["Speed"]
)

print(df.head(5))

df = df.drop(columns=["Total"])


print(df.head(5))


df["Total"] = df.iloc[:, 4:-2].sum(axis=1)  # Total по умолчанию в конец

cols = list(df.columns)
print(cols)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]  # Totak перед HP
print(df.head(5))


print(df)

# Save

# df.to_csv("new_data.csv")
# df.to_excel("new_data.xlsx", index=False)


# Filtering data

df2 = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]
# df2 = df2.reset_index(drop=True)  # Можно так
df2.reset_index(drop=True, inplace=True)  # или так
print(df2)

print(
    df.loc[df["Name"].str.contains("Mega")]
)  # Получаем все столбцы где Name содержит Mega
print(
    df.loc[~df["Name"].str.contains("Mega")]
)  # Получаем все столбцы где Name не содержит Mega


print(
    df.loc[df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)]
)  # Использование регулярных выражений

print(df.loc[df["Name"].str.contains("^p[a-z]*", flags=re.I, regex=True)])  # На p

df.loc[df["Type 1"] == "Fire", "Type 1"] = (
    "Flamer"  # Заменяем Fire в стоблце Type 1 на Flamer
)

# df.loc[df["Total"] > 500, ["Genetation", "Legendary"]] = "Test"

# df.loc[df["Total"] > 500, ["Genetation", "Legendary"]] = ["Test", "test2"]


# Groupby

print(df)
print(df.groupby(["Type 1"]).mean(numeric_only=True))

df["Count"] = 1

print(df.groupby(["Type 1"]).count()["Count"])
