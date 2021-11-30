# -*- coding: utf-8 -*-
"""
Server.py

Server setup that will be used to connect the model developed with
MESA and the graphical environment developed with Unity to display a
graphical solution of the simulation of 5 robots organizing warehouse boxes.

Authors: Melissa Garduño Ruiz (A01748945), Omar Rodrigo Sorchini Puente (A01749389), Emilio Rios Ochoa (A01378965)
Date: November 23rd, 2021
"""

from agent import *
from model import RandomModel
from flask import Flask, request, jsonify

app = Flask("Traffic simulator")

"""
Function that gets executed when de /init service is called and serves the purpose of
initializing the model based on the parameters received from the Unity client
● Parameters: None
● Return: json structure to notify that there was success
"""
@app.route('/init', methods=['POST', 'GET'])
def initModel():
    global orgModel, number_robots, width, height

    if request.method == 'POST':
        number_robots = int(request.form.get('NRobots'))
        number_boxes = int(request.form.get('NBoxes'))
        width = int(request.form.get('width'))
        height = int(request.form.get('height'))
        max_time = int(request.form.get('MTime'))

        print(request.form)
        print(number_robots, width, height)
        orgModel = OrgModel(number_robots, number_boxes, width, height, max_time)

        return jsonify({"message":"Parameters recieved, model initiated."})

"""
Function that gets executed when de /getRobots service is called and serves the purpose of
informing the client about the changes in the coordinates of each robot agent on the grid
● Parameters: None
● Return: json with the positions of all robot agents in the model
@app.route('/getRobots', methods=['GET'])
def getRobots():
    global orgModel

    if request.method == 'GET':
        robPositions = [{"x": x, "y":0.5, "z":z} for (a, x, z) in orgModel.grid.coord_iter() for e in a if isinstance(e, RobotAgent)]

        return jsonify({'positions':robPositions})

Function that gets executed when de /getObstacles service is called and serves the purpose of
informing the client about the changes in the coordinates of each wall block agent on the grid,
since this blocks can't be moved, this function will only be called once at the beginning of
the program execution
● Parameters: None
● Return: json with the positions of all obstacles agents in the model
@app.route('/getObstacles', methods=['GET'])
def getObstacles():
    global orgModel

    if request.method == 'GET':
        obsPositions = [{"x": x, "y":1, "z":z} for (a, x, z) in orgModel.grid.coord_iter() for e in a if isinstance(e, ObstacleAgent)] 

        return jsonify({'positions':obsPositions})

Function that gets executed when de /getBoxes service is called and serves the purpose of
informing the client about the changes in the coordinates of each box agent on the grid
● Parameters: None
● Return: json with the positions of all box agents in the model
@app.route('/getBoxes', methods=['GET'])
def getBoxes():
    global orgModel

    if request.method == 'GET':
        boxPositions = [{"x": x, "y":e.yPos, "z":z} for (a, x, z) in orgModel.grid.coord_iter() for e in a if isinstance(e, BoxAgent)] 

        return jsonify({'positions':boxPositions})

Function that gets executed when de /update service is called and serves the purpose of
executing the step, that is, activate the agents to make their corresponding movement
● Parameters: None
● Return: json structure to notify the current step
@app.route('/update', methods=['GET'])
def updateModel():
    global currentStep, orgModel
    if request.method == 'GET':
        orgModel.step()
        currentStep += 1
        print("\033[41mCurrent Step:", currentStep, "\033[0m")
        return jsonify({'message':f'Model updated to step {currentStep}.', 'currentStep':currentStep})
"""

if __name__=='__main__':
    app.run(host="localhost", port=8585, debug=True)
