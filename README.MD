# Portfoio Web Page

## Prerequisits
- [Python 3](https://www.python.org/downloads/)
- pipenv package
    ```bash
    pip3 install pipenv
    ```


## Install
1. Open **pipenv** shell
    ```bash
    pipenv shell
    ```
2. Install Dependencies
    ```bash
    pipenv install
    ```
3. Run the project from the root folder, having **pipenv** activated
    
    ```bash
    export FLASK_APP=server.py
    ```
    For hot reload, it required to enable development mode
    ```bash
    export FLASK_ENV=development
    ```

    ```bash
    flask run
    ```