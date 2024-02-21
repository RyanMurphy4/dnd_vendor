import cv2 as cv
import numpy as np


def find_item(game_screenshot, item, threshold=0.5):

    # img_gray = cv.cvtColor(item, cv.COLOR_BGR2GRAY)
    # template_gray = cv.cvtColor(game_screenshot, cv.COLOR_BGR2GRAY)
    
    img_gray = item
    template_gray = game_screenshot

    METHOD = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(template_gray, img_gray, METHOD)
    bbw = item.shape[1]
    bbh = item.shape[0]


    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for location in locations:
        rect = [int(location[0]), int(location[1]), bbw, bbh]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

    points = []

    if len(rectangles):
        line_color = (0, 0, 255)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x, center_y))
            # self.public_points.append((center_x, center_y))

            top_left = (x, y)
            bottom_right = (x+h, y+w)


            cv.rectangle(game_screenshot, top_left, bottom_right, color=line_color, lineType=line_type,
                            thickness=2)
    return points