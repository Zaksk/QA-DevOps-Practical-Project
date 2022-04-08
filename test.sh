#!/bin/bash
declare -a directories=("service-1" "service-2" "service-3" "service-4")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3.8-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r test_requirements.txt
  python3 -m pytest --cov=application --cov-report term-missing --cov-report=html -p no:warnings
  deactivate
  cd ..
done