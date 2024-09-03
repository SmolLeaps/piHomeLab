# piHomeLab
LLM-powered git ops tool running on raspberry pi 4 model B

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git gcc python3 python3-pip
pip3 install transformers torch
pip3 install requests
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker pi  # Add 'pi' user to Docker group
```

run 
```
python3 main.py
```
