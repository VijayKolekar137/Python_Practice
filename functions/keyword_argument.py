# Keyword Arguments in function

def des_pet(ani_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {ani_type}.")
    print(f"My {ani_type}'s name is {pet_name.title()}")



des_pet(ani_type = "Dog", pet_name = "Jonny")