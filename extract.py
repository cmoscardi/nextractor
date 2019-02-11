from datetime import datetime














def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d:%H")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def main():
    parser = argparse.ArgumentParser(description='Extract bird counts within a specified window of space and time')
    parser.add_argument('start_time', metavar='start_time', type=str, nargs=1,
                        help='Start time (date + hour). Format | mm/dd/YYYY:HH')
 
    parser.add_argument('end_time', metavar='end_time', type=str, nargs=1,
                        help='End time (date + hour). Format | mm/dd/YYYY:HH')
    args = parser.parse_args()

if __name__ == "__main__":
    import argparse
    main()
