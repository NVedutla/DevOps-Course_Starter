# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).


TRELLO provides a REST API, that can be used to create, read and update to-do items. 
1. In order to make calls to TRELLO REST API, Developer API Keys need to be obtained and token generated. Details can be found on https://trello.com/app-key . 
2. In this application, in order to execute the list, add and complete items, TRELLO_KEY and TRELLO_TOKEN need to be provided
3. Use postman, https://web.postman.co/home, to find out the board id, to_do id, doing_id and done _id in order to obtain the values for constants - TRELLO_BOARD_ID, TRELLO_LIST_TODO_ID, TRELLO_LIST_DOING_ID and TRELLO_LIST_DONE_ID=
4. Add PyTest as a dependancy of our project
5. In order to run the test cases, need to install Selenium Python package
6. We need to install Firefox as its the easier browser to test usign Selenium
7. We need to download Gecko Driver executable and place it in the root of the project

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

