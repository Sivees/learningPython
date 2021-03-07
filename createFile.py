height = 20
side = height - 1
stars = '*'
i = 1

while i <= height:
    star_side = ' ' * side
    print(star_side + stars + star_side)
    stars += '**'
    i += 1
    side -= 1
