#!/usr/bin/env python3
# Module müssen Namen haben die den py-Regeln entsprechen
# _module, modul - ok
# 11_modul, 11-modul, modul-11 - nicht ok
import module

print(dir())
print(dir(module))

tipp = module.lese_tipp()
ziehung = module.erzeuge_ziehung()
ergebnis = module.werte_spiel_aus(tipp, ziehung)
module.gebe_ergebnis_aus(ergebnis)

