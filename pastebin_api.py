import requests

def create_pastebin_paste(title, body_text, expiration='1M', public=False):
    """
    Creates a new PasteBin paste.

    Parameters:
        title (str): The title of the paste.
        body_text (str): The body text of the paste.
        expiration (str): The expiration period of the paste (default is 1M for 1 month).
        public (bool): Whether the paste is publicly listed (default is False).

    Returns:
        str: URL of the newly created paste if successful, None otherwise.
    """
    api_url = 'https://pastebin.com/doc_api'
    api_dev_key = 'bencHhw8kke9o-NMzYxquDkqNeVCUgqP'  
    paste_params = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if public else 1
    }

    print("Creating a new PasteBin paste...")
    response = requests.post(api_url, data=paste_params)

    if response.status_code == 200:
        print("Paste created successfully.")
        return response.text
    else:
        print("Failed to create paste.")
        print("Response code:", response.status_code)
        return None
