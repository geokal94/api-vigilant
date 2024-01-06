import typer
from commands import endpoints

app = typer.Typer()
app.add_typer(endpoints.app, name="endpoints")

if __name__ == "__main__":
    app()