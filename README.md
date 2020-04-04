# m3u-parser
A neat little command line utility that downloads a remote M3U URL, parses it for your channels and saves a clean playlist

Do you use IPTV or any such service? If you're like me, your provider perhaps furnishes you with an M3U a mile long, which makes it difficult to sift through the content you really want on your media player

## Installation:
 * Just clone this repository into your desired directory

## Config:
 * In the config/ directory, edit the sample config.yaml as follows:

 ** REMOTE_URL:
      "<<enter your remote M3U URL, which you will have received from your provider. These are in a standard format"
 ** FILTER_FILE:
      "config/<<drop a text file name in here, where you have stored your list of preferred categories. One line per category, exactly as the name appears in the M3U>>"
 ** INPUT_FILE:
      "<<enter a file name the script will use e.g. raw.m3u>>"
 ** OUTPUT_FILE:
      "<<enter a file name where the resulting clean m3u will be written in the output dir e.g. output/out.m3u>>"
 ** USE_PROGRESS_BAR:
      True
 
 * For the last item, USE_PROGRASS_BAR, as the name suggests this is a neat progress bar for large M3Us. However it might not work on Linux because of character code differences between OSs. If so, change to False

## First run:
 1. Remember to update your config.yaml as described above
 2. At this point, you may not know exactly which categories you are most interested in. SO just leave the config/megafaves.txt file as it is for now and move to the next step 
 3. Run using python main.py from the directory you used to clone the repository
 4. An output file will appear in the root project directory (default name is all_grp.txt). This is a list of EVERY catorey in your M3U. Go ahead and select the categories you like in this file and copy them into the config/megafaves.txt file. 
 5. Run again as per 3. Hey presto! You will find a nicely modifed (default: out.m3u) in the output/ directory. Go ahead and link your media player to that file (making sure to specify that your M3U is now a local file, rather than remote.
 
You'll now have a clean, short playlist, focussed on the content you want to see

