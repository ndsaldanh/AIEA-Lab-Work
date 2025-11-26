from production import AND, OR, NOT, PASS, FAIL, IF, THEN, match, populate, simplify, variables
from data import zookeeper_rules

def backchain_to_goal_tree(rules, goal):
    # Define the goal as the root of our tree
    tree = [goal]

    # Check every rule to see if its consequent matches the goal
    for rule in rules:
        consequent = rule.consequent()    
        name = match(consequent, goal)

        #If the current rule doesn't match our goal, continue
        if name is None:
            continue

        subRules = rule.antecedent()       
        subRulesNamed = populate(subRules, name)

        #Recursively go through the subrules in antecedent
        if isinstance(subRulesNamed, str):
            subtree = backchain_to_goal_tree(rules, subRulesNamed)
        elif isinstance(subRulesNamed, AND):
            children = [backchain_to_goal_tree(rules, clause) for clause in subRulesNamed.conditions()]
            subtree = AND(*children)
        elif isinstance(subRulesNamed, OR):
            children = [backchain_to_goal_tree(rules, clause) for clause in subRulesNamed.conditions()]
            subtree = OR(*children)
        else:
            subtree = subRulesNamed

        tree.append(subtree)

    return simplify(OR(*tree))

print(backchain_to_goal_tree(zookeeper_rules, 'opus is an ungulate'))
