import os
from waitress import serve
from application import api

serve(app,host="0.0.0.0",port=os.environ["PORT"])
