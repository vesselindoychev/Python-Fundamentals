row_one = list(map(int, input().split()))
row_two = list(map(int, input().split()))
row_three = list(map(int, input().split()))

winner = ""

if row_one[0] == row_one[1] == row_one[2] == 1 or \
    row_two[0] == row_two[1] == row_two[2] == 1 or \
    row_three[0] == row_three[1] == row_three[2] == 1 or \
    row_one[0] == row_two[0] == row_three[0] == 1 or \
    row_one[1] == row_two[1] == row_three[1] == 1 or \
    row_one[2] == row_two[2] == row_three[2] == 1 or \
    row_one[0] == row_two[1] == row_three[2] == 1 or \
    row_one[2] == row_two[1] == row_three[0] == 1:

    winner = "First player won"

elif row_one[0] == row_one[1] == row_one[2] == 2 or \
    row_two[0] == row_two[1] == row_two[2] == 2 or \
    row_three[0] == row_three[1] == row_three[2] == 2 or \
    row_one[0] == row_two[0] == row_three[0] == 2 or \
    row_one[1] == row_two[1] == row_three[1] == 2 or \
    row_one[2] == row_two[2] == row_three[2] == 2 or \
    row_one[0] == row_two[1] == row_three[2] == 2 or \
    row_one[2] == row_two[1] == row_three[0] == 2:

    winner = "Second player won"

else:
    winner = "Draw!"
print(winner)
