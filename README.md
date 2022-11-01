usage: python script.py

script.py should be in the same location as the 'csv' directory.
The 'csv' directory should contain a .csv file for each lecture.

To get the .csv files, open the google forum for each lecture,
select "responses", then "Download Responses (.csv)". You may
need to unzip the files.

script.py will sort the surveys based on the timestamp of the
first response (as the names for each survey may vary). This
order will be printed to the terminal, make sure it is correct.

out.csv will then be generated. For each student, it includes a
grade for each lecture (0-1) and a total score.

csv/dummy.py was used to generate the dummy csv files. You can
ignore this file.
