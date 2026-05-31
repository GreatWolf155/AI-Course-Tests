from db import run_query_select, run_update_query


"""
Q1
Write and run a Python script (like we did in class) that connects to world_cups.db and prints all World Cups won by Brazil.
Hint: use a parameterized query with ? — do not hardcode the value in the SQL string
"""
brazil_wins = run_query_select("SELECT * FROM world_cups WHERE winner = 'Brazil'")
for w in brazil_wins:
    print(w)

"""
Q2
Write and run a Python script (like we did in class) that connects to world_cups.db and updates the 2002 World Cup host country to 'East Asia'.
Hint: use UPDATE with ? parameters, then conn.commit() and print cursor.rowcount
"""

run_update_query("""
UPDATE world_cups SET host_country = ?
WHERE year = ?
""", ('East Asia', 2002))

host = run_query_select("""SELECT host_country FROM world_cups
WHERE year = 2002;""")
for h in host:
    print(h)