- Create virtual environment for an specific python version

`virtualenv venv --python=python3.9.6`

- Activate our virtual environment

`source venv/bin/activate`

- To deactivate our virtual environment

`deactivate`

- Install flask

`pip install flask`

- Show dependencies

`pip freeze`

- Command to install requirements
`pip install -r requirements.txt`

- Running the flask 🌶️ server

*Firstly we need to add a environment
`FLASK_APP` with the directory where it is our py instance

`export FLASK_APP=main.py`

*Next,  we need to run the follow command
`flask run`

- Activate debug mode

`export FLASK_DEBUG=1`