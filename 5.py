import matplotlib.pyplot as plt

def plot_flowchart(procedure):
  """Plots a flowchart of the given procedure.

  Args:
    procedure: A list of strings describing the steps in the procedure.

  Returns:
    A matplotlib figure object containing the flowchart.
  """

  fig, ax = plt.subplots()

  # Create a flowchart object.
  flowchart = plt.flowchart.Flowchart()

  # Add the steps to the flowchart.
  for step in procedure:
    flowchart.add(step)

  # Draw the flowchart.
  flowchart.draw(ax)

  # Return the figure object.
  return fig

if __name__ == "__main__":
  # Get the procedure.
  procedure = [
    "Collect precipitation data from CMDN and ERA5",
    "Combine the data",
    "Use kriging interpolation method to generate a precipitation map",
    "Use the precipitation map to analyze flood patterns"
  ]

  # Plot the flowchart.
  fig = plot_flowchart(procedure)

  # Show the figure.
  plt.show()
