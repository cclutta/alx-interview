#!/usr/bin/python3
"""Lockboxes module.
Contains the function canUnlockAll
"""


def canUnlockAll(boxes):
    """ Returns whether all boxes can be unlocked. """
    box_len = len(boxes)

    if box_len > 0:
        keys = boxes[0]
        boxes[0] = [-1]
        while keys:
            new_keys = []
            for key in keys:
                if key < box_len:
                    if boxes[key] != [-1]:
                        new_keys += boxes[key]
                        boxes[key] = [-1]
            keys = new_keys

        return boxes.count([-1]) == box_len

    return False
        
