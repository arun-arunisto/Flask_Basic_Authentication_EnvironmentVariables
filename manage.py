from flask.cli import FlaskGroup
from src import create_app
from dotenv import load_dotenv


load_dotenv()
app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli.main(['run','--host', '0.0.0.0', '--port', '8080'])