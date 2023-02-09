# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 8
# Description: This microservice gets the current exchange rate using the
#              Open Access EchangeRate-API endpoint.
#              https://www.exchangerate-api.com/docs/free

import requests
import time
import re


if __name__ == "__main__":

    filename = "requests.txt"
    api_url = "https://open.er-api.com/v6/latest/"

    print("Starting Microservice...")
    print(f"Listening for changes to {filename} ...")

    while True:

        time.sleep(1)

        # Check for a request to process.
        try:
            with open(filename, "r") as in_file:
                try:
                    time.sleep(1)
                    data = in_file.read()
                except OSError as error:
                    print(f"{filename}: {error}")
        except (FileExistsError, FileNotFoundError, PermissionError, OSError) as error:
            print(f"{filename}: {error}")

        # Validate request using Regular Express:
        # data must match the following pattern:
        #   3 alphabet characters (not case senstaive)
        #   a comma
        #   3 alphabet characters (not case senstaive)
        # ex: USD,EUR
        if re.search("^[a-zA-z]{3},[a-zA-z]{3}$", data):
            time.sleep(1)
            print("Request Received...\nProcessing...")

            # Split and standardize the request data.
            currencies_to_exchange = data.split(",")
            base_currency = currencies_to_exchange[0].upper()
            target_currency = currencies_to_exchange[1].upper()

            # Generate the API URL.
            if api_url == "https://open.er-api.com/v6/latest/":
                api_url += f"{base_currency}"

            # Get ExchangeRate-API data as a JSON object.
            exchange_rate_data = requests.get(api_url).json()
            currencies = exchange_rate_data["rates"]

            # Make sure the target currency is supported.
            if target_currency in currencies:
                results = currencies[target_currency]
            else:
                print(
                    f"target_currency: {target_currency} is not a supported currency..."
                )
                continue

            # Send the exhange rate as a response by saving to a file.
            try:
                with open(filename, "w") as out_file:
                    try:
                        time.sleep(1)
                        out_file.write(str(results))
                    except OSError as error:
                        print(f"{filename}: {error}")
            except (
                FileExistsError,
                FileNotFoundError,
                PermissionError,
                OSError,
            ) as error:
                print(f"{filename}: {error}")

            print(f"Listening for new changes to {filename} ...")

        else:
            continue
