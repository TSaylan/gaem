def load(file):

    fileLenght = 1

    try:
        with open(file=file, mode="rt") as file:
            line = file.readlines()

    except FileNotFoundError:
        with open(file=file, mode="wt") as file:
            file.writelines("\n" * fileLenght)
        with open(file=file, mode="rt") as file:
            line = file.readlines()

    while len(line) < fileLenght:
        line.append("\n")

    for i in range(len(line)):
        line[i] = line[i].strip()
        if not line[i]:
            line[i] = 0

    return line

def save(file, line):
    with open(file=file, mode="wt") as file:
        for i in range(len(line)):
            file.writelines(str(line[i]).join("\n"))
