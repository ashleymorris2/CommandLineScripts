import click
import moment
from datetime import datetime


# http://click.pocoo.org/5/quickstart/#quickstart

@click.command()
@click.option('--work_hours', '-w', default=False,
              help='Formats a unix millisecond time stamp to human readable.')
def between(work_hours):
    """Calculate the difference now and the weekend"""
    try:
        time1 = moment.now()
        time2 = moment.now().replace(weekday=5, hours=15, minutes=30, seconds=0)

        time1 = time1.epoch() * 1000
        time2 = time2.epoch() * 1000

        difference = time2 - time1

        dif_sec, dif_mins, dif_hours, diff_days = convert_millis(difference)

        click.echo("{0} days {1} hours {2} minutes {3} seconds".format(diff_days, dif_hours, dif_mins, dif_sec))
    except ValueError:
        click.echo("The value that was entered is not valid")


def convert_millis(millis):
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24
    hours = int(hours)
    days = (millis / (1000 * 60 * 60 * 24)) % 7
    days = int(days)

    return seconds, minutes, hours, days


# check if they are milliseconds or unix epoch
def get_length(millis):
    millis = str(millis)
    length = len(millis)

    while length != 13:
        millis += "0"
        length = len(millis)

    return float(millis)


def calc_work_hours(millis):

    return 0


if __name__ == '__main__':
    between()
