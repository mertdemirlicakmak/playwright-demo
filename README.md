## Playwright UI testing demo

Prerequisites: 
- Python 3.12
- Google Chrome

Steps to run the test:
1. Create a Python virtual environment:
`python -m venv venv`
`source venv/bin/activate`
2. Install requirements with pip
`pip install -r requirements.txt`
3. Install playwright
`playwright install`
4. Run the test:
`pytest -m "basic_search"`