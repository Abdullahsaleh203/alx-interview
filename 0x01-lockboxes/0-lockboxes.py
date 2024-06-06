#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes) # Get the number of boxes
    unlocked_boxes = [0] # Initialize a list with the first box (index 0)
    for box_num, box in enumerate(boxes): # Loop through each box and its index
        for key in box: # Loop through each key in the current box
            # Check if the key can open a new box that hasn't been unlocked yet by
            #  checking if the key is less than the total number of boxes (n),
            # if the key has not been added to the list of unlocked boxes (unlocked_boxes),
            # and if the key does not unlock the current box (i.e., the box the key is from)
            if key < n and key not in unlocked_boxes and key != box_num:
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == n
