import subprocess
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-q',"--query",type=str)
parser.add_argument( '-l',"--lang",type=str)
parser.add_argument( '-p',"--location",type=str)
parser.add_argument( '-c',"--countrycode",type=str)
parser.add_argument( '-u',"--uulu",type=str)
parser.add_argument( '-nf',"--nfpr",type=str)
parser.add_argument( '-tm',"--tbm",type=str)
parser.add_argument( '-ts',"--tbs",type=str)
parser.add_argument( '-f',"--fillter",type=str)
parser.add_argument( '-s',"--safesearch",type=str)
parser.add_argument( '-st',"--start",type=str)
parser.add_argument( '-n',"--noofresults",type=str)
parser.add_argument( '-R',"--device",type=str)
args = parser.parse_args()
string=args.location
cmd="python check.py -q "+args.query
x = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = x.communicate() 
#print(err)
j=json.loads(out)
pp=j['search results']
for p in pp:
    title=p['title']
    if args.query in str(title):
        val=1
    else:
        val=0
