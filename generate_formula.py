import matplotlib.pyplot as plt

# Create figure with black background
fig, ax = plt.subplots(figsize=(5, 1))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Add LaTeX equation
equation = r"$L1\_Loss = \frac{1}{n} \sum_{i=1}^{n} | y_i - \hat{y}_i |$"
ax.text(0.5, 0.5, equation, color='white', fontsize=20, ha='center', va='center')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Save as PNG
plt.savefig("l1_loss_dark.png", dpi=300, bbox_inches='tight', facecolor='black')
plt.show()
