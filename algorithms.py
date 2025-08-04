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
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd


def perform_kmeans(data, items, n_clusters=3):
    #Perform K-means clustering on transaction data.
    #Determine optimal number of clusters if we have enough transactions
    if len(data) > 10:
        n_clusters = min(4, len(data) // 3)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42) #Using scikit-learn's KMeans implementation to generate clusters.
    clusters = kmeans.fit_predict(data)

    #Analyze cluster characteristics
    cluster_items = {}
    for cluster_id in range(n_clusters):
        cluster_data = data[clusters == cluster_id]
        if len(cluster_data) > 0:
            item_freq = cluster_data.mean(axis=0) #Computes the purchase probability per item within the generated clusters
            top_items_idx = np.argsort(item_freq)[-3:][::-1]  #Top 3 items in each cluster
            top_items = [(items[i], round(item_freq[i] * 100, 1)) for i in top_items_idx]
            cluster_items[f"Cluster {cluster_id + 1}"] = {
                "size": len(cluster_data),
                "top_items": top_items,
                "description": f"Customers who frequently buy {', '.join([items[i] for i in top_items_idx])}"
            }

    return {#Returns dictionary with cluster sizes, top items and human readable descriptions.
        "n_clusters": n_clusters,
        "cluster_distribution": {f"Cluster {i + 1}": sum(clusters == i) for i in range(n_clusters)},
        "cluster_details": cluster_items,
        "interpretation": "Clusters group customers with similar purchasing patterns."
    }


def perform_apriori(transactions, items, min_support=0.2, min_threshold=0.6):
    #Perform association rule mining using Apriori algorithm.
    if len(transactions) < 10:
        min_support = 0.3  # Higher support for small datasets

    #Data Processing
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    #Find frequent itemsets
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

    if len(frequent_itemsets) == 0:
        return {"message": "No significant association rules found with current settings."}

    #Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_threshold)

    #Filter and format rules
    interesting_rules = []
    for _, rule in rules.iterrows():
        if len(rule['antecedents']) + len(rule['consequents']) <= 4:  # Limit rule complexity
            interesting_rules.append({#Dictionary containing a human readable version of the rules, along with the confidence, support, and lift.
                "rule": f"If you buy {', '.join(rule['antecedents'])}, you're likely to also buy {', '.join(rule['consequents'])}",
                "confidence": round(rule['confidence'] * 100, 1),
                "support": round(rule['support'] * 100, 1),
                "lift": round(rule['lift'], 2)
            })

    #Sort by confidence and lift
    interesting_rules.sort(key=lambda x: (-x['confidence'], -x['lift']))

    return {
        "rules": interesting_rules[:10],  # Return top 10 rules
        "interpretation": "Association rules show products that are frequently purchased together."
    }