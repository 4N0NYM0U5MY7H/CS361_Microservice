# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 8
# Description: This microservice gets the current exchange rate using the
#              Open Access EchangeRate-API endpoint.
#              https://www.exchangerate-api.com/docs/free

import requests
import time
import re
import exchange_rate


if __name__ == "__main__":

    request_file = exchange_rate.request_path()
    response_file = exchange_rate.response_path()

    print("Starting Microservice...")
    exchange_rate.create_file(request_file)
    exchange_rate.create_file(response_file)
    print(f"Listening for requests from {request_file} ...")

    try:
        while True:
            api_url = exchange_rate.api_url()
            time.sleep(1)

            # Check for a request to the microservice.
            try:
                with open(request_file, "r") as in_file:
                    try:
                        data = in_file.read()
                    except OSError as error:
                        print(f"Receive Request: {error}")
                        time.sleep(3)
                        print(f"Listening for requests from {request_file} ...")
                        continue
            except PermissionError as error:
                print(f"Receive Request: {error}")
                time.sleep(3)
                print(f"Listening for requests from {request_file} ...")
                continue
            except FileNotFoundError as error:
                print(f"Receive Request: {error}")
                exchange_rate.create_file(request_file)
                time.sleep(3)
                print(f"Listening for requests from {request_file} ...")
                continue

            # Validate request using Regular Express:
            # data must match the following pattern:
            #   3 alphabet characters (not case senstaive)
            #   a comma
            #   3 alphabet characters (not case senstaive)
            # ex: USD,EUR
            if re.search("^[a-zA-z]{3},[a-zA-z]{3}$", data):
                print("Request Received...\nProcessing...")

                try:
                    with open(request_file, "w") as in_file:
                        try:
                            in_file.write("Request Recieved")
                        except OSError as error:
                            print(f"Recieve Request: {error}")
                            time.sleep(3)
                            print(f"Listening for requests from {request_file} ...")
                            continue
                except PermissionError as error:
                    print(f"Receive Request: {error}")
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue
                except FileNotFoundError as error:
                    print(f"Receive Request: {error}")
                    exchange_rate.create_file(request_file)
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue

                # Split and standardize the request data.
                currencies_to_exchange = data.split(",")
                base_currency = currencies_to_exchange[0].upper()
                target_currency = currencies_to_exchange[1].upper()

                # Generate the API URL.
                if api_url == exchange_rate.api_url():
                    api_url += f"{base_currency}"

                # Get ExchangeRate-API data as a JSON object.
                try:
                    exchange_rate_data = requests.get(api_url).json()
                    if exchange_rate_data["result"] == "error":
                        raise requests.exceptions.RequestException
                    currencies = exchange_rate_data["rates"]
                except requests.ConnectionError as error:
                    print(f"ExchangeRate-API: {error}")
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue
                except requests.exceptions.HTTPError as error:
                    print(f"ExchangeRate-API: {error}")
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue
                except requests.exceptions.RequestException:
                    print(f'ExchangeRate-API: unsupported-code "{base_currency}"')
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue

                # Make sure the target currency is supported.
                if target_currency in currencies:
                    results = currencies[target_currency]
                else:
                    print(f'ExchangeRate-API: unsupported-code "{target_currency}"')
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue

                # Send the exhange rate as a response by saving to a file.
                try:
                    with open(response_file, "w") as out_file:
                        try:
                            time.sleep(1)
                            out_file.write(str(results))
                        except OSError as error:
                            print(f"Send Response: {error}")
                            time.sleep(3)
                            print(f"Listening for requests from {request_file} ...")
                            continue
                except PermissionError as error:
                    print(f"ExchangeRate-API: {error}")
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue
                except FileNotFoundError as error:
                    print(f"Send Response: {error}")
                    exchange_rate.create_file(response_file)
                    time.sleep(3)
                    print(f"Listening for requests from {request_file} ...")
                    continue

                print(f"Sending response to {response_file} ...")
                time.sleep(1)
                print(f"Listening for new requests from {request_file} ...")

            else:
                continue
    except KeyboardInterrupt:
        print("Terminating microservice...")