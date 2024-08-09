# Prompt the user for the number of tables and the range for each table
o = int(input("Enter the number of multiplication tables you want to generate: "))
p = int(input("Enter the highest number to include in each table: "))

def multy(n, m):
    table = ""
    for i in range(1, m + 1):  # Ensure the range includes m
        table += f"{n} X {i} = {n * i}\n"
    # Open the file and write the complete table after generating it
    with open(f"table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables for numbers 1 through o
for n in range(1, o + 1):
    multy(n, p)
