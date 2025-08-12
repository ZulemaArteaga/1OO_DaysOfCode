# Modifying Global Scope

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")