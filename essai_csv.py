import csv


file = open(r'C:/Users/rbent/Desktop/git_repository/projet3_DA_Python/structure.csv')

try:
    reader = csv.reader(file)
    for row in reader:
        print(row)
finally:
    file.close()