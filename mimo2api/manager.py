def load_all_users():
    try:
        response = requests.get('https://api.example.com/users')
        response.raise_for_status()  # Raise an error for bad responses
        try:
            return response.json()
        except json.JSONDecodeError as e:
            logging.error(f'JSONDecodeError: {e} - Response content: {response.text}')
            return []  # Return empty list or handle it the way you prefer
    except requests.exceptions.RequestException as e:
        logging.error(f'RequestException: {e}')
        return []  # Return empty list or handle it accordingly


# Example usage of JSON handling in other r.json() calls
try:
    data = r.json()  # Ensure that r is a response object
except json.JSONDecodeError as e:
    logging.error(f'JSONDecodeError: {e} - Response content: {r.text}')
    data = {}  # Handle accordingly
