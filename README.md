## Playwright UI testing demo

Prerequisites:
- Python 3.12
- Google Chrome

### Steps to run the test:

* Create a Python virtual environment:

```
python -m venv venv
source venv/bin/activate 
```

* Install requirements with pip:

```
python -m pip install -r requirements.txt
```

* Install playwright:

```
playwright install
```

* Run the test:

``` 
pytest -m "basic_search"
```