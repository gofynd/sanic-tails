# Sanic-Tails
A sidekick for your sanic app. 

This project (powered by Sanic) provides a boilerplate code to develop your lightening fast API complete with tests, documentation and monitoring.

## Setup Instructions
* Install python 3.6.5
* Install pip using either apt-get or brew
* Install virtualenv
* To install all the dependencies of the app run `pipenv install`. Note that you don't need to create a separate virtual environment for this project as `pipenv` handles all that.
* To run the server use `pipenv run python runserver.py`

## Running Scripts
You may want to run scripts/commands in the created virtual environment. There are two ways to do it:
* Use the prefix `pipenv run` before your command. eg. `pipenv run python`
* Activate shell using `pipenv shell`. Once activated all your commands will run in project's virtual environment. To deactivate this virtual environment run `exit`.

## TODO
- [x] Initial setup with Sanic
- [x] Configure sentry
- [ ] Update README.md
- [x] Configure db connection(Mongo)
- [x] Prometheus metrics setup
- [x] Select one testing library (eg. pytest, unittest) and configure
- [x] Setup TravisCI for this repo
- [x] Expolore tools to facilitate api development
    - [x] Swagger integration (or something functionally equivalent)
- [x] Add tool to calculate the Coverage
- [ ] Add development instructions in contribute.md file
- [ ] Load testing tool/framework
- [ ] Write deployment script
