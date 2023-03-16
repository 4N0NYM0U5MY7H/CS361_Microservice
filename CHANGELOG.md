# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [1.4.2] - 2023-03-15
### Changed
- Updated README Project Integration to include instructions for cloning the project direcly to a project root as per request.

## [1.4.1] - 2023-03-13
### Added
- CHANGELOG

### Changed 
- Rewrite project README.
- Update main.py docstring.
- Update exchange_rate to include customizable variables for the `request` and `response` files.
- Minor changes for accessing the `data` directory.

## [1.3.0] - 2023-02-24
### Added
- Pipfile
- Data directory for microservice requests/response files.

### Changed
- Microservice program title.
- The microservice now appends a new line to the request file instead of overwriting the file.

## [1.2.9] - 2023-02-15
### Added
- README troubleshooting section.

### Changed
- README to use more clear language.

## [1.2.4] - 2023-02-14
### Changed
- Minor updates to the README.

## [1.2.3] - 2023-02-12
### Added
- example.py

### Changed
- Project architecture to be more like a Python package.
- README to include a better sample client.

### Fixed
- README instructions to be more accurate.

## [1.0.1] - 2023-02-09
### Added
- license

## [1.0.0] - 2023-02-09
### Added
- response.txt
- .gitattributes
- pyproject.toml
- requests.txt
- Basic implementation of the requested microservice.

### Changed
- create_file now takes a filepath as a parameter.
- Included comments in the code as per partner's request.
- Encapsulated exchange rate functions into exchange_rate.py
- Updated project README.
- README to include an example client program.
- README to include description of how to send requests to the microservice.
- README to include description of how to receive a response from the microservice.
- README to include a sequence diagram.

### Removed
- The request state variable from main.py.

### Fixed
- The microservice now handles IOErrors when working with files.
- The microservice now exits the program on KeyboardInterrupt.

## [0.1.0] - 2023-02-06
### Added
- Project README.
- .gitignore

[1.4.2]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/releases/tag/v1.4.2
[1.4.1]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/releases/tag/v1.4.1
[1.3.0]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/pull/5
[1.2.9]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/commits/main?since=2023-02-15&until=20213-02-15
[1.2.4]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/commits/main?since=2023-02-14&until=20213-02-14
[1.2.3]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/commits/main?since=2023-02-12&until=20213-02-12
[1.0.1]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/pull/2
[1.0.0]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/pull/1
[0.1.0]: https://github.com/4N0NYM0U5MY7H/CS361_Partner_Microservice/commits/main?since=2023-02-06&until=20213-02-06
