def life_in_weeks(year):
    life_span = 90
    life_left = life_span - year
    weeks_in_life = round(365/7) * life_left
    return f"You have {weeks_in_life} left"


print(life_in_weeks(70))
