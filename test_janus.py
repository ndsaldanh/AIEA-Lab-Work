import janus_swi

# Run a simple Prolog query
result = janus_swi.query_once("member(X, [1, 2, 3, 4])")

print("Result from Prolog:", result)
