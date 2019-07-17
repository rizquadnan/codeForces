player_pos = list(str(input()))

dangerous = "NO"
if player_pos.count("1") >= 7 or player_pos.count("0") >= 7:
    player_pos = [int(char) for char in player_pos]
    for idx in range(len(player_pos)):
        count = float('inf')
        count = sum(player_pos[idx:idx+7])
        if count == 7:
            dangerous = "YES"
            break
        elif count == 0 and ((idx + 7) <= len(player_pos)):
            dangerous = "YES"
            break
else:
    pass

print(dangerous)