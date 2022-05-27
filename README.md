# Databases_Advanced

Download VirtualBox: (url: https://www.virtualbox.org/)

Download Ubuntu: (url: https://ubuntu.com/download/desktop)

Zet Ubuntu op de VirtualBox met behulpt van deze link: (url: https://brb.nci.nih.gov/seqtools/installUbuntu.html)

Deel 1: Scraper:

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
  
Na het gebruiken van de scraper zal er een 'logfile.txt' aangemaakt zijn in u bestanden, hier kan u de waarden in een `.txt` bestand verder bekijken

`Deel 2: Mongo`

Om de Mongo database te installeren voer volgend script uit `bash_script` dat zich bevindt in de `2. mongo` map.

`Deel 3: Redis`

Om Redis te installeren voer volgend script uit `bash_script_installation_redis` dat zich bevindt in de `3. redis` map.

`Deel 4: Docker`

Als laatste istalleer je Docker, hiervoor voer je volgend script uit `bash_script_installation_docker` dat zich bevindt in de `4. docker` map.

Als je vervolgens klaar bent met het downloaden en installeren van vorige applicaties voer je volgende commando's uit in het `CMD`.

1 - in het `CMD` navigeer naar de map met de scraper file
`cd bestandslocatie`

2 - het aanmaken van de `Mongo`, `Redis` en `Python` container:

`docker run -d --name mongocontainer -p 24052:27017 mongo`

`docker run -d --name rediscontainer -p 2405:6379 redis`

`docker run -d -t --name pythoncontainer --network=host python`


3 - lijst met alle actieve cotainers

`docker ps`

4 - onthoud het id van de pythoncontainer

5 - kopieer de files naar de python container

`docker cp docker_scraper.py container-ID:/.`

`docker cp imports_docker.sh container-ID:/.`

Ga nu naar je `docker.exe` terminal in de `python cotainer` en voer volgende commando's uit:

1 - open de docker terminal van de python conatainer

`ls`

2 - activeer de volgende files (in de `docker.exe` terminal van de python container)

`sh imports_docker.sh`

`python3 docker_scraper.py`
