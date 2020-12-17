To run:
  1. Configure db_config.py to match your local MySQL and Neo4j settings
  2. run `py nutritio.py' (it will automatically setup the tables and dummy data for you)
  3. To auto create / reset table, comment nutrition.py line before app.run (on if __name__ = "__main__" block)

On progress:
  1. AI algorithm for meal generation [done]
  2. Prototype for NoSQL section of our program. Currently developing Neo4j. [done]


TODO:
  1. Host codebase in a web-server so it can be accessed by others (cPanel, heroku?)
  2. Fix the front-end for the social features [By 12/23/2020]
