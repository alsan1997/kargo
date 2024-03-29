# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:54:45 2019

@author: aldos
"""

from flask import Flask, jsonify, request
import json
app = Flask(__name__)

with open('data.txt') as json_file:
    data = json.load(json_file)

def mergesort(A, data_types):
    
    if len(A) > 1:
        if data_types == "jobs":
            types = "jobs_budget"
        else:
            types = "bids_price"
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        
        mergesort(lefthalf, data_types)
        mergesort(righthalf, data_types)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][types] < righthalf[j][types]:
                A[k] = lefthalf[i]
                i = i + 1
            else:
                A[k] = righthalf[j]
                j = j + 1
                
            k = k + 1
        
        while i < len(lefthalf):
            A[k] = lefthalf[i]
            k = k + 1
            i = i + 1
            
        while j < len(righthalf):
            A[k] = righthalf[j]
            k = k + 1
            j = j + 1
            
        return A


@app.route('/data/jobs', methods = ["GET"])
def return_sorted_jobs():
    #unsorted_jobs = data['jobs']
    sorted_jobs = mergesort(data['jobs'], "jobs")
        
    return jsonify({'sorted_jobs':sorted_jobs})    
   

@app.route('/data/bids', methods = ["GET"])
def return_sorted_bids():
    sorted_bids = mergesort(data['bids'], "bids")
    return jsonify({'sorted_bids':sorted_bids})
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)