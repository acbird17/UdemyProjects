from turtle import Turtle
import pandas
import csv

class Write(Turtle):
    def __init__(self):
        super().__init__()
        data = pandas.read_csv("./50_states.csv")