import matplotlib.pyplot as plt

# Data
questions = [
    "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10",
    "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20",
    "Q21", "Q22", "Q23", "Q24", "Q25", "Q26", "Q27", "Q28", "Q29", "Q30"
]
mean_scores = [
    6.2381, 6.2857, 6.6667, 6.0952, 6.0476, 6.0000, 6.2857, 6.2381, 6.5238, 6.5714,
    6.5714, 6.1429, 6.1905, 6.2381, 6.0952, 5.9048, 6.2381, 6.2381, 6.2857, 6.3333,
    6.5238, 6.3810, 6.3810, 6.2857, 6.5238, 6.2857, 6.1905, 6.2857, 6.2857, 6.2381
]

# Plot
plt.figure(figsize=(12, 6))
plt.bar(questions, mean_scores, color=['#1f77b4']*8 + ['#ff7f0e']*9 + ['#7f7f7f']*4 + ['#bcbd22']*9)
plt.xlabel('Questions')
plt.ylabel('Mean Scores')
plt.title('Mean Scores for Usefulness, Ease of Use, Ease of Learning, and Satisfaction (USE) of PARA! Client')
plt.xticks(rotation=45)
plt.ylim(1, 7)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels
for i, score in enumerate(mean_scores):
    plt.text(i, score + 0.05, f'{score:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

