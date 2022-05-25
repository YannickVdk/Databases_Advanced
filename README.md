# Databases_Advanced

Download VirtualBox: (url: https://www.virtualbox.org/)

Download Ubuntu: (url: https://ubuntu.com/download/desktop)

Zet Ubuntu op de VirtualBox met behulpt van deze link: (url: https://brb.nci.nih.gov/seqtools/installUbuntu.html)

Download de Blockchain scraper: 
  `ScraperDBA.py`

Open de terminal en voer volgend commando uit: 
  `sudo apt-get install python3-bs4`

De file zal zich bevinden in downloads, verander je directory met volgend commando: 
  `cd Downloads/`

Om de scraper te laten runnen voer het volgend commando uit: 
  `python3 ScraperDBA.py`

Om de scraper vroegtijdig te laten eindigen voer je  volgend commando uit:
  `Ctrl + c`
  
Na het gebruiken van de scraper zal er een "logfile.txt" aangemaakt zijn in u bestanden, hier kan u de waarden in een ".txt" bestand verder bekijken

Om de Mongo database te installeren voer volgend script uit "bash_script" dat zich bevindt in de "2. mongo" map.

Om Redis te installeren voer volgend script uit "bash_script_installation_redis" dat zich bevindt in de "3. redis" map.

Als laatste istalleer je Docker, hiervoor voer je volgend script uit "bash_script_installation_docker" dat zich bevindt in de "4. docker" map.

Als je vervolgens klaar bent met het downloaden en installeren van vorige applicaties voer je volgende commando's uit in de "cmd".

1 - IN DE CMD NAVIGEER NAAR DE MAP MET SCRAPER FILE
cd 'bestandslocatie'

2 - REDIS, MONGO EN PYTHONCONTAINER OPZETTEN:
docker run -d --name mongocontainer -p 24052:27017 mongo
docker run -d --name rediscontainer -p 2405:6379 redis
docker run -d -t --name pythoncontainer --network=host python


3 - LIJST MET ACTIEVE CONTAINERS OPLIJSTEN
docker ps

4 - ID VAN PYTHON CONTAINER ONTHOUDEN

5 - SCRAPER FILE KOPIEREN NAAR DE PYTHON IMAGE
docker cp docker_scraper.py 'container-ID:/.'
docker cp imports_docker.sh 'container-ID:/.'

Ga nu naar je docker.exe terminal in de python cotainer en voer volgende commandos uit:

1 - TERMINAL OPENEN IN DOCKER VAN DE PYTHON CONTAINER
ls

2 - WEBSCRAPER ACTIVEREN (in de docker.exe terminal van de python container)
imports_docker.sh
python3 docker_scraper.py