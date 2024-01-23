# MongoDB-Neo4j

## Initiate the project

We work on the **--port 27017** but it's not a problem if you are using another one.

### Launch MongoDB as a service
```
mongod --dbpath <dataFolderPath> --logpath <logFilePath>
```

### Launch the connection
```
mongosh --port <port>
```

## Import the data
Our database is called crunchbase but it doesn't matter, you can edit the *.env* file.
```
mongoimport -d <databaseName> -c movies <path_to_movies.json>
```

## Setup and configure the project

First you have to go to an empty folder. You can now create the origin of the project.

```
mkdir projectNoSQL
cd projectNoSQL
```

### Virtual environment

```
python -m venv env-pymongo-fastapi-crud source env-pymongo-fastapi-crud/bin/activate
```

### Install the packages

Installation of multiple packages : **fastapi**, **pymongo**, **python-dotenv**, **neo4j**.
```
pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv neo4j
```

### Clone the git

```
git clone https://github.com/Emilien-Valain/MongoDB-Neo4j
```

## Edit the configuration (**Optional**)
Here is where you can edit the db_name and the url if they are different. It's in the *.env* file in the **MongoDB-Neo4j** folder.

#### Edit with an editor (Notepad etc.)
```
MONGODB_URL="mongodb://127.0.0.1:27017/tp?directConnection=true" ← You can change the port if needed
DB_NAME=crunchbase                                               ← Change the db_name if not the same
```
#### Edit with vim
```
cd MongoDB-Neo4j
vim .env                                                         ← edit the file
```

## Congratulation, you are now ready to run the application

```
python -m uvicorn main:app --reload
```

You can also run the *neoTest.py* file which is connected to neo4j and will show you some data.
