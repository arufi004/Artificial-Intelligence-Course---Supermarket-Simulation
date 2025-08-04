# Artificial-Intelligence-Course---Supermarket-Simulation

Name:  	 	 	 	Anthony Rufin 
Panther ID:  	 	 	 	6227314 
Class:  	 	 	 	CAP5602 U01C 1255 - Introduction to Artificial 
Intelligence 
Homework:   	 	 	HW 3 – Data Mining  
Due:   	 	 	 	07/21/2025 
What is this program?  	 	This program is a Supermarket simulation program. It allows the user to “purchase” items and make transactions from a supermarket. Then, once there are at least five transactions, the user can request the program to sort the items into k-means clusters and create association rules using the Apriori Algorithm. 
 
File Structure: 
HW1-Search:  	static/  	 	styles.css  	templates/ 
  index.html -> This is the html file holding the main html code for the flask web application   results.html -> This is the html file for showing the generated clusters and association rules.   transactions.html -> This is the html file for displaying created transactions.  app.py -> This is the main project file, used to host the flask program. 
 algorithm.py -> This is the project file that contains the k-means clustering and the apriori algorithm.  run.py -> A Helper file used to create the app.route for the executable file. 
 
Use the HW3_DataMining.exe file and copy the address given onto a browser to run the program.
Note that the file couldn't be uploaded to github due to file size. To access the exe, please use this link: https://fiudit-my.sharepoint.com/:u:/g/personal/arufi004_fiu_edu/Eb5vKVP-me5KpE-h04L4laEBLGqy7MtlrUDf-GWEG77OoA?e=cLY7v5
 
Libraries used: 
Flask - For creating the web application, uses Flask, render_template, request, jsonify sklearn -> Used to handle the k-means clustering mlxtend -> used to handle the apriori and Transaction encoding. 
numpy -> used for formatting the results pandas -> Used for creating a dataframe to store the transactions for the apriori function 
 
----------------------------------------------------------------------------------------------------------------------------------------------- 
 
app.py app.py is the main file for this project. Like the previous two projects, it uses flask to create a web application to host the super market application.  
app.py has four routes: First is the index, which hosts the main page of the program. The route add_transaction refreshes the index page and adds the created transaction to the supermarket database. View_transaction allows the user to see all the transactions created. Analyze sends the user to the results page, and calls the algorithm functions (kmeans and apriori) to analyze the data and create k-means clusters and association rules app.py also has a list of 15 sample products that one would buy at a supermarket. These are: milk, bread, eggs, cheese, apples, bananas, chicken, beef, fish, rice, pasta, cereal, yogurt, juice, and soda. App.py also has an empty list to store each transactions (as a list of lists). 
 
------------------------------------------------------------------------------------------------------------------
------------------------------ algorithms.py algorithms.py is the main file for algorithms in this project. It hosts the two main algorithms used in this project, k-means and apriori.  
perform_kmeans is a function that performs the kmeans clustering algorithm on the retrieved transaction data obtained from the main flask program. It takes two arguments: data, which is the binarized transactions from the main flask program, and items, which are a list of strings representing the labels for each item available in the supermarket simulation. The raw transactions are converted into binary data and then clustered by the function. The function then uses items to translate the cluster centroids to generate rational insights into the data provided.  
perform_kmeans also initializes a variable n_clusters, which is, by default, set to 3 clusters. Depending on the amount of data, the program will decide the amount of clusters to create for this program. The program uses scikit-learn’s k-means implementation due to it being more optimized and produces more accurate, rational clusters. After generating the cluster, the program computes the purchase probability for each item within each cluster, and them sorts the items by probability. The function then returns dictionary with cluster sizes, top 3 items and human readable descriptions. 
 
perform_apriori is a function that generates the association rules between items using the apriori algorithm. It takes two inputs: transactions, and items. Transactions, unlike data, is simply a list of all transactions made by the user. Each list represents a transaction of items, where the product names are listed as strings. Items is the complete list of all possible products in the program.  
 The program automatically sets the minimum support to 0.3 if there are fewer than 10 transactions. Otherwise, the minimum support is 0.2. min_threshold represents the threshold for the confidence level each association rule must have to be considered as significant. From there, the program uses mlxtend to aid in creating the association rules, and pandas to manipulate the transaction data. The output of this function includes the confidence, support, and lift of the rule, along with a human readable format of the rule: Example “If you buy cereal, you're likely to also buy milk”.  
 
 
 
