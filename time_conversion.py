class TimeConversion:

    @staticmethod
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

