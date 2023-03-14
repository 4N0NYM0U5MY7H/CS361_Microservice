r"""rate_X microservice functions.

The exchange_rate module contains all the functions required run the
rate_X microservice.

Rates by Exchange Rate API: <https://www.exchangerate-api.com>"""

__version__ = "1.1.1"
__author__ = "August Frisk <https://github.com/users/4N0NYM0U5MY7H>"

# --------------------------------------------------------------------
# internal variables

# Make changes to requests/response file directory here
_data_directory = "../data"

# Make changes requests/response file names here
_request_file = "requests.txt"
_response_file = "response.txt"

# CHANGE WITH CARE
_path_to_request = f"{_data_directory}/{_request_file}"
_path_to_response = f"{_data_directory}/{_response_file}"

# --------------------------------------------------------------------
# public interface


def request_path():
    """Returns the file path for the request file."""
    return _path_to_request


def response_path():
    """Returns the file path for the reponse file."""
    return _path_to_response


def api_url():
    """Returns the Open Acess ExchangeRate-API URL endpoint."""
    return "https://open.er-api.com/v6/latest/"


def create_file(filepath):
    """Creates the request file if it does not exist."""
    try:
        with open(filepath, "r") as in_file:
            try:
                in_file.readline()
            except OSError as error:
                print(f"Create File: {error}")
    except PermissionError as error:
        print(f"Create File: {error}")
        return
    except FileNotFoundError:
        try:
            with open(filepath, "w") as in_file:
                try:
                    print(f'Creating new file "{filepath}" ...')
                    return
                except OSError as error:
                    print(f"Create File: {error}")
        except (FileExistsError, PermissionError) as error:
            print(f"Create File: {error}")
