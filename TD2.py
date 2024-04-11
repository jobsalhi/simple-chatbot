
import re

# Function to calculate the sum of two numbers
def calculate_sum(match):
    return f"Le résultat est {int(match.group(1)) + int(match.group(2))}"


reglesV2 = [
    ["bonjour1", "salut", "Salut à toi !", 1, None],
    ["bonjour2", "salut", "Salut!", 2, None],
    ["bonjour2", "bonjour", "Salut humain", 1, None],
    ["presentation1", "mon nom est .*", "Enchanté :)", 2, None],
    ["presentation2", "je m'appelle .*", "Enchanté :)", 2, None],
    ["presentation3", "je suis .*", "Enchanté :)", 2, None],
    ["bye", "by.*", "Au revoir :/", 1, None],
    ["au revoir", "au revoir", "Au revoir :/", 1, None],
    ["jo", "jeux olympiques", "Les prochains JO auront lieu à Paris en 2024.", 3, None],
    ["capacite", "capable de faire .*", "Je peux parler des futurs JO et calculer des sommes.", 2, None],
    ["calcul", r"calculer (\d+) et (\d+)", None, 4, calculate_sum],
    ["age", "quel est ton âge", "Je suis un programme informatique, je n'ai pas d'âge !", 2, None],
    ["humeur", "comment vas-tu", "Je suis un programme informatique, je n'ai pas de sensations !", 2, None],
    ["inconnu", ".*", "Je ne sais pas.", 0, None]
]



c = ""
while (c != "bye"):
    c = input("> ") # le prompt
    max_priority = -1
    selected_rule = None
    
    # Iterate through rules to find the highest priority rule that matches the input
    for r in reglesV2:
        pattern = re.compile(r[1])
        res = pattern.finditer(c)
        pos = [m.span() for m in res]
        if len(pos) > 0 and r[3] > max_priority:
            max_priority = r[3]
            selected_rule = r
            
    if selected_rule:
        if selected_rule[4]:
            # If a function is specified, execute the function
            print(selected_rule[4](re.search(selected_rule[1], c)))
        else:
            # If no function is specified, print the response
            print(selected_rule[2])
    else:
        # If no rule matches, print the default response
        print("Je ne sais pas.")

