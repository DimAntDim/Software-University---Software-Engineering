country = input().split(', ')
capitals = input().split(', ')
print(*[f"{couple[0]} -> {couple[1]}" for couple in zip(country, capitals)], sep='\n')