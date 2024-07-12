import requests

def get_pokemon_info(pokemon_name):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Parameters:
        pokemon_name (str): The name or PokéDex number of the Pokémon.

    Returns:
        dict: A dictionary of Pokémon information if successful, None otherwise.
    """
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}'
    
    print(f"Getting information for {pokemon_name}...")
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Successfully fetched Pokémon information.")
        return response.json()
    else:
        print("Failed to fetch Pokémon information.")
        print("Response code:", response.status_code)
        return None

