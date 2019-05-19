yuokada.github.com
==================

## github pages


     pip3 install  -r requirements.txt
     
## Getting started

    git clone --recurse-submodules git@github.com:yuokada/yuokada.github.com.git gh-pages

## Plus

     pip install watchdog
     watchmedo shell-command --patterns="*.rst" --recursive --wait --command="make html"
