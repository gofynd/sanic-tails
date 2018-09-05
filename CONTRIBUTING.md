# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue (preferred)
or any other method with the owners of this repository before making a change.

## Adding an API

- Describe the model and the schema your API would be using in `/v1/models` directiory
- Add route (blueprints) in `/routes` directory
- Add logic/code to in the `/views` directory
- Add documentation in yaml format in your view class. Note that to extract documentation correctly you *must* inherit your view class from `BaseViewClass`.
- Add tests

## Generating swagger documentation

- Add tag, schema defination and the path corresponding to your API's view in the `generate_api_spec.py` file
- Run `pipenv run python generate_api_spec.py` to generate swagger doc in `swagger.json` file
- You can now use this swagger.json file to generate postman collections etc.

## Viewing the API docs

- The file `api_gui.html` will render the documentation described by above generated swagger doc

## PreCommit Checks

The current repo enforces that your commited code adheres to some existing code standards (PEP-8).
To add/edit these hooks you'll have to update `.pre-commit-config.yaml` file.
In case you don't see these hooks running when you commit a change, contact the repo maintainer.
