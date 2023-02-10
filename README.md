<div align="center">

![](.github/osuEcampus.png)
# CS361: Currency Exchange Rate Microservice
### An accurate and Reliable Exchange Rate Service 

</div>
<br>

## Installation
To clone and run these files, you must have [Python 3.9+](https://www.python.org/downloads/release/python-390/) with IDLE or an alternative text editor, such as Atom or Visual Studio Code, installed on your local machine.

### Dependencies
This microservices requires the [requests 2.28+ python library](https://pypi.org/project/requests/).

### From the Termial
```bash
# Move to the desired install directory
$ cd Documents/GitHub

# Clone this repository
$ git clone https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice

# Go into the directory
$ cd CS361_Partner_Microservice

# Install dependencies
$ python -m pip install requests

# Run the microservice
$ python microservice_main.py
```

### More Options:
For more cloning options, please visit the [GitHub Docs page for cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Using the Microservice
### Sending a Request
Send a "`request`" to this microservice by updating `requests.txt` with two ISO 4217 Three Letter Currency Codes - e.g. `USD` for US Dollars, `EUR` for Euro etc. - separated by a comma.

> Here's the list of [supported currency codes](https://www.exchangerate-api.com/docs/supported-currencies).

### Receving a Response
After a valid "`request`", the microservice will send a reponse to `response.txt` containing the exchange rate - e.g. request: `USD,EUR` response: `0.932527`.

### Animated Demo
<img src=".github/request-response.gif" height="350px">

### Sample Client in Python
```Python
# Simple example client to run with the Currency Exchange Microservice
import time
import re

# <path_to_requests_file> points to the request file in the microservice directory
path_to_requests_file = "requests.txt"

# <path_to_response_file> points to the request file in the microservice directory
path_to_response_file = "response.txt"

# variable to ensure the new reponse isn't the old response
previous_response = ""

# Send the request to the <path_to_request_file>
with open(path_to_requests_file, "w") as out_file:
    out_file.write("usd,eur")

# Poll the <path_to_response_file> until you receive a response
while True:
    time.sleep(1)
    # Receive the response from the <path_to_response_file>
    with open(path_to_response_file, "r") as in_file:
        exchange_rate = in_file.readline()

    # No response received
    if exchange_rate == "":
        continue
    # You already have this reponse data
    if exchange_rate == previous_response:
        continue
    # Valid reponse received
    if re.search("^(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", exchange_rate):
        previous_reponse = exchange_rate
        break

# View the results
print(f"The exchange rate from USD to EUR is {exchange_rate}.")
```
```bash
# Expected Output
>>> The exchange rate from USD to EUR is 0.932527.
```

## Sequence Diagram
<img src=".github/sequence-diagram.png" width="700px">

## Acknowledgements
This microservice would not be possible without the [Free and Open Access ExchangeRate-API](https://www.exchangerate-api.com/docs/free) endpoint.

## License
[MIT License](license)