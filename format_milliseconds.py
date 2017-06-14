import click
import moment
from datetime import datetime


# http://click.pocoo.org/5/quickstart/#quickstart

@click.command()
@click.argument('time', default=moment.now().epoch())
# @click.option('--time', prompt='The timestamp to format',
# help='Formats a unix millisecond time stamp to human readable.')
def format_millis(time):
    """Formats a unix milliseconds timestamp to user readable string"""
    try:
        time = float(time)
        formatted_time = moment.unix(time)
        click.echo(formatted_time)
    except ValueError:
        click.echo("The value that was entered is not valid")


if __name__ == '__main__':
    format_millis()
