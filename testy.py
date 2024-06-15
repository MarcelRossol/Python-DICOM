from datetime import datetime
from collections import Counter


def get_oldest_comp(conn_data, comp_data):
    # Gets first competition id
    all_dates = []
    for comp in comp_data:
        all_dates.append(comp['comp_date'])
    date_format = "%Y-%m-%d"
    date_objects = [datetime.strptime(date, date_format) for date in all_dates]
    oldest_date = min(date_objects)
    oldest_date = oldest_date.strftime(date_format)

    for comp in comp_data:
        if comp['comp_date'] == oldest_date:
            first_comp_id = comp['id']

    # Gets oldest races
    oldest_races = []
    for conn in conn_data:
        if conn['comp_id'] == first_comp_id:
            oldest_races.append(conn)
    return oldest_races


def get_second_comp(conn_data, comp_data):
    # Gets first competition id
    all_dates = []
    for comp in comp_data:
        all_dates.append(comp['comp_date'])
    date_format = "%Y-%m-%d"
    date_objects = [datetime.strptime(date, date_format) for date in all_dates]
    oldest_date = min(date_objects)
    oldest_date = oldest_date.strftime(date_format)




    for comp in comp_data:
        if comp['comp_date'] == oldest_date:
            first_comp_id = comp['id']

    second_comp_id = first_comp_id + 1

    # Gets oldest races
    second_oldest_races = []
    for conn in conn_data:
        if conn['comp_id'] == second_comp_id:
            second_oldest_races.append(conn)
    return second_oldest_races




def sort_races_by_time(races, ev_id):
    # Define a function to convert 'time_mes' string to a datetime object
    def parse_time(time_str):
        return datetime.strptime(time_str, '%H:%M:%S')

    races_in_event = []
    for race in races:
        if race['ev_id'] == ev_id:
            races_in_event.append(race)

    # Sort the list of dictionaries using the 'time_mes' value
    sorted_races = sorted(races_in_event, key=lambda race: parse_time(race['time_mes']))

    return sorted_races


def assign_lanes(races):
    assigned_lanes = []
    lane = 1
    series = 1
    for race in races:
        if lane < 5:
            race['lane'] = lane
            race['series'] = series
            lane += 1
            assigned_lanes.append(race)
        else:
            race['lane'] = lane
            race['series'] = series
            assigned_lanes.append(race)

            lane = 1
            series += 1

    return assigned_lanes


def assign_first(conn_data, comp_data, ev_data):
    first_comp = get_oldest_comp(conn_data, comp_data)

    assigned_races = []
    for ev in ev_data:
        sorted_races_in_event = sort_races_by_time(first_comp, ev['id'])
        assigned_in_event = assign_lanes(sorted_races_in_event)
        assigned_races.extend(assigned_in_event)

    return assigned_races


def assign_second(conn_data, comp_data, ev_data):
    second_comp = get_second_comp(conn_data, comp_data)

    assigned_races = []
    for ev in ev_data:
        sorted_races_in_event = sort_races_by_time(second_comp, ev['id'])
        assigned_in_event = assign_lanes(sorted_races_in_event)
        assigned_races.extend(assigned_in_event)

    return assigned_races





def get_races(conn_data, comp_data, ev_data):
    curr_date = "2024-02-26"
    # Gest past competition ids
    date_format = "%Y-%m-%d"
    curr_date = datetime.strptime(curr_date, date_format)
    past_comps = []
    for comp in comp_data:
        comp_date = datetime.strptime(comp['comp_date'], date_format)
        if comp_date <= curr_date:
            past_comp_id = comp['id']
            past_comps.append(past_comp_id)

    # Gets all past races
    past_races_all = []
    for conn in conn_data:
        if conn['comp_id'] in past_comps:
            past_races_all.append(conn)

    # Gets unique patricipat ids
    part_id_all = []
    for race in past_races_all:
        part_id_all.append(race['usr_id'])
    counter = Counter(part_id_all)
    unique_part_ids = [item for item, count in counter.items() if count == 1]

    # Gets best times
    best_times_all = []
    for part_id in unique_part_ids:
        temp = []
        for race in past_races_all:
            if part_id == race['usr_id']:
                temp.append(race)




def group_series(conn_data):
    # Gets unique series
    series_all = []
    for race in conn_data:
        series_all.append(race['series'])
    unique_series = []
    for x in series_all:
        # check if exists in unique_list or not
        if x not in unique_series:
            unique_series.append(x)

    # Groups series
    grouped_series = []
    for series in unique_series:
        temp = []
        for race in conn_data:
            if race['series'] == series:
                temp.append(race)
        grouped_series.append(temp)

    return grouped_series






if __name__=='__main__':


    ser_data = [{'comp_id': 2, 'ev_id': 1, 'id': 18, 'lane': 1, 'position': 0, 'series': 1, 'time_mes': '00:46:00', 'usr_id': 11},
                {'comp_id': 2, 'ev_id': 1, 'id': 14, 'lane': 2, 'position': 0, 'series': 1, 'time_mes': '00:49:00', 'usr_id': 8},
                {'comp_id': 2, 'ev_id': 1, 'id': 22, 'lane': 3, 'position': 0, 'series': 1, 'time_mes': '00:49:00', 'usr_id': 13},
                {'comp_id': 2, 'ev_id': 1, 'id': 15, 'lane': 4, 'position': 0, 'series': 1, 'time_mes': '01:23:01', 'usr_id': 9},
                {'comp_id': 2, 'ev_id': 1, 'id': 20, 'lane': 5, 'position': 0, 'series': 1, 'time_mes': '01:33:01', 'usr_id': 12},
                {'comp_id': 2, 'ev_id': 1, 'id': 16, 'lane': 1, 'position': 0, 'series': 2, 'time_mes': '01:41:01', 'usr_id': 10},
                {'comp_id': 2, 'ev_id': 2, 'id': 23, 'lane': 1, 'position': 0, 'series': 1, 'time_mes': '01:04:00', 'usr_id': 13},
                {'comp_id': 2, 'ev_id': 2, 'id': 21, 'lane': 2, 'position': 0, 'series': 1, 'time_mes': '01:18:00', 'usr_id': 12},
                {'comp_id': 2, 'ev_id': 2, 'id': 17, 'lane': 3, 'position': 0, 'series': 1, 'time_mes': '03:05:02', 'usr_id': 10},
                {'comp_id': 2, 'ev_id': 2, 'id': 19, 'lane': 4, 'position': 0, 'series': 1, 'time_mes': '03:58:02', 'usr_id': 11}]



    conn_data = [{"comp_id":1,"ev_id":1,"id":1,"lane":0,"position":2,"series":0,"time_mes":"00:52:00","usr_id":1},
                 {"comp_id":1,"ev_id":2,"id":2,"lane":0,"position":0,"series":0,"time_mes":"02:00:01","usr_id":1},
                 {"comp_id":1,"ev_id":1,"id":3,"lane":0,"position":4,"series":0,"time_mes":"01:08:00","usr_id":2},
                 {"comp_id":1,"ev_id":2,"id":4,"lane":0,"position":0,"series":0,"time_mes":"02:29:01","usr_id":2},
                 {"comp_id":1,"ev_id":1,"id":5,"lane":0,"position":7,"series":0,"time_mes":"01:02:00","usr_id":3},
                 {"comp_id":1,"ev_id":1,"id":6,"lane":0,"position":1,"series":0,"time_mes":"00:32:00","usr_id":3},
                 {"comp_id":1,"ev_id":1,"id":7,"lane":0,"position":3,"series":0,"time_mes":"00:48:00","usr_id":4},
                 {"comp_id":1,"ev_id":1,"id":8,"lane":0,"position":6,"series":0,"time_mes":"01:24:01","usr_id":5},
                 {"comp_id":1,"ev_id":2,"id":9,"lane":0,"position":0,"series":0,"time_mes":"02:47:02","usr_id":5},
                 {"comp_id":1,"ev_id":1,"id":10,"lane":0,"position":8,"series":0,"time_mes":"00:47:00","usr_id":6},
                 {"comp_id":1,"ev_id":2,"id":11,"lane":0,"position":0,"series":0,"time_mes":"01:37:01","usr_id":6},
                 {"comp_id":1,"ev_id":1,"id":12,"lane":0,"position":5,"series":0,"time_mes":"01:19:00","usr_id":7},
                 {"comp_id":1,"ev_id":2,"id":13,"lane":0,"position":0,"series":0,"time_mes":"03:41:02","usr_id":7},
                 {"comp_id":2,"ev_id":1,"id":14,"lane":0,"position":0,"series":0,"time_mes":"00:49:00","usr_id":8},
                 {"comp_id":2,"ev_id":1,"id":15,"lane":0,"position":0,"series":0,"time_mes":"01:23:01","usr_id":9},
                 {"comp_id":2,"ev_id":1,"id":16,"lane":0,"position":0,"series":0,"time_mes":"01:41:01","usr_id":10},
                 {"comp_id":2,"ev_id":2,"id":17,"lane":0,"position":0,"series":0,"time_mes":"03:05:02","usr_id":10},
                 {"comp_id":2,"ev_id":1,"id":18,"lane":0,"position":0,"series":0,"time_mes":"00:46:00","usr_id":11},
                 {"comp_id":2,"ev_id":2,"id":19,"lane":0,"position":0,"series":0,"time_mes":"03:58:02","usr_id":11},
                 {"comp_id":2,"ev_id":1,"id":20,"lane":0,"position":0,"series":0,"time_mes":"01:33:01","usr_id":12},
                 {"comp_id":2,"ev_id":2,"id":21,"lane":0,"position":0,"series":0,"time_mes":"01:18:00","usr_id":12},
                 {"comp_id":2,"ev_id":1,"id":22,"lane":0,"position":0,"series":0,"time_mes":"00:49:00","usr_id":13},
                 {"comp_id":2,"ev_id":2,"id":23,"lane":0,"position":0,"series":0,"time_mes":"01:04:00","usr_id":13}]

    comp_data = [{"comp_date":"2024-02-20","comp_loc":"Wroclaw","comp_time":"08:00:00","id":1},
                 {"comp_date":"2024-02-25","comp_loc":"Krakow","comp_time":"07:00:00","id":2},
                 {"comp_date":"2024-03-15","comp_loc":"Debica","comp_time":"07:30:00","id":3}]

    ev_data = [{"event":"dowolny 50m","id":1},
               {"event":"dowolny 100m","id":2},
               {"event":"dowolny 200m","id":3},
               {"event":"dowolny 400m","id":4},
               {"event":"dowolny 800m","id":5},
               {"event":"dowolny 1500m","id":6},
               {"event":"klasyczny 50m","id":7},
               {"event":"klasyczny 100m","id":8},
               {"event":"klasyczny 200m","id":9},
               {"event":"grzbietowy 50m","id":10},
               {"event":"grzbietowy 100m","id":11},
               {"event":"grzbietowy 200m","id":12},
               {"event":"motylkowy 50m","id":13},
               {"event":"motylkowy 100m","id":14},
               {"event":"motylkowy 200m","id":15},
               {"event":"zmienny 100m","id":16},
               {"event":"zmienny 200m","id":17}]

    """
    x = assign_second(conn_data, comp_data, ev_data)
    for i in x:
        print(i)
    """
    y = group_series(ser_data)
    for i in y:
        print(i)


