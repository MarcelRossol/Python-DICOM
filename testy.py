from datetime import datetime
from collections import Counter

def assign_first_lanes(conn_data, comp_data, ev_data):
    # Gets first competition id
    all_dates = []
    for comp in comp_data:
        all_dates.append(comp['comp_date'])
    date_format = "%Y-%m-%d"
    date_objects = [datetime.strptime(date, date_format) for date in all_dates]
    oldest_date = min(date_objects)
    oldest_date = oldest_date.strftime(date_format)

    oldest_races = []
    for conn in conn_data:




    print(oldest_date)






def assign_series_lane(conn_data, comp_data, ev_data, curr_date):

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







    for comp in past_races_all:
        print(comp)









conn_data = [{"comp_id":1,"ev_id":1,"id":1,"lane":0,"position":0,"series":0,"time_mes":"05:33:04","usr_id":1},
             {"comp_id":1,"ev_id":2,"id":2,"lane":0,"position":0,"series":0,"time_mes":"04:43:03","usr_id":1},
             {"comp_id":1,"ev_id":1,"id":3,"lane":0,"position":0,"series":0,"time_mes":"03:22:02","usr_id":2},
             {"comp_id":1,"ev_id":2,"id":4,"lane":0,"position":0,"series":0,"time_mes":"09:56:07","usr_id":2},
             {"comp_id":1,"ev_id":1,"id":5,"lane":0,"position":0,"series":0,"time_mes":"08:01:06","usr_id":2},
             {"comp_id":1,"ev_id":2,"id":6,"lane":0,"position":0,"series":0,"time_mes":"02:23:01","usr_id":3},
             {"comp_id":1,"ev_id":1,"id":7,"lane":0,"position":0,"series":0,"time_mes":"09:15:06","usr_id":4},
             {"comp_id":1,"ev_id":2,"id":8,"lane":0,"position":0,"series":0,"time_mes":"09:07:06","usr_id":5},
             {"comp_id":1,"ev_id":1,"id":9,"lane":0,"position":0,"series":0,"time_mes":"02:07:01","usr_id":5},
             {"comp_id":1,"ev_id":2,"id":10,"lane":0,"position":0,"series":0,"time_mes":"01:43:01","usr_id":5}]

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

curr_date = "2024-03-10"

#assign_series_lane(conn_data, comp_data, ev_data, curr_date)
assign_first_lanes(conn_data, comp_data, ev_data)