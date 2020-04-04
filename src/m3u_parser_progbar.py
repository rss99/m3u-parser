import sys
import time
from urllib import request
import math
import yaml

def get_config(item):

    #config_file = Path("../config/") / "config.yaml"
    config_file = "config/config.yaml"

    try:
        with open(config_file, 'r') as stream:
                conf = yaml.safe_load(stream)
                return conf.get(item)
    except FileNotFoundError as fnf:
        sys.exit("Check your config.yaml file. See docs for settings...")
    except yaml.YAMLError as exc:
        sys.exit("Invalid configuration, please see docs...")

def getProgress(iterator, total, progress_points=125, gaps=1):
    if (iterator % gaps == 0):
        pct = "{:.2f}%".format(round((iterator / total), 4) * 100)
        bar = ['=' * math.ceil((iterator / total) * progress_points) + '>>' +
               '.' * (math.ceil((1 - (iterator / total)) * progress_points))]

        print("", end='\r' + str(bar) + ' ' + pct)

def retrieveM3U():

    REMOTE_URL = get_config('REMOTE_URL')
    FILTER_FILE = get_config('FILTER_FILE')
    INPUT_FILE = get_config('INPUT_FILE')
    OUTPUT_FILE = get_config('OUTPUT_FILE')
    USE_PB = get_config('USE_PROGRESS_BAR')

    try:
        request.urlretrieve(REMOTE_URL, INPUT_FILE)
    except ValueError as e:
        sys.exit("Invalid remote M3U URL supplied, please check your config.yaml...")

    start_time = time.time()

    wanted = open(FILTER_FILE, "r").readlines()

    lines = []
    all_pl = []

    out_file = open(OUTPUT_FILE, 'w')
    out_file.writelines("#EXTM3U\n")
    out_file.close()

    iterator = 1

    with open(INPUT_FILE) as f:
        count = len(f.read().split('\n')) - 1

    count *= len(wanted)

    for fave in wanted:
        with open(INPUT_FILE, 'r') as infile:
            with open(OUTPUT_FILE, 'a') as outfile:
                for line in infile:

                    if(USE_PB): getProgress(iterator, count)

                    if ("#EXTM3U" in line):
                        continue
                    else:
                        lines.append(line)

                    if len(lines) >= 2:

                        grp = lines[0].split('group-title=\"')[1].split('\"')

                        if(grp is not None and grp[0] in fave):
                            outfile.writelines(lines)
                        elif (grp is not None and grp[0] not in all_pl):
                            all_pl.append(grp[0])

                        lines = []

                    iterator += 1

    print('\n\n[M3UP]: Produced compressed file of ' + str(len(open(OUTPUT_FILE,'r').readlines())))
    print("[M3UP]: Process took %s seconds" % "{:.2f}".format(time.time() - start_time))

    all_pl.sort()

    with open('output/all_grp.txt', 'w') as f:
        for item in all_pl:
            f.write("%s\n" % item)
