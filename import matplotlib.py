import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Set node styles
node_style = dict(boxstyle="round", facecolor="white")
start_node_style = dict(boxstyle="round", facecolor="green")
end_node_style = dict(boxstyle="round", facecolor="red")

# Draw nodes
ax.text(0.5, 0.9, "Study Area", ha="center", va="center", bbox=start_node_style)
ax.text(0.5, 0.75, "Data Source", ha="center", va="center", bbox=node_style)
ax.text(0.5, 0.6, "Flood Monitoring\nUsing Sentinel-1 Images", ha="center", va="center", bbox=node_style)
ax.text(0.5, 0.45, "Corresponding Validation\nfor Water Body Extraction", ha="center", va="center", bbox=node_style)
ax.text(0.5, 0.3, "Interpolation for\nPrecipitation Data", ha="center", va="center", bbox=node_style)
ax.text(0.5, 0.15, "Analysis of Flood\nPatterns", ha="center", va="center", bbox=node_style)
ax.text(0.5, 0.0, "Results and\nConclusions", ha="center", va="center", bbox=end_node_style)

# Draw arrows
arrow_args = dict(arrowstyle="->", color="black")
ax.annotate("", xy=(0.5, 0.85), xytext=(0.5, 0.78), arrowprops=arrow_args)
ax.annotate("", xy=(0.5, 0.7), xytext=(0.5, 0.63), arrowprops=arrow_args)
ax.annotate("", xy=(0.5, 0.55), xytext=(0.5, 0.48), arrowprops=arrow_args)
ax.annotate("", xy=(0.5, 0.4), xytext=(0.5, 0.33), arrowprops=arrow_args)
ax.annotate("", xy=(0.5, 0.25), xytext=(0.5, 0.18), arrowprops=arrow_args)
ax.annotate("", xy=(0.5, 0.1), xytext=(0.5, 0.03), arrowprops=arrow_args)

# Set axis limits and remove ticks
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Set the title
ax.set_title("Flowchart: Flood Monitoring Procedure")

# Display the flowchart
plt.show()
