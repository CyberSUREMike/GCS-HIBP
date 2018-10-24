<<<<<<< HEAD
import os
from waitress import serve
from index import app

=======
import os
from waitress import serve
from index import app

>>>>>>> 3ea0d4bb6491210789cbe40ff787881803a3df65
serve(app,host="0.0.0.0",port=os.environ["PORT"])