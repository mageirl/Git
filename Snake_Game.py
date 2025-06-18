import random

def roll_dice():
    return random.randint(1, 6)

def generate_random_board(width, height, num_snakes=8, num_ladders=8):
    max_pos = width * height
    snakes = {}
    ladders = {}
    all_used = set()

    def valid_pair(start, end, is_ladder):
        if start == end or start in all_used or end in all_used:
            return False
        return (start < end) if is_ladder else (start > end)

    while len(snakes) < num_snakes:
        head = random.randint(width + 1, max_pos - 1)
        tail = random.randint(1, head - 1)
        if valid_pair(head, tail, is_ladder=False):
            snakes[head] = tail
            all_used.update([head, tail])

    while len(ladders) < num_ladders:
        bottom = random.randint(1, max_pos - width - 1)
        top = random.randint(bottom + 1, max_pos)
        if valid_pair(bottom, top, is_ladder=True):
            ladders[bottom] = top
            all_used.update([bottom, top])

    return snakes, ladders

def move_player(position, roll, snakes, ladders, max_pos):
    new_pos = position + roll
    if new_pos > max_pos:
        return position
    if new_pos in snakes:
        print(f"Bitten by a snake! {new_pos} > {snakes[new_pos]}")
        new_pos = snakes[new_pos]
    elif new_pos in ladders:
        print(f"Climbed a ladder! {new_pos} > {ladders[new_pos]}")
        new_pos = ladders[new_pos]
    return new_pos

def display_board(positions, width, height):
    max_pos = width * height
    print("\n" + "-" * (width * 7 + 1))
    for row in range(height, 0, -1):
        line = ""
        rng = range((row - 1) * width + 1, row * width + 1)
        if row % 2 == 0:
            rng = reversed(rng)
        for i in rng:
            cell = ""
            players_here = [f"P{idx+1}" for idx, pos in enumerate(positions) if pos == i]
            if players_here:
                cell = ",".join(players_here)
            else:
                cell = str(i)
            line += f"|{cell:^5}"
        line += "|"
        print(line)
        print("-" * (width * 7 + 1))

def play_game():
    print("Welcome to Custom Snakes and Ladders!")
    if input('Do you want to play on a preset board? (type "yes" or anything else if you dont want to)') == 'yes':
        width = 10
        height = 10
        max_pos = 100
        snakes = {
            16:6,
            46:25,
            49:11,
            62:19,
            64:60,
            74:53,
            89:68,
            92:88,
            95:75,
            99:80
        }
        ladders = {
            2:38,
            7:14,
            8:31,
            15:26,
            21:42,
            28:84,
            36:44,
            51:67,
            71:91,
            78:98,
            87:94
        }

    else:
        width = int(input("Enter board width (e.g., 10): "))
        height = int(input("Enter board height (e.g., 10): "))
        max_pos = width * height

        num_snakes = int(input("Number of snakes (e.g., 8): "))
        num_ladders = int(input("Number of ladders (e.g., 8): "))

        snakes, ladders = generate_random_board(width, height, num_snakes, num_ladders)

    while num_players < 2:
        try:
            num_players = int(input("Enter number of players (2+): "))
        except Exception:
            print('Incorrect input')
            
    print("\nGame setup complete!")
    print(f"Snakes: {snakes}")
    print(f"Ladders: {ladders}\n")

    positions = [1] * num_players
    player = 0

    while True:
        display_board(positions, width, height)
        input(f"Player {player + 1}, press Enter to roll the dice...")
        roll = roll_dice()
        print(f"Player {player + 1} rolled a {roll}")
        new_pos = move_player(positions[player], roll, snakes, ladders, max_pos)
        print(f"Player {player + 1} moves to {new_pos}")

        for i, pos in enumerate(positions):
            if i != player and pos == new_pos:
                print(f"Collision! Player {i + 1} is pushed back by 1 tile.")
                positions[i] = max(1, positions[i] - 1)

        positions[player] = new_pos

        if positions[player] == max_pos:
            display_board(positions, width, height)
            print(f"Player {player + 1} wins! 🎉")
            break

        player = (player + 1) % num_players


play_game()
