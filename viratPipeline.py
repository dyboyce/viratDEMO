import cv2
import numpy as np


def check_frame(curr_frame, objects_arr, events_arr, image):
    retimage = image
    for x in objects_arr:
        if objects_arr[x][2] == curr_frame:
            retimage = draw_box(
                objects_arr[curr_frame][3], objects_arr[curr_frame][4],
                objects_arr[curr_frame][5], objects_arr[curr_frame][6], retimage)

    for y in events_arr:
        if events_arr[y][5] == curr_frame:
            retimage = draw_box(
                events_arr[curr_frame][6], events_arr[curr_frame][7],
                events_arr[curr_frame][8], events_arr[curr_frame][9], retimage)
    return retimage


def read_in_boxes():
    vid_objects = ()
    vid_events = ()
    return vid_objects, vid_events


def draw_box(s1, s2, x, y, image):
    startpt = (s1, s2)
    endpt = (startpt[0] + x, startpt[1] + y)
    drawn_image = cv2.rectangle(image, startpt, endpt, color, thickness)
    return drawn_image


def write_video():
    pass


# main function part of script

vidcap = cv2.VideoCapture('VIRAT_S_000200_01_000226_000268.mp4')
success, image = vidcap.read()
count = 0
color = (255, 255, 255)
thickness = 5

read_in_boxes()

while success:
    check_frame(count)

    cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', count)
    count += 1
