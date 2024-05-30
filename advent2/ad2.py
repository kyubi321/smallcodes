def advent2():
    limits = {
        "blue": 14,
        "red": 12,
        "green": 13
    }
    possible_games = []

    with open("text.txt", "r") as file:
        for inputstring in file:
            # Splitting the game string
            game_id, subsets = inputstring.split(":")
            game_id = int(game_id.replace("Game", ""))

            for each_set in subsets.split(";"):
                # Check if each_set is not an empty string
                if each_set.strip():
                    for colour_pair in each_set.split(","):
                        num, colour = colour_pair.strip().split()
                        if int(num) > limits[colour]:
                            possible_games.append(game_id)
                            print(possible_games)

    return sum(possible_games)


print(advent2())
