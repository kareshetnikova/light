# Подключение библиотек
import numpy as np
import matplotlib.pyplot as plt
import imageio
from PIL import Image


def obrezka(fileName, outfileName):
    with Image.open(fileName) as red:
        red.load()

    obr_red = red.rotate(360)
    obr_red = obr_red.crop(((480, 300, 590, 500))) #сверху слева снизу справа

    obr_red.save(outfileName)

# каждый пиксель в кортеж из трех значений ргб
def readIntensity(photoName, plotName, lamp, surface):
    im = Image.open(photoName)
    photo = imageio.v2.imread(photoName)
    cut = photo.swapaxes(0, 1)
    intensity = np.mean(cut, axis=(2, 0))
    intensity = [(i - 60) for i in intensity]

    fig = plt.figure(figsize=(10, 3), dpi=200)
    plt.plot(intensity, 'w', label='{} / {}'.format(lamp, surface))
    plt.imshow(cut, origin='lower')
    plt.title('Интенсивность отражённого излучения')
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')
    plt.legend()
    plt.savefig(plotName)
    return intensity


# Функция калибровки
# находит максимумы значений(самые яркие полосы)
def calibration(m, my):
    max1 = 0
    max2 = 0
    n1 = 0
    n2 = 0
    for i in range(150, 200):
        if m[i] > max1:
            n1 = i
            max1 = m[i]
    for i in range(0, 100):
        if m[i] > max2:
            n2 = i
            max2 = m[i]
    calibration_value = (110 / (n1 - n2))
    mn = []
    for i in range(len(my)):
        mn.append(i * calibration_value + 546 - n1 * calibration_value)
    return mn


# Рассчет значений альбедо
def albedo_znach(m1, m2, n):
    alb = []
    for i in range(n):
        if m2[i] <= 0.1:
            alb.append(0)
        else:
            alb.append(m1[i] / m2[i])

    return alb


# Функция построения графиков интенсивностей
def intensities(my, mb, mw, mr, mg, mn):
    fig = plt.figure(figsize=(10, 5), dpi=200)
    plt.plot(mn, my, "y", linewidth=0.8, label='Жёлтый лист')
    plt.plot(mn, mb, "b", linewidth=0.8, label='Синий лист')
    plt.plot(mn, mw, "w", linewidth=0.8, label='Белый лист')
    plt.plot(mn, mr, "r", linewidth=0.8, label='Красный лист')
    plt.plot(mn, mg, "g", linewidth=0.8, label='Зелёный лист')
    plt.axis([350, 600, 0, 80])
    ax = plt.gca()
    ax.set_facecolor('lightgray')
    plt.ylabel('Яркость', fontsize=15)
    plt.xlabel('Длина волны[нм]', fontsize=15)
    plt.title('Отраженная интенстивность излучения лампы накаливания', fontsize=15, fontweight='bold')
    ax.minorticks_on()
    plt.grid(which="both", linewidth=1)
    plt.grid(which="minor", ls="--", linewidth=0.25)
    plt.legend(fontsize=13)
    plt.savefig('intensities.png')


# Построение графика альбедо
def albedos(my, mb, mw, mr, mg, mn):
    fig = plt.figure(figsize=(10, 5), dpi=200)
    plt.plot(mn, my, "y", linewidth=0.8, label='Жёлтый лист')
    plt.plot(mn, mb, "b", linewidth=0.8, label='Синий лист')
    plt.plot(mn, mw, "w", linewidth=0.8, label='Белый лист')
    plt.plot(mn, mr, "r", linewidth=0.8, label='Красный лист')
    plt.plot(mn, mg, "g", linewidth=0.8, label='Зелёный лист')
    plt.axis([350, 600, 0, 2])
    ax = plt.gca()
    ax.set_facecolor('lightgray')
    plt.ylabel('Альбедо', fontsize=15)
    plt.xlabel('Длина волны[нм]', fontsize=15)
    plt.title('Альбедо поверхностей', fontsize=15, fontweight='bold')
    ax.minorticks_on()
    plt.grid(which="both", linewidth=1)
    plt.grid(which="minor", ls="--", linewidth=0.25)
    plt.legend(fontsize=13)
    plt.savefig('albedos.png')
    plt.show()