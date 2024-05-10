def hero(bullets, dragons):
    bullets_for_dragons = 2 * dragons
    if bullets>bullets_for_dragons or bullets==bullets_for_dragons:
        return True
    else:
        return False
