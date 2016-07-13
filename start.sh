#Set Sound zo 3.5mm Klinke
sudo amixer cset numid=3 1
#Volle Lautstärke
amixer set PCM -- 400
#Starte Nodejs server im Hintergrund
nohup node '/home/pi/ITS_2016/app/app.js' &
#Starte python-DMX im Hintergrund
nohup python '/home/pi/ITS_2016/Scripts/python/client.py' &

