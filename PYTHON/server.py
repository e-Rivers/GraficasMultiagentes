# -*- coding: utf-8 -*-
"""
Server.py

Server setup that will be used to connect the model developed with
MESA and the graphical environment developed with Unity to display a
graphical solution of the simulation of city traffic.

Authors: Melissa Garduño Ruiz (A01748945), Omar Rodrigo Sorchini Puente (A01749389), Emilio Ri
os Ochoa (A01378965)
Date: December 4th, 2021
"""

from model import TrafficModel
from agent import *
from flask import Flask, request, jsonify
import os

# This parameters will be providen by Unity
carsNumber = 20
carsSpan = 2
lightSpan = 10

# Internal parameters
trafficModel = None
port = int(os.getenv("PORT", 8000))

app = Flask("Traffic Simulation")

"""
Function that gets executed when de /init service is called and serves the purpose of
initializing the model based on the parameters received from the Unity client
● Parameters: None
● Return: json structure to notify that there was success
"""
@app.route('/init', methods=['POST', 'GET'])
def initModel():
    global trafficModel, carsNumer, carsSpan, lightSpan

    if request.method == "POST":
        carsNumber = int(request.form.get("carsNumber"))
        carsSpan = int(request.form.get("carsSpan"))
        lightSpan = int(request.form.get("lightSpan"))

        print(request.form)
        trafficModel = TrafficModel(carsNumber, carsSpan, lightSpan)

        return jsonify({"message": "Parameters received, model initiated."})

"""
Function that gets executed when de /getCars service is called and serves the purpose of
informing the client about the changes in the coordinates of each car agent on the grid
● Parameters: None
● Return: json with the positions of all car agents in the model
"""
@app.route('/getCars', methods=['GET'])
def getCars():
    global trafficModel

    if request.method == "GET":
        carPositions = [{"x":x,"y":0,"z":z,"w":e.isStop,"id":e.unique_id} for (a,x,z) in trafficModel.grid.coord_iter() for e in a if isinstance(e, Car)]

        carPositions.sort(key=lambda x: x["id"])
        return jsonify({"positions": carPositions})

"""
Function that gets executed when de /update service is called and serves the purpose of
executing the step, that is, activate the agents to make their corresponding movement
● Parameters: None
● Return: json structure to notify the current step
"""
@app.route('/update', methods=['GET'])
def updateModel():
    global trafficModel

    if request.method == "GET":
        trafficModel.step()
        return jsonify({"message": "Model Updated!"})

if __name__=='__main__':
    app.run(host="localhost", port=port, debug=True) #"0.0.0.0"

