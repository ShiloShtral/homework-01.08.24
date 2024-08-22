games = ["Grand thief auto:v", "Fortnite", "Overwatch","Dark Souls", "The Elder Scrolls V:Skyrim"]

print(list(filter(lambda x: len(x) > 8, games)))

print(list(filter(lambda x: x.startswith('F'), games)))

print(list(filter(lambda x: len(x.split()) == 2, games)))

print(list(filter(lambda x: "v" in x, games)))



