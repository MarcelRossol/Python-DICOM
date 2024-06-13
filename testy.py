

def assign_series_lane(conn_data, comp_data, ev_data, curr_date):
    # Pozyskuje id aktualnej comp
    for comp in comp_data:

        if comp['comp_date'] == curr_date:
            curr_comp_id = comp['id']


    print(curr_comp_id)
"""    
    past_races = []
    for race in conn_data:
        if race['comp_id'] < curr_comp_id:
            
            past_races.append(race) 
        
        
        
    for i in past_races:
        print(i)
    """








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

assign_series_lane(conn_data, comp_data, ev_data, curr_date)