from typing import List, Tuple

from datetime import datetime, time, timedelta


def get_free_time_list(
        busy_terms: List[Tuple[datetime, datetime]],
        date_range: Tuple[datetime, datetime],
        opening_time: time,
        closing_time: time,) -> List[Tuple[datetime, datetime]]:

    """

    function returns list of free time periods

    Args:
        busy_terms: [(start: datetime, stop: datetime)]
        date_range: (start: datetime, stop: datetime)
        opening_time: time
        closing_time: time

    Returns:
        List[Tuple[start: datetime, stop: datetime]]
    """

    def next_day(actual_date, start_time) -> datetime:
        new_date = actual_date + timedelta(days=1)
        return new_date.replace(hour=start_time.hour, minute=start_time.minute)

    result = []

    # set date range variables
    free_time_start = date_range[0]
    free_time_end = date_range[1]

    while busy_terms:

        # get first available term
        term_start, term_end = busy_terms.pop(0)
        print('terms: ', term_start, term_end)

        if term_start.day != free_time_start.day:
            result.append((free_time_start, datetime(year=free_time_start.year,
                                                     month=free_time_start.month,
                                                     day=free_time_start.day,
                                                     hour=closing_time.hour, minute=closing_time.minute)))

            free_time_start = datetime(year=term_start.year, month=term_start.month, day=term_start.day,
                                       hour=opening_time.hour, minute=opening_time.minute)

            print(f' free_time_start from if: {free_time_start}')

        if term_start.day == free_time_start.day:
            print('jestem w else')

            if free_time_start < term_start:
                result.append((free_time_start, term_start))
                free_time_start = term_end

                if free_time_start == datetime(year=free_time_start.year,
                                               month=free_time_start.month,
                                               day=free_time_start.day,
                                               hour=closing_time.hour, minute=closing_time.minute):

                    free_time_start = next_day(free_time_start, opening_time)

        print(result)

    if free_time_start < free_time_end:
        result.append((free_time_start, free_time_end))

    return result


if __name__ == '__main__':
    specific_date = datetime.now()

    open_from = time(7, 0)
    open_to = time(18, 0)

    busy_terms = [
        (datetime(year=2021, month=3, day=5, hour=10, minute=0),
         datetime(year=2021, month=3, day=5, hour=10, minute=30)),
        (datetime(year=2021, month=3, day=6, hour=8, minute=0),
         datetime(year=2021, month=3, day=6, hour=9, minute=30)),
        (datetime(year=2021, month=3, day=6, hour=17, minute=0),
         datetime(year=2021, month=3, day=6, hour=18, minute=0)),
        (datetime(year=2021, month=3, day=7, hour=14, minute=0),
         datetime(year=2021, month=3, day=7, hour=15, minute=0)),
    ]

    date_range = (datetime(2021, 3, 5, 7, 0), datetime(2021, 3, 7, 18, 0))

    free_terms = get_free_time_list(busy_terms, date_range, open_from, open_to)

    print(free_terms)
