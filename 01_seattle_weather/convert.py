# DO NOT RUN THIS FILE. THIS IS ONLY FOR CONVERTING THE DATA.

with open('cleaned_weather.csv', 'r') as infile:
    lines = infile.readlines()

with open('init-mysql.sql', 'a') as outfile:
    l = len(lines)
    for i in range(1, l):
        outfile.write(f"INSERT INTO weather VALUES ({lines[i].strip()});\n")
