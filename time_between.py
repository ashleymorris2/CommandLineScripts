import click

from time_conversion import TimeConversion


# http://click.pocoo.org/5/quickstart/#quickstart

@click.command()
@click.argument('start')
@click.argument('end')
# @click.option('--time', prompt='The timestamp to format',
# help='Formats a unix millisecond time stamp to human readable.')
def between(start, end):
    """Calculate the difference between two unix timestamps"""
    try:

        start = get_length(start)
        end = get_length(end)

        if start < end:
            difference = end - start
        else:
            difference = start - end

        dif_sec, dif_mins, dif_hours = TimeConversion.convert_millis(difference)
        click.echo("{0} hours {1} minutes {2} seconds".format(dif_hours, dif_mins, dif_sec))
    except ValueError:
        click.echo("The value that was entered is not valid")


# check if they are milliseconds or unix epoch
def get_length(millis):
    millis = str(millis)
    length = len(millis)

    while length != 13:
        millis += "0"
        length = len(millis)

    return float(millis)


if __name__ == '__main__':
    between()
