# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:26:24 2019

@author: aldos
"""

import json

data = {}
data['jobs'] = []
data['bids'] = []

def create_dummy():
    jobs_budget = [8000, 10000, 2000]
    jobs_date = ["2018-01-12", "2017-04-29", "2017-04-11"]
    jobs_origin =["JKT", "DEN", "MDN"]
    jobs_dest = ["SBY", "BDG", "SMG"]
    jobs_id = [1, 2, 3]
    
    i = 0
    for j in jobs_budget:
        data['jobs'].append({'jobs_date':jobs_date[i],'jobs_id':jobs_id[i],'jobs_budget': jobs_budget[i], 'jobs_origin':jobs_origin[i], 'jobs_dest':jobs_dest[i]})
        i = i + 1

    bids_price = [9000, 3200, 5000]
    bids_vehicle = ["Tronton", "Pickup", "Fuso"]
    bids_id = [1,2,3]
    
    i = 0
    for j in jobs_budget:
        data['bids'].append({'bids_price':bids_price[i],'bids_vehicle':bids_vehicle[i],'bids_id': bids_id[i]})
        i = i + 1

    
if __name__ == '__main__':
    
    create_dummy()
    
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)