import click
import moment

from time_conversion import TimeConversion


# http://click.pocoo.org/5/quickstart/#quickstart

@click.command()
@click.option('--work_hours', '-w', is_flag=True,
              help='Specifies whether to calculate working hours remaining only.')
def between(work_hours):
    """Calculate the difference now and the weekend"""
    try:
        time1 = moment.now()
        time2 = moment.now().replace(weekday=5, hours=15, minutes=30, seconds=0)

        time1 = time1.epoch() * 1000
        time2 = time2.epoch() * 1000

        difference = time2 - time1

        if work_hours:
            day = 7.5 * 3600000

            day_end = moment.now().replace(hours=15, minutes=30, seconds=0).epoch() * 1000

            # difference today
            difference = day_end - time1
            weekday = moment.now().weekday + 1

            while weekday < 6:
                difference += day
                weekday += 1

        dif_sec, dif_mins, dif_hours, diff_days = TimeConversion.convert_millis(difference)

        click.echo("{0} days {1} hours {2} minutes {3} seconds".format(diff_days, dif_hours, dif_mins, dif_sec))

    except ValueError:
        click.echo("The value that was entered is not valid")

if __name__ == '__main__':
    between()
