install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
