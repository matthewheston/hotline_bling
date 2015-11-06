import calendar
import collections
import constants
from os import path
import sqlite3 as sql

def get_dates_for_days():
    dates = []
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    yearcal = flatten(c.yeardatescalendar(constants.year))
    for day in yearcal:
        if day.weekday() in constants.days:
            dates.append(day)
    return dates


def flatten(iterable):
    iterator = iter(iterable)
    array, stack = collections.deque(), collections.deque()
    while True:
        try:
            value = next(iterator)
        except StopIteration:
            if not stack:
                return tuple(array)
            iterator = stack.pop()
        else:
            if not isinstance(value, str) \
               and isinstance(value, collections.Iterable):
                stack.append(iterator)
                iterator = iter(value)
            else:
                array.append(value)

def get_contacts(dates):
    db = sql.connect(path.expanduser(constants.imessage_path))
    cursor = db.cursor()
    query = """SELECT chat.chat_identifier, count(*) as cnt
            FROM chat
            JOIN chat_message_join
            ON chat.ROWID = chat_message_join.chat_id
            LEFT JOIN message
            ON message.ROWID = chat_message_join.message_id
            WHERE  strftime("%%Y-%%m-%%d", datetime(message.date + 978307200, 'unixepoch', 'localtime')) IN (%s)
            AND strftime("%%H:%%M:%%S", datetime(message.date + 978307200, 'unixepoch', 'localtime')) > '00:00:00'
            AND strftime("%%H:%%M:%%S", datetime(message.date + 978307200, 'unixepoch', 'localtime')) < '04:00:00'
            AND message.is_from_me = 1
            GROUP BY chat.chat_identifier;""" % ",".join(dates)
    results = cursor.execute(query).fetchall()
    ordered_results = sorted(results, key=lambda t: t[1], reverse=True)
    return ordered_results

def main():
    dates = get_dates_for_days()
    formatted_dates = [date.strftime("'%Y-%m-%d'") for date in dates]
    results = get_contacts(formatted_dates)
    for result in results:
        print "%s: %s" % result

if __name__ == "__main__":
    main()
