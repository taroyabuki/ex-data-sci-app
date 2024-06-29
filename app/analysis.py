import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
import matplotlib

matplotlib.rcParams['font.family'] = 'IPAexGothic'

def perform_linear_regression(data):
    X = np.array([d[0] for d in data]).reshape(-1, 1)
    y = np.array([d[1] for d in data])
    
    model = LinearRegression()
    model.fit(X, y)
    
    slope = model.coef_[0]
    intercept = model.intercept_
    r_squared = model.score(X, y)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5)
    plt.plot(X, model.predict(X), color='red', linewidth=2)
    plt.xlabel('身長 (cm)')
    plt.ylabel('体重 (kg)')
    plt.title('身長と体重の関係')
    
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    plot_path = os.path.join(static_dir, 'regression_plot.png')
    plt.savefig(plot_path)
    plt.close()
    
    return slope, intercept, r_squared