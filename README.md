# STEAM for Vietnam Foundation Data Pipeline

<img src="https://static.ybox.vn/2020/8/5/1597995091967-Thie%CC%82%CC%81t%20ke%CC%82%CC%81%20kho%CC%82ng%20te%CC%82n%20(1).png"/>

## Assignment:
Our data/product analysts are working on a reporting dashboard so they would like to see
all students' related information including age, gender, schools they are attending (if any),
and the courses they’ve signed up at STEAM for Vietnam.

We would like you to create 3 tables in PostgreSQL database: **Students**, **Schools** and **Courses**, in
which:
- We want a random of 1000 students, 10 schools, and 3 courses. Each of them should
have a timestamp when it is created or updated (createdAt, updatedAt).
- We want a scheduled job to run everyday at 5:00 PM to pull data from those 3 tables
above and dump it into one BigQuery table

## Task Summary:
1. Create a docker-compose file to spin up new PostgreSQL database
3. Create appropriate database schemas for those 3 tables above
4. Write a script to random populate data into those tables
5. Write a schedule job to pull data from those 3 tables and push to BigQuery table
6. Provide instructions on how to run those steps above
7. Provide us with the github repository url so we can rerun it

## Usage:

    docker-compose up

The Airflow will run on http://localhost:8080/ <br>
The pgweb: http://localhost:8080/