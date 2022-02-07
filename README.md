# YottaDB-Graphviz

This repo demonstrates how YottaDB globals can be displayed as a chart generated by Graphviz.

To view the demo on Gitpod:

A global ^CARS is already created with the following data:

     ^CARS("BMW",320,"Grey","Petrol",2016)="$10,200"
     ^CARS("BMW",330,"Blue","Petrol",2021)="$18,000"
     ^CARS("Nissan","Civic","Red","Diesel",2019)="$11,000"
     ^CARS("Nissan","Civic","Red","Diesel",2020)="$12,000"
     ^CARS("Nissan","Civic","Red","Petrol",2020)="$11,600"
     ^CARS("Nissan","Qashqai","Blue","Diesel",2018)="$12,400"
     ^CARS("Nissan","Qashqai","Green","Hybrid",2020)="$18,000"
     
globalgraph.py then holds code to connect to the CARS global in the YottaDB database running in a Docker container. Each nested subscript is looped on, generating data for Graphviz to generate a PDF chart.

Once the Gitpod environment is provisioned, a new document will be generated as below:


