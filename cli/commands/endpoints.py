from typing import Optional

import requests
import typer


def add_endpoint(
    name: str = typer.Option(..., "--name", "-n", help="The name of the API endpoint"),
    url: str = typer.Option(..., "--url", "-u", help="The URL of the API endpoint"),
    method: str = typer.Option(
        ..., "--method", "-m", help="The HTTP method for the API endpoint"
    ),
    # headers: Optional[str] = typer.Option(None, "--headers", "-h", help="The headers for the API endpoint"),
    check_interval: str = typer.Option(
        "5m", "--check-interval", "-c", help="The check interval for the API endpoint"
    ),
):
    """Add a new API endpoint to monitor."""
    typer.echo(f"Adding endpoint: {name}")
    # headers_dict = dict(h.split(":") for h in headers.split(","))

    data = {
        "name": name,
        "url": url,
        "method": method,
        # "headers": headers_dict,
        "check_interval": check_interval,
    }

    response = requests.post("http://localhost:8000/api/endpoints/", json=data)
    print("response:", response)
    if response.status_code == 201:
        typer.echo("Endpoint added successfully.")
    else:
        typer.echo(f"Failed to add endpoint. Status code: {response.status_code}")
        typer.echo(f"Response content: {response.content}")


app = typer.Typer()
app.command()(add_endpoint)
