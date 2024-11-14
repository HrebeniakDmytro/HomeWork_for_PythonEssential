from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Shape:
    def __init__(self):
        self.back_color = (155, 213, 117, 100)
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)

class Cone(Shape):
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        radius = 5
        height = 10
        resolution = 50
        
        theta = np.linspace(0, 2 * np.pi, resolution)
        z = np.linspace(0, height, resolution)
        theta, z = np.meshgrid(theta, z)
        x = radius * (height - z) / height * np.cos(theta)
        y = radius * (height - z) / height * np.sin(theta)
        
        ax.plot_surface(x, y, z, cmap='Oranges')
        ax.set_title('3D Cone')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Image with 3D cone was created")

class Paraboloid(Shape):
    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        resolution = 50
        x = np.linspace(-5, 5, resolution)
        y = np.linspace(-5, 5, resolution)
        x, y = np.meshgrid(x, y)
        z = x**2 + y**2
        
        ax.plot_surface(x, y, z, cmap='Purples')
        ax.set_title('3D Paraboloid')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Image with 3D paraboloid was created")

def work_with_obj(obj):
    obj.draw()
    obj.save()

def update_obj(obj):
    obj.erase()
    obj.save()

def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
                          '8. Cтворити 3D конус\n\t9. Cтворити 3D параболоїд\n\t10. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                cone = Cone()
                work_with_obj(cone)
            case 9:
                paraboloid = Paraboloid()
                work_with_obj(paraboloid)
            case 10:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
