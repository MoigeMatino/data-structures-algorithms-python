def knightly_number(n:int, m:int, kr:int, kc:int, pr:int, pc:int) -> int:
    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0
    
    if m == 0:
        if kr == pr and kc == pc:
            return 1
        else:
            return 0
        
    movements = [
        (kr+1, kc+2),
        (kr+1, kc-2),
        (kr-1, kc+2),
        (kr-1, kc-2),
        (kr+2, kc+1),
        (kr+2, kc-1),
        (kr-2, kc+1),
        (kr-2, kc-1),
    ]
    count = 0
    for movement in movements:
        pos_r, pos_c = movement
        count += knightly_number(n, m-1, pos_r, pos_c, pr, pc)

    return count

