#!/usr/bin/env sh

if [ $1 == "Transformer-Annotated" ]; then
    req_suffix="TransfAnnotated"
    venv="venv-${req_suffix}"
else
    exit -1
fi

app="./py"
req="./req/requirements-${req_suffix}.txt"

python -m ensurepip
pip install --upgrade pip setuptools virtualenv
pip install -r requirements.txt
virtualenv -p python3 $venv --no-site-packages
source $venv/bin/activate

#TODO
#install req into $venv 
#python -m pip install -r $req
