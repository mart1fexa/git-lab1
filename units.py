def pcs_to_boxes(qty, box=50):
    return -(-qty // box)


def boxes_to_pcs(boxes, box=50):
    return boxes * box
