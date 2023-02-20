# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 8
# Description: This modules constains the functions for the currency exchange
#              rate microservice.


r"""This modules contains the functions for the currency exchange rate microservice."""

__version__ = "1.0.0"

# --------------------------------------------------------------------
# public interface


def request_path():
    """Returns the file path for the request file."""
    return "data/requests.txt"


def response_path():
    """Returns the file path for the reponse file."""
    return "data/response.txt"


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
