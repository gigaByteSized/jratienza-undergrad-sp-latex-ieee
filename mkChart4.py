import matplotlib.pyplot as plt

# Data
questions = [
    "Usefulness", "Ease of Use", "Ease of Learning", "Satisfaction"
]
mean_scores = [
    6.125,	4.00,	3.25,	4.285714286
]
# Plot
plt.figure(figsize=(12, 6))
plt.bar(questions, mean_scores, color=['#1f77b4']*1 + ['#ff7f0e']*1 + ['#7f7f7f']*1 + ['#bcbd22']*1)
plt.ylabel('Scores')
plt.title('Scores for all scales of the USE Questionnaire of PARA! Manager')
plt.xticks(rotation=45)
plt.ylim(1, 7)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add data labels
for i, score in enumerate(mean_scores):
    plt.text(i, score + 0.05, f'{score:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

