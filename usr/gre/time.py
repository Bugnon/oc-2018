import time
t = time.time()
def t(x):
    secs= x
    sec=secs%60
    mins=secs//60
    min=mins%60
    hrs=mins//60
    hr=hrs%24
    jrs=hrs//24
    jr=jrs%365
    years=jrs//365
    year=years%100
    century=years//100
    print('Temps de', sec, 'secondes, ',  min, 'minutes, ', hr, 'heures et ', jr, 'jours, ', year, ' an(s) et ', century, ' siècle(s).')