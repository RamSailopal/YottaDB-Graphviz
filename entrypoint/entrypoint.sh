#!/bin/bash
/opt/yottadb/current/ydb << 'H'
S ^CARS("BMW",320,"Grey","Petrol",2016)="$10,200"
S ^CARS("BMW",330,"Blue","Petrol",2021)="$18,000"
S ^CARS("Nissan","Civic","Red","Diesel",2019)="$11,000"
S ^CARS("Nissan","Civic","Red","Diesel",2020)="$12,000"
S ^CARS("Nissan","Civic","Red","Petrol",2020)="$11,600"
S ^CARS("Nissan","Qashqai","Blue","Diesel",2018)="$12,400"
S ^CARS("Nissan","Qashqai","Green","Hybrid",2020)="$18,000"
H
chmod +x /tmp/run.sh
/tmp/run.sh
