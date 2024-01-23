from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://3.219.167.2:7687",
  auth=basic_auth("neo4j", "sunday-probabilities-presses"))

cypher_query2 = '''
MATCH (p:Person)-[:REVIEWED]->(m:Movie {title: $movie_title})
RETURN p.name AS userName
'''
# Function to execute the query
def find_users_who_rated_movie(movie_title):
    with driver.session(database="neo4j") as session:
        results = session.execute_read(
            lambda tx: tx.run(cypher_query2, movie_title=movie_title).data())
        for record in results:
            print(record['userName'])


cypher_query3 = '''
MATCH (person:Person  {name: $user_name})-[:REVIEWED]->(movie:Movie)
RETURN COUNT(movie) AS numberOfMovies, COLLECT(movie.title) AS movieTitles
'''
def get_user_movie_ratings(user_name):
    with driver.session(database="neo4j") as session:
        result = session.execute_read(
            lambda tx: tx.run(cypher_query3, user_name=user_name).single())
        if result:
            return {
                "userName": user_name,
                "numberOfMovies": result["numberOfMovies"],
                "ratedMovies": result["movieTitles"]
            }
        else:
            return {"userName": user_name, "message": "No ratings found"}

find_users_who_rated_movie('The Replacements')
user_ratings = get_user_movie_ratings('Jessica Thompson')
print(user_ratings)

driver.close()