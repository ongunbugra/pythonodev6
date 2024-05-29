import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

num_points = 1000
x_coords = np.random.randint(0, 1001, num_points)
y_coords = np.random.randint(0, 1001, num_points)

df = pd.DataFrame({'X': x_coords, 'Y': y_coords})

excel_file = 'kordinat.xlsx'
df.to_excel(excel_file, index=False)

df_read = pd.read_excel(excel_file)

def plot_points_with_grid(df, grid_size):
    x = df['X']
    y = df['Y']
    
    num_colors = (1000 // grid_size) ** 2
    colors = plt.cm.get_cmap('hsv', num_colors)
    
    fig, ax = plt.subplots()
    
    for i in range(0, 1000, grid_size):
        for j in range(0, 1000, grid_size):
            
            mask = (x >= i) & (x < i + grid_size) & (y >= j) & (y < j + grid_size)
            grid_x = x[mask]
            grid_y = y[mask]
            
    
            color_index = (i // grid_size) * (1000 // grid_size) + (j // grid_size)
            grid_color = colors(color_index)
            
    
            ax.scatter(grid_x, grid_y, c=[grid_color], s=10)
    
    ax.set_xticks(np.arange(0, 1001, grid_size))
    ax.set_yticks(np.arange(0, 1001, grid_size))
    ax.grid(which='both')
    
    plt.xlabel('X Koordinatlari')
    plt.ylabel('Y Koordinatlari')
    plt.title(f'Koordinatlar ve {grid_size}x{grid_size} Izgara')
    plt.show()


plot_points_with_grid(df_read, 50)

plot_points_with_grid(df_read, 100)

plot_points_with_grid(df_read, 200)
