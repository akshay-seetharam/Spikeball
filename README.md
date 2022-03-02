# Spikeball
Spikeball Scheduling Stuff

## How-To
To run this, first open Terminal (spotlight search).

Run the following code:

`git clone https://github.com/akshay-seetharam/Spikeball`⏎

`python3 -m pip install -r requirements.txt`\342\217\216
Permit any confirmation/security messages.

Then:

`cd Spikeball`⏎

`python3 spikeball_groups.py`⏎

If you have any errors, open an issue, email me, or text if you have my number.

### Customized Teams and Timeslots

In a text editor of your choosing, simply open `teams.txt` or `timeslots.txt` and write the timeslots you prefer. Teams/timeslots should be separated by line breaks. If you want to programmatically generate teams/timeslots, customize one of the `generator.*.py` files and run it with `python3 generator.*.py`. Then run `python3 spikeball_groups.py` ⏎ as usual.
