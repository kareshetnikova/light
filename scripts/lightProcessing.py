
import lightfunctions11 as j

j.obrezka("red-tungsten.png", "red-tungsten_.png")
j.obrezka("white-mercury.png", "white-mercury_.png")
j.obrezka("white-tungsten.png", "white-tungsten_.png")
j.obrezka("yellow-tungsten.png", "yellow-tungsten_.png")
j.obrezka("blue-tungsten.png", "blue-tungsten_.png")
j.obrezka("green-tungsten.png", "green-tungsten_.png")



my = j.readIntensity("yellow-tungsten_.png", "1yellow-tungsten", "Лампа накаливания", "Жёлтый лист")
mb = j.readIntensity("blue-tungsten_.png", "1blue-tungsten", "Лампа накаливания", "Синий лист")
mw = j.readIntensity("white-tungsten_.png", "1white-tungsten", "Лампа накаливания", "Белый лист")
mr = j.readIntensity("red-tungsten_.png", "1red-tungsten", "Лампа накаливания", "Красный лист")
mg = j.readIntensity("green-tungsten_.png", "1green-tungsten", "Лампа накаливания", "Зелёный лист")
mc = j.readIntensity("white-mercury_.png", "1white-mercury", "Ртутная лампа", "Белый лист")
mn = j.calibration(mc, my)
n = len(mn)

albmy = j.albedo_znach(my, mw, n)
albmb = j.albedo_znach(mb, mw, n)
albmw = j.albedo_znach(mw, mw, n)
albmr = j.albedo_znach(mr, mw, n)
albmg = j.albedo_znach(mg, mw, n)


# Построение графика интенсивностей и альбедо
j.intensities(my, mb, mw, mr, mg, mn)
j.albedos(albmy, albmb, albmw, albmr, albmg, mn)