contents = []

file_names = ["file1.txt", "file2.txt", "file3.txt"]

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        line_count = len(file_content.split('\n'))
        contents.append((file_name, line_count, file_content))

contents.sort(key=lambda x: x[1])

combined_file_name = "combined.txt"
with open(combined_file_name, 'w') as combined_file:
    for file_info in contents:
        combined_file.write(f"File: {file_info[0]}\n Line Count: {file_info[1]}\n")
        combined_file.write(file_info[2])
        combined_file.write("\n\n")

print(f"Создан объединенный файл: {combined_file_name}")
