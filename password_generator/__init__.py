import click
from .generation import generate_password

@click.command()
@click.option('--length', default=8, help="Determine the length of the password | DEFAULT=8")
@click.option('--upper', default=True, help="Enable/Disable uppercase chars (ABC) | DEFAULT=True")
@click.option('--lower', default=True, help="Enable/Disable lowercase chars (abc) | DEFAULT=True")
@click.option('--numeric', default=True, help="Enable/Disable numeric chars (123) | Default=True")
@click.option('--punct', default=True, help="Enable/Disable punctuation chars (@!?) | Default=True")

def main(length, upper, lower, numeric, punct):
    """Generate a Strong Password"""
    
    password = generate_password(length, numeric, lower, upper, punct)
    return password

if __name__ == "__main__":
    main()
