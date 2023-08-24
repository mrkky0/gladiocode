import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



def x_isprime():
    x_prime_data=[]
    non_prime_data=[]
    for num in range(2, 2000):  # 0 ve 1 asal sayı değildir, bu yüzden 2'den başlıyoruz
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
            
        
        if is_prime:
            plt.polar(num,num,'g.')  
            x_prime_data.append(num)
        if num % 2 == 0:
            plt.polar(num,num,'y.')  
            pass

                            
        else:
            #plt.polar(num,num,'r.')
            if not num in non_prime_data:
                non_prime_data.append((num)%360)
 

    plt.polar(1750,1210,'y.')  
        
        

def other_td_prime():

    # Veri oluşturma
    x =np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499])
    
    y = np.linspace(-50, 50, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # 3D plot oluşturma
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Yüzeyi çizdirme
    ax.plot_surface(x, y, z, cmap='viridis')

    # Eksen etiketleri
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Başlığı ayarlama
    plt.title('3D Yüzey Çizimi')

 

 
        
def td_ploting_prime():
        # Veri oluşturma
        
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.linspace(0, 1, 100)
    theta, r = np.meshgrid(theta, r)
    z = r**2

    # 3D plot oluşturma
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot'u çizdirme
    ax.plot_surface(r * np.cos(theta), r * np.sin(theta), z, cmap='viridis')

    # Eksen etiketleri
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Başlığı ayarlama
    plt.title('Örnek 3D Plot')

x_isprime()

 
plt.show()

    
    
     

