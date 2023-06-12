import numpy as np
from scipy.interpolate import griddata

# Generate sample data
x_cmdn = np.random.random(100)  # Sample x coordinates from CMDN
y_cmdn = np.random.random(100)  # Sample y coordinates from CMDN
precip_cmdn = np.random.random(100)  # Sample precipitation data from CMDN

x_era5 = np.random.random(200)  # Sample x coordinates from ERA5
y_era5 = np.random.random(200)  # Sample y coordinates from ERA5
precip_era5 = np.random.random(200)  # Sample precipitation data from ERA5

# Combine CMDN and ERA5 data
x_combined = np.concatenate((x_cmdn, x_era5))
y_combined = np.concatenate((y_cmdn, y_era5))
precip_combined = np.concatenate((precip_cmdn, precip_era5))

# Define the grid for interpolation
grid_x, grid_y = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))

# Perform Kriging interpolation
grid_precip = griddata((x_combined, y_combined), precip_combined, (grid_x, grid_y), method='cubic')

# Plot the interpolated precipitation map
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.imshow(grid_precip, extent=(0, 1, 0, 1), origin='lower', cmap='rainbow')
plt.colorbar(label='Precipitation (mm)')
plt.title('Interpolated Precipitation Map')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
