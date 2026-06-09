
# Problem 5: Game Scoreboard (*args + global list + nested logic)
# ---------------------------------------------------------------
# Define a GLOBAL leaderboard:

#     high_score_board = []     # list of (player, total) tuples

# Write `record_game(player, *scores, bonus=0, multiplier=1.0)` that:
#   - Takes a player name (positional).
#   - Takes ANY NUMBER of round scores using `*scores`.
#   - Takes optional `bonus` (added to total) and `multiplier`
#     (applied at the end).
#   - APPENDS the result to the global leaderboard.
#   - Returns FOUR values: `(player, rounds, total, status)`

# Rules:
#     no scores at all          → (player, 0, 0, "no rounds played")
#     any negative score        → (player, 0, 0, "negative score not allowed")
#     otherwise:
#         raw_total = sum(scores)
#         total = int((raw_total + bonus) * multiplier)
#         rounds = number of scores given
#         append (player, total) to high_score_board
#         figure out rank by sorting the board:
#             rank 1 → status = "high score!"
#             otherwise → status = "rank N"

# Add a docstring documenting *args and keyword args.

# In your main code, call the function for at least 3 players and
# print the final leaderboard.

#============================================================================================
# Solution:
#============================================================================================

high_score_board = []


def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Records a player's game result.
    *scores:
        Any number of round scores.
    keyword args:
        bonus: extra points added to the total.
        multiplier: number applied to the total at the end.
    """

    if len(scores) == 0:
        return player, 0, 0, "no rounds played"

    for score in scores:
        if score < 0:
            return player, 0, 0, "negative score not allowed"

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    def get_score(item):
        return item[1]

    sorted_board = sorted(
        high_score_board,
        key=get_score,
        reverse=True
    )

    rank = sorted_board.index((player, total)) + 1

    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return player, rounds, total, status


print(record_game("Nouf", 10, 20, 30))
print(record_game("Sara", 15, 25, bonus=10))
print(record_game("Lama", 40, 50, multiplier=1.5))

print("Final leaderboard:")
print(high_score_board)