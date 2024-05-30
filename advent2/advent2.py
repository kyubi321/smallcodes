def advent2():
    limits = {
        "blue": 14,
        "red": 12,
        "green": 13
    }
    possible_games = []
    with open("text.txt", "r") as file:
        for inputstring in file:

            # splitting the game string
            game_id, subsets = inputstring.split(":")
            game_id = int(game_id.replace("Game", ""))
            possible = True

            for each_set in subsets.split(";"):
                if not possible:
                    break

                for colour_pair in each_set.split(','):
                    if not possible:
                        break
                    num, colour = colour_pair.strip().split()
                    if int(num) > limits[colour]:
                        possible_games.append(game_id)
    return sum(possible_games)


print(advent2())
