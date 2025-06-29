def blocking_spot(pos1, pos2):
    winning_lines = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for line in winning_lines:
        if pos1 in line and pos2 in line:
            for spot in line:
                if spot != pos1 and spot != pos2:
                    return spot
    return None