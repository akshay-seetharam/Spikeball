# Spikeball
Spikeball Scheduling Stuff

## How-To
To run this, first open Terminal (spotlight search).

Run the following code:



`pip3 install python3`⏎

Let me know if you have any problems at this stage.

`pip3 install names`⏎

`git clone https://github.com/akshay-seetharam/Spikeball`⏎

`python3 -m pip install -r requirements.txt`⏎

Permit any confirmation/security messages.

Then:

`cd Spikeball`⏎

`python3 spikeball_groups.py`⏎

It will prompt you to enter the number of teams per group. By default, there are 80 teams in `teams.txt`, so make sure the number of teams per group is a factor of 80.

It will print a schedule below two "------------------" lines

If you have any errors, open an issue, email me, or text if you have my number.

### Customized Teams and Timeslots

In a text editor of your choosing, simply open `teams.txt` or `timeslots.txt` and write the timeslots you prefer. Teams/timeslots should be separated by line breaks. If you want to programmatically generate teams/timeslots, customize one of the `generator.*.py` files and run it with `python3 generator.*.py`⏎. Then run `python3 spikeball_groups.py` ⏎ as usual.

# Colab
Note that the Colab version works slightly differently, though the underlying logic is the same.
https://colab.research.google.com/drive/14SJmi1vpFIDzbXLl4_X3YzuPN2O7_on6#scrollTo=e5be1e6f
