install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=brain_games

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml

setup: install build package-install