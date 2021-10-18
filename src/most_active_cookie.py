import csv
import argparse
import datetime
from collections import Counter
import logging

logging.basicConfig(filename='test/cookie.log')


def find_cookie_count(filename, date):
    cookies = Counter()

    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                cookie = line['cookie']
                timestamp = datetime.datetime.fromisoformat(line['timestamp'])

                if timestamp.date() == date:
                    cookies[cookie] += 1
    except FileNotFoundError as e:
        logging.exception('error while accessing the file')
        raise e
    except KeyError as e:
        logging.exception('error in the header of the log file')
        raise e
    except ValueError as e:
        logging.exception('error while reading cookie and time')
        raise e

    return cookies.most_common()


def most_active_cookie(cookie_count):
    most_active_cookies = []
    try:
        max_count = cookie_count[0][1]
        for cookie, count in cookie_count:
            if count != max_count:
                break

            most_active_cookies.append(cookie)
    except IndexError:
        logging.exception('error no cookie found on given date')

    return most_active_cookies


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find most active cookie')
    parser.add_argument('-l', '--logfile', type=str, help='Cookie Log File')
    parser.add_argument(
        '-d', '--date', type=datetime.date.fromisoformat, required=True, help='Date')
    args = parser.parse_args()

    cookie_count = find_cookie_count(args.logfile, args.date)
    result = most_active_cookie(cookie_count)
    print(f'Most Active Cookies on date {str(args.date)}:')
    print('\n'.join(map(str, result)))
