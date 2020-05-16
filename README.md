# PA1450
### Skeleton application
***

## Quick Start

You're currently viewing the branch `skeleton`. This branch contains a skeleton example project with the basics to get you started.

To use the application, you will first need to make sure that your environment supports it. Please see the `virtual-lab-environment` branch for a complete and tested environment for use with this project.

When you're ready to download and start the application, follow these steps:

```shell
# Clone the repository
git clone https://github.com/AlexGustafsson/PA1450
# Enter the repository and checkout this branch
cd PA1450
git checkout skeleton

# Install dependencies
make install

# Start the application by using the wrapper script
./application.sh
```

To run a greeting command use:

```shell
./application.sh greet --user "Joe Doe"
```

To serve the same functionality as a web-based API, use:

```shell
./application.sh serve
```

The server will now be available on `http://localhost:8080`.

## Contributing

### Quick Start

First start by downloading the repository:

```shell
# Clone the repository
git clone https://github.com/AlexGustafsson/PA1450
```

You can now enter the directory and install the dependencies:

```shell
# Enter the repository and checkout this branch
cd PA1450
git checkout skeleton

# Install dependencies
make install
```

You're now ready to develop the application.

### Project structure

The main entrypoint of the application is the `application/main.py` file. It contains the command line argument parser which is in charge of interfacing with the user in order to start the application.

Each available command is located within the `application/commands` directory. Each command file defines a `create_parser` method which sets up the command's command line argument parser.

Lastly, the `www` directory contains the static web files used for the demonstrational website.

### Yes :)

![Smile](./smile.jpg)
