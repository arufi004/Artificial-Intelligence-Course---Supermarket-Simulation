"""
Name: 				    Anthony Rufin
Panther ID: 			6227314
Class: 					CAP5602 U01C 1255 - Introduction to Artificial Intelligence
Homework: 				HW 3 – Data Mining
Due: 					07/21/2025
What is this program? 	This program is a Supermarket simulation program. It allows the user to “purchase” items and make transactions from a supermarket.
                        Then, once there are at least five transactions, the user can request the program to sort the items into k-means clusters
                        and create association rules using the Apriori Algorithm.

"""
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)