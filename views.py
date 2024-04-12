import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from django.http import JsonResponse
from django.conf import settings
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def lorenz(request):
    def lorenz_eq(t, xyz, sigma, rho, beta):
        x, y, z = xyz
        return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]
    
    sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
    initial_conditions = [1.0, 1.0, 1.0]
    t_span = (0, 100)
    t_eval = np.linspace(*t_span, 10000)
    sol = solve_ivp(lorenz_eq, t_span, initial_conditions, args=(sigma, rho, beta), t_eval=t_eval)
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol.y[0], sol.y[1], sol.y[2], color='b', alpha=0.7, linewidth=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorenz Çekicisi')
    
    file_path = os.path.join(settings.BASE_DIR, 'maps', 'lorenz.png')
    canvas = FigureCanvas(fig)
    canvas.print_png(file_path)
    plt.close(fig)
    
    return JsonResponse({'url': request.build_absolute_uri('/')[:-1] + settings.MEDIA_URL + 'maps/lorenz.png'})
