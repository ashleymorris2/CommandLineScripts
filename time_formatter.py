import click
import moment
from datetime import datetime

@click.command()
@click.argument('time')
#@click.option('--time', prompt='The timestamp to format', help='Formats a unix millisecond time stamp to human readable.')
def format_time(time):
    """Formats a timestamp to user readable string"""
    time = float(time)
    formatted_time = moment.unix(time)
    click.echo(formatted_time)

if __name__ == '__main__':
    format_time()
