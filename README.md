# fastapi_basic

lab from [StackPython web](https://stackpython.co/tutorial/api-python-fastapi)

## after git clone
1. open vscode at fastapi_basic folder
2. create virtual environment `python -m venv venv`
3. start virtual environment `venv\Scripts\activate`
4. (optional) `python.exe -m pip install --upgrade pip`
5. restore all needed dependency lib `pip install -r requirements.txt`

## API Documents bundled with FastAPI
FastAPI will create 2 types of the API documents:
1. Interactive API Docs .. SwaggerUI able to test APIs ... url --> `http://127.0.0.1:8000/docs`
2. Alternative API docs .. ReDoc unable to test API, just view information ... url --> `http://127.0.0.1:8000/redoc`

## start to coding from zero
1. create a blank project folder
2. enter into the project folder
3. create an virtual environment `python -m venv venv`
4. start virtual environment `venv\scripts\activate`
5. vscode .. don't forget to change working directory to venv, to avoid error about unrecognize library import
6. pip freeze > requirements.txt
