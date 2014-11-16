#!/usr/bin/python
# encoding: utf-8

import sys
import corpse_data

from workflow import Workflow

log = None

 
def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`

    # Your imports here if you want to catch import errors
    
    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    if len(wf.args):
        query = wf.args[0]
    else:
        query = ""
    i = getItemPos(query)


    # Add an item to Alfred feedback
    if corpse_data.corpse_list[i][1] != "":
        wf.add_item('Nutrition', corpse_data.corpse_list[i][1], icon="img/nutrition_icon.png")
    else:
        wf.add_item("<"+query+">", icon="img/nethack_icon.png")
    if corpse_data.corpse_list[i][2] != "":
        wf.add_item('Inital effects', corpse_data.corpse_list[i][2], icon="img/ieffect_icon.png")
    if corpse_data.corpse_list[i][3] != "":
        wf.add_item('Final effects', corpse_data.corpse_list[i][2], icon="img/feffect_icon.png")
    if corpse_data.corpse_list[i][4] != "":
        wf.add_item('Intrinsics', corpse_data.corpse_list[i][4], icon="img/intrinsics_icon.png")

    # Send output to Alfred
    wf.send_feedback()

def getItemPos(query):
    for index in range(0,len(corpse_data.corpse_list)):
        # TODO fuzzy matching
        if query.lower() == corpse_data.corpse_list[index][0].lower():
            return index;
    return 0

if __name__ == '__main__':
    wf = Workflow()
    # Assign Workflow logger to a global variable, so all module
    # functions can access it without having to pass the Workflow
    # instance around
    log = wf.logger
    sys.exit(wf.run(main))