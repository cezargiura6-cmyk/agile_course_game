from utils.read_game_data import read_game_data

def main():
   print("game running")
   print(read_game_data("data/monster_races.txt"))

if __name__ == "__main__":
   main()