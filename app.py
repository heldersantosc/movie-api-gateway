from flask import Flask
from controllers import register_routes
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv("PORT")

app = Flask(__name__)
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
