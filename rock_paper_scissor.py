import random
options = ["ROCK", "PAPER", "SCISSOR"]
IA_pick = options[random.randint(0, len(options)-1)]


def Is_playable(pick):
    if pick not in options: return False
    return True


def Player_win(player_pick, IA_pick = IA_pick):
    if not Is_playable(player_pick): return "Vous n'avez pas écrit un mot valide"

    if options.index(player_pick) == options.index(IA_pick): return "égalité"

    if player_pick == options[0] and IA_pick == options[len(options)-1]: return "Vous avez gagné"
    if player_pick == options[len(options)-1] and IA_pick == options[0]: return "Vous avez perdu"
    
    if options.index(player_pick) < options.index(IA_pick) : return "Vous avez perdu"
    return "Vous avez gagné"
    

def main():
    player_pick = input(f"select {options} :").upper()
    print(f"{Player_win(player_pick)}")
    print(f"player : '{player_pick}', IA : '{IA_pick}'")


if __name__ == "__main__":
    main()