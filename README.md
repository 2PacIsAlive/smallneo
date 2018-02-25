# How to set up a wallet & connect to blockchain 
# Via neo python package & docker

## 1.  First download python 3.5.4
    Check what version of python you have by typing: 
    
    $ python --version

## 2.  If not then install 3.5.4 via brew, type in terminal:

    $ brew install pyenv
    $ pyenv install 3.5.4

## 3. To export path - Type in terminal:

    $ export PYENV_ROOT=~/.pyenv   
    $ export PATH=$PYENV_ROOT/shims:$PATH
    $ pyenv local 3.5.4

## 4. To see what version of python you are running on type:

    $ python --version

## 5. Next install docker to hook up to the blockchain w/ brew command:

    $ brew install docker
    
    To pull down docker image:
    
    $ docker pull cityofzion/neo-privatenet

## 6. To run :

    $ docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet

## 7.  Next download neo-python package
   
    To download, first clone repo on following git page into any directory of your choosing:
    
    $ git clone https://github.com/CityOfZion/neo-python.git

## 8.  Make sure you have the right python version 

    $ python --version
    
    If not then run 
    
    $ pyenv local 3.5.4

## 9.  To avoid "file not found #include "leveldb/db.h" " error run:

    $ brew install leveldb
    
    Then run:
    
    $ pip install -r requirements.txt

## 10. Next download wallet file from the /data file into your cloned git repo.

## 11. Then execute :

    $ prompt.py -p

## 12. When you see neo> prompt type:

    $ open wallet neo-privnet.wallet
    
    It will ask for a password : password = coz

## 13. Next type:

    $ wallet rebuild
    $ wallet

## 14. Break out into dance cause you're connected to neo blockchain son!

    It should look like 

![Image](/data/wallet.png?raw=true)  

