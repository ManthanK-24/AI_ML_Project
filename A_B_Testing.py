import random
from collections import defaultdict

class ABTestFramework:
    def __init__(self):
        self.groups = defaultdict(list)
        self.results = defaultdict(list)
    
    def assign_group(self, user_id, strategy):
        group = random.choice(['A', 'B'])
        self.groups[group].append((user_id, strategy))
        return group
    
    def log_interaction(self, user_id, group, success):
        self.results[group].append(success)
    
    def analyze_results(self):
        analysis = {}
        for group, results in self.results.items():
            analysis[group] = sum(results) / len(results) if results else 0
        return analysis

# Example usage
ab_test = ABTestFramework()
user_id = 123
strategy = 'new_algorithm'
group = ab_test.assign_group(user_id, strategy)
print(f"User {user_id} assigned to group {group}")

# Log some interactions
ab_test.log_interaction(user_id, group, success=True)
ab_test.log_interaction(user_id, group, success=False)

# Analyze results
results = ab_test.analyze_results()
print(results)
