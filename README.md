<div align="center">

![](.github/osuEcampus.png)
# CS361: Currency Exchange Rate Microservice
### An accurate and Reliable Exchange Rate Service 

</div>
<br>

## Sending a Request
Send a "`request`" to this microservice by updating `requests.txt`.

```Python
# Example Client code using Python

# <path_to_requests_file> points to the request file in the microservice directory
path_to_requests_file = "requests.txt"

# Send the request to the <path_to_request_file>
with open(path_to_requests_file, "w") as out_file:
    out_file.write("usd,eur")
```

## Receving a Response
If the "`request`" was valid, this microservice will send a response to the `requests.txt`.

```Python
# Example Client code using Python

# <path_to_response_file> points to the request file in the microservice directory
path_to_response_file = "response.txt"

# Recieve the response from the <path_to_response_file>
with open(path_to_response_file, "r") as in_file:
    exchange_rate = in_file.readline()

# View the results
print(f"The exchange rate from USD to EUR is {exchange_rate}.")
```
```bash
# Expected Output
>>> The exchange rate from USD to EUR is 0.932527.
```

## Animated Demo
<img src=".github/request-response.gif" height="350px">

## Installation
To clone and run these files, you must have [Python 3.9+](https://www.python.org/downloads/release/python-390/) with IDLE or an alternative text editor, such as Atom or Visual Studio Code, installed on your local machine.

### From the Termial
```bash
# Clone this repository
$ git clone https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice

# Go into the directory
$ cd CS361_Partner_Microservice
```

### More Options:
For more cloning options, please visit the [GitHub Docs page for cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Dependencies
This microservices requires the [requests 2.28+ python library](https://pypi.org/project/requests/).
```bash
# Install requests
$ python -m pip install requests
```

## Acknowledgements
This microservice would not be possible without the [Free and Open Access ExchangeRate-API](https://www.exchangerate-api.com/docs/free) endpoint.

## License
