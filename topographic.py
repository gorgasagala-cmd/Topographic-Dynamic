import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib
from screeninfo import get_monitors

matplotlib.use('TkAgg')

def get_screen_resolution():
    try:
        monitor = get_monitors()[0]
        return monitor.width, monitor.height
    except Exception as e:
        print(f"Gagal mendeteksi resolusi: {e}. Menggunakan default 1920x1080.")
        return 1920, 1080

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()
DPI = 100 

RESOLUSI_GRID = 250 

x = np.linspace(-SCREEN_WIDTH/DPI, SCREEN_WIDTH/DPI, RESOLUSI_GRID)
y = np.linspace(-SCREEN_HEIGHT/DPI, SCREEN_HEIGHT/DPI, RESOLUSI_GRID)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(SCREEN_WIDTH/DPI, SCREEN_HEIGHT/DPI), dpi=DPI, facecolor='black')

ax = fig.add_axes([0, 0, 1, 1], facecolor='black')

def generate_smooth_circles(frame):
    """
    Menghasilkan data ketinggian Z dengan fokus pada lengkungan bulat (setengah lingkaran).
    Menggunakan rumus radius jarak dari titik pusat yang bergerak.
    """
    t = frame * 0.02 
    
    cx1, cy1 = 3 * np.cos(t), 3 * np.sin(t)
    
    cx2, cy2 = 5 * np.sin(t*0.5), 3 * np.sin(t)
    
    cx3, cy3 = -6, -4
    
    dist1 = np.sqrt((X - cx1)**2 + (Y - cy1)**2)
    dist2 = np.sqrt((X - cx2)**2 + (Y - cy2)**2)
    dist3 = np.sqrt((X - cx3)**2 + (Y - cy3)**2)
    
    Z = np.sin(dist1 * 0.8 - t) 
    Z += 0.7 * np.cos(dist2 * 0.5 + t * 0.7)
    Z += 0.5 * np.sin(dist3 * 0.3)
    
    return Z

def update(frame):
    """Fungsi update untuk animasi."""
    ax.clear()
    ax.set_facecolor('black')
    
    Z = generate_smooth_circles(frame)
    
    ax.contour(X, Y, Z, levels=12, colors='white', linewidths=0.8, alpha=0.8)
    
    ax.set_axis_off() 
    return []

ani = FuncAnimation(fig, update, frames=np.arange(0, 10000), interval=33, cache_frame_data=False)

mng = plt.get_current_fig_manager()

if hasattr(mng, 'window'):

    mng.window.overrideredirect(True) 
    mng.window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+0+0") 
elif hasattr(mng, 'frame'):
    
    mng.frame.setWindowFlags(matplotlib.backends.qt_compat.QtCore.Qt.FramelessWindowHint)
    mng.full_screen_toggle()

print(f"Berjalan dalam mode Borderless Fullscreen ({SCREEN_WIDTH}x{SCREEN_HEIGHT}).")
print("Tutup jendela konsol/terminal untuk keluar.")

plt.show()