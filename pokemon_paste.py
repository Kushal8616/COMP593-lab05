import sys
from poke_api import get_pokemon_info
from pastebin_api import create_pastebin_paste

def get_pokemon_name():
    """
    Gets the Pokémon name from the command line parameter.

    Returns:
        str: The Pokémon name.
    """
    if len(sys.argv) < 2:
        print("Error: No Pokémon name provided.")
        sys.exit(1)
    
    return sys.argv[1]

def construct_paste_title_and_body(pokemon_info):
    """
    Constructs the title and body text for the new paste.

    Parameters:
        pokemon_info (dict): A dictionary of Pokémon information.

    Returns:
        tuple: The paste title and body text as strings.
    """
    name = pokemon_info['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    
    title = f"{name}’s Abilities"
    body_text = '\n'.join(f"- {ability}" for ability in abilities)
    
    return title, body_text

def main():
    """
    Main function that implements the sequence of function calls and logic.
    """
    pokemon_name = get_pokemon_name()
    pokemon_info = get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        title, body_text = construct_paste_title_and_body(pokemon_info)
        paste_url = create_pastebin_paste(title, body_text, expiration='1M', public=False)
        
        if paste_url:
            print("Paste URL:", paste_url)
        else:
            print("Error: Failed to create PasteBin paste.")
    else:
        print(f"Error: Pokémon '{pokemon_name}' not found.")

if __name__ == "__main__":
    main()
