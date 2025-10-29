
def HandleSetting(file_path) -> list:
    settings = []
    with open(file_path, "r") as txt:
        for line in txt:
            line = line.rstrip()
            line = line.split(" ")
            settings.append(line)
    return settings
