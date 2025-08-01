users = input().split()
movies = input().split()
view_history = {user: input().split()[2:] for user in users}

view_all_films = list(filter(
    lambda user: len(view_history[user]) == len(movies),
    view_history
))

print("YES" if len(view_all_films) == len(users) else "NO")
