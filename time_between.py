import click
import moment
from datetime import datetime


# http://click.pocoo.org/5/quickstart/#quickstart

@click.command()
@click.argument('time1')
@click.argument('time2')
# @click.option('--time', prompt='The timestamp to format',
# help='Formats a unix millisecond time stamp to human readable.')
def between(time1, time2):
    """Calculate the difference between two unix timestamps"""
    try:

        time1 = get_length(time1)
        time2 = get_length(time2)

        difference = time1 - time2

        dif_sec, dif_mins, dif_hours = convert_millis(difference)

        click.echo("{0}hours {1}minutes {2}seconds".format(dif_hours, dif_mins, dif_sec))
    except ValueError:
        click.echo("The value that was entered is not valid")


def convert_millis(millis):
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    hours = int(hours)

    return seconds, minutes, hours


def get_length(millis):

    millis = str(millis)
    length = len(millis)

    while length != 13:
        millis += "0"
        length = len(millis)

    return float(millis)


if __name__ == '__main__':
    between()
