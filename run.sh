rm run.log
ps -ef | grep "all_in_one.py" | grep -v grep | awk '{print $2}' | xargs kill -s 9
#nohup python -u all_in_one.py   >  ./run.log 2>&1 &
nohup python -u all_in_one2.py   >  ./run.log 2>&1 &




