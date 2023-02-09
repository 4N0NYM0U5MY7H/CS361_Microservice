# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 8
# Description: This modules constains the functions for the currency exchange
#              rate microservice.


r"""This modules contains the functions for the currency exchange rate microservice."""

__version__ = "1.0.0"

# --------------------------------------------------------------------
# public interface


def get_filepath():
    """Returns the file path for the desired request and response file."""
    return "requests.txt"


def get_api_url():
    """Returns the Open Acess ExchangeRate-API URL endpoint."""
    return "https://open.er-api.com/v6/latest/"


def create_file():
    """Creates the desired request and response file if it does not exist."""
    try:
        with open(get_filepath(), "r") as in_file:
            try:
                in_file.readline()
            except OSError as error:
                print(f"Create File: {error}")
    except PermissionError as error:
        print(f"Create File: {error}")
        return
    except FileNotFoundError:
        try:
            with open(get_filepath(), "w") as in_file:
                try:
                    return
                except OSError as error:
                    print(f"Create File: {error}")
        except (FileExistsError, PermissionError) as error:
            print(f"Create File: {error}")