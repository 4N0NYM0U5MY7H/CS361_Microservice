# Simple example client to run with the Currency Exchange Microservice
import time
import re

# <path_to_requests_file> points to the request file in the data directory
# NOTE: This example assumes the client is at the project root
path_to_requests_file = "data/requests.txt"

# NOTE: This example assumes the client is at the project root
# <path_to_response_file> points to the request file in the data directory
path_to_response_file = "data/response.txt"

# example currencies to exchange
base_currency = "usd"
target_currency = "eur"

# Send the request to the <path_to_request_file>
with open(path_to_requests_file, "w") as out_file:
    out_file.write(f"{base_currency},{target_currency}")

# Poll the <path_to_response_file> until you receive a response
while True:
    time.sleep(1)
    # Receive the response from the <path_to_response_file>
    with open(path_to_response_file, "r") as in_file:
        exchange_rate = in_file.readline()

    # No response received
    if exchange_rate == "":
        continue

    # Valid reponse received
    if re.search("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", exchange_rate):
        # acknowledge valid response in <path_to_response_file>
        with open(path_to_response_file, "a") as out_file:
            out_file.write("\nResponse Received")
        break

# View the results
print(f"The exchange rate from USD to EUR is {exchange_rate}.")