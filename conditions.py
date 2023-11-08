winners_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                        [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def who_win(locations):

    numbers_x = [numbers for numbers in locations if locations[numbers] == "X"]
    numbers_o = [numbers for numbers in locations if locations[numbers] == "O"]

    if len(numbers_o) >= 5 or len(numbers_x) >= 5:
        print("This is a draw!")
    else:
        for _ in range(8):
            winning_numbers = set(numbers_x) & set(winners_combinations[_])  # look for matches between lists
            if len(winning_numbers) == 3:
                print("player 1 wins")
                return True

            winning_numbers = set(numbers_o) & set(winners_combinations[_])
            if len(winning_numbers) == 3:
                print("player 2 wins")
                return False
