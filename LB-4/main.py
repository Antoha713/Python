csv_url = "https://informer.com.ua/dut/python/import/129-indeksi-tsin-na-zhitlo.csv"

# Створення екземпляра класу та читання даних
csv_reader = CsvReader()
data = csv_reader.read_data(csv_url)

print(data[:3])  # Виводимо перші три записи для перевірки
