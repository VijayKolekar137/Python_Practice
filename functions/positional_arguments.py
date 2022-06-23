# Positional Arguments

def describe_pet(ani_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {ani_type}.")
    print(f"My {ani_type}'s name is {pet_name.title()}")


describe_pet('hamster','harry')

describe_pet('dog','willie')