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
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from algorithms import perform_kmeans, perform_apriori
import numpy as np
from collections import defaultdict

app = Flask(__name__)

#Sample supermarket items
ITEMS = [
    "milk", "bread", "eggs", "cheese", "apples",
    "bananas", "chicken", "beef", "fish", "rice",
    "pasta", "cereal", "yogurt", "juice", "soda"
]

#In-memory storage for transactions (in a real app, use a database)
transactions = []


@app.route('/') #Homepage
def index():
    return render_template('index.html', items=ITEMS, transaction_count=len(transactions))


@app.route('/add_transaction', methods=['POST'])#Store transaction and update homepage.
def add_transaction():
    selected_items = request.form.getlist('items')
    if selected_items:
        transactions.append(selected_items)
    return redirect(url_for('index'))


@app.route('/view_transactions')
def view_transactions():
    return render_template('transactions.html', transactions=transactions)


@app.route('/analyze')
def analyze(): #Route that prepares data for analysis.
    if len(transactions) < 5:
        return redirect(url_for('index'))

    #Prepare data for algorithms
    item_indices = {item: idx for idx, item in enumerate(ITEMS)}
    binary_transactions = []
    #Binarize data for k-means clustering
    for transaction in transactions:
        binary = [0] * len(ITEMS)
        for item in transaction:
            binary[item_indices[item]] = 1
        binary_transactions.append(binary)

    # Perform data mining
    kmeans_results = perform_kmeans(np.array(binary_transactions), ITEMS)
    apriori_results = perform_apriori(transactions, ITEMS)

    return render_template('results.html', #Once analysis is done, send the user to the results page with the results of the analysis.
                           kmeans_results=kmeans_results,
                           apriori_results=apriori_results,
                           transaction_count=len(transactions))


if __name__ == '__main__':
    app.run(debug=True)