import random

# Snakes and Ladders configuration (from image)
snakes = {
    99: 7,
    92: 35,
    89: 53,
    76: 58,
    73: 15,
    62: 19,
    49: 11,
    46: 25,
    16: 6
}

ladders = {
    4: 25,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 91
}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    position += roll
    if position > 100:
        return position - roll  # must land exactly on 100
    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}. Going down to {snakes[position]}.")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder from {position} to {ladders[position]}.")
        position = ladders[position]
    return position

def display_board(p1_pos, p2_pos):
    print("\n" + "-" * 66)
    for row in range(10, 0, -1):
        line = ""
        rng = range((row - 1) * 10 + 1, row * 10 + 1)
        if row % 2 == 0:
            rng = reversed(rng)
        for i in rng:
            cell = f"{i:>3}"
            markers = []
            if i == p1_pos:
                markers.append("P1")
            if i == p2_pos:
                markers.append("P2")
            if markers:
                cell = "".join(markers).ljust(3)
            line += f"|{cell:^5}"
        line += "|"
        print(line)
        print("-" * 66)

def play_game():
    positions = [1, 1]
    player = 0

    print("🎲 Welcome to Snakes and Ladders!")
    print("Reach exactly 100 to win.\n")

    while True:
        display_board(positions[0], positions[1])
        input(f"Player {player + 1}, press Enter to roll the dice...")
        roll = roll_dice()
        print(f"Player {player + 1} rolled a {roll}.")
        new_pos = move_player(positions[player], roll)
        print(f"Player {player + 1} moves from {positions[player]} to {new_pos}.\n")
        positions[player] = new_pos

        if positions[player] == 100:
            display_board(positions[0], positions[1])
            print(f"🎉 Player {player + 1} wins! 🎉")
            break

        player = 1 - player  # switch turn

if __name__ == "__main__":
    play_game()
