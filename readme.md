API Interface for the Have I Been Pwned site

Runs a simple web service to integrate with the HaveIBeenPwned sqlite3

To run:

pip install -r requirements
python api.py


URLs are:

GET /user/<email address> - Returns breach data for that email.

Get /breach/<name> - Returns info on that breach.

