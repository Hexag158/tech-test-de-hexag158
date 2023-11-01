# TECH TEST SOLUTION
This repo is my work on the tech test for DE from FindMyPast just for learning purposes. I started learning Docker a month ago and I think this test could be a great chance for practicing.
## Build Docker Images
This command will create all the images that are defined from the docker-compose.yml file
```
docker compose build
```
## For the MySQL database containers
#### Start the database by using:
```
docker compose up database
```
#### Copy the my_schema.sql file from the local to container
Since containers run on a seperate file system from the host machine, we have to make sure the file can be found in the containers' files to execute it
```
docker cp /path/in/local <container_id_or_name>:/path/in/container
```
#### Execute the SQL query
```
docker exec -it <container_id_or_name>  bash -c "mysql -h localhost -P 3306 --protocol=tcp -u codetest -pswordfish codetest < /my_schema.sql"
```
#### Access the database from bash
We can access the database from bash by open the cmd of the container
```
docker exec -it <container_id_or_name> bash
```
Using this bash script to access the db, type password: swordfish
```
mysql -h localhost -P 3306 --protocol=tcp -u codetest -p codetest
```
## For the Upload containers
#### Run the container
```
docker compose run upload
```
#### Run the Python script to upload the data
Since I have defined the WORKDIR as App folder we just need to call directly upload.py
```
docker exec -it <container_id_or_name> bash -c "python upload.py"
```
The summary_result.json will be in the Data folder
## Close everything
```
docker compose down
```
