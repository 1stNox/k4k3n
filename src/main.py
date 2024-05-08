import typer
from commands import create_project


app = typer.Typer()


@app.command()
def create(name: str):
    create_project(name)


@app.command()
def hello_world():
    print('Hello World!')


if __name__ == "__main__":
    app()
