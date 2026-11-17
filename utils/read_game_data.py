def read_game_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines