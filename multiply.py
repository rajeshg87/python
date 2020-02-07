def print_multplication_table(table=5, start=1, end=10):
    for i in range(start, end+1):
        print(f"{table} X {i} = {table*i}")

print_multplication_table(6, 1, 12)
print("=======================")
print_multplication_table(9,1)
print("=======================")
print_multplication_table()
print("=======================")

