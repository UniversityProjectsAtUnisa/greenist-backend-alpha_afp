if [ $# = 1 ]; then
    ssh -t pi@192.168.1.149 'cd Greenist_backend; git fetch --all; git reset --hard origin/master; python3 -m pip install -r requirements.txt; sudo systemctl restart flask.service;'
else
    ssh -t pi@greenist.ddns.net -p 2022 "cd Greenist_backend; git fetch --all; git reset --hard origin/master; python3 -m pip install -r requirements.txt; sudo systemctl restart flask.service"
fi
