import janus_swi as janus

# Load your Prolog knowledge base file
janus.consult("knowledgebase.pl")

# Define and run your queries
queries = [
    ("is_capital('Lima', 'Libya')", "false"),
    ("is_capital('Lima', 'Peru')", "true"),
    ("city_continent('Manila', 'Asia')", "true"),
    ("city_continent('Manila', 'Europe')", "false"),
    ("is_in_country('New York', 'Egypt')", "false"),
    ("is_in_country('New York', 'United States of America')", "true"),
    ("is_in_country('Los Angeles', 'United States of America')", "true"),
    ("is_in_country('Barcelona', 'United States of America')", "false"),
    ("country_continent('Libya', 'Africa')", "true"),
    ("country_continent('Libya', 'Australia')", "false"),
    ("is_capital('Melbourne', 'Australia')", "false"),
    ("is_in_country('Melbourne', 'Australia')", "true")
]

# Execute and print results
for q, expected in queries:
    print(f"Query: {q}")
    result = list(janus.query(q))
    print("Result:", "true" if result else "false", "| Expected:", expected)
    print("-" * 40)
