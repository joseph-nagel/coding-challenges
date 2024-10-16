'''
Non-maximum suppression.

Summary
-------
An implementation of non-maximum suppression (NMS) is provided in this module.
In the context of object detection, this widespread algorithm is typically used
for reducing a high number of bounding boxes that may significantly overlap.

'''

from typing import Union, Tuple, Optional

import numpy as np


def _get_coords(boxes: Union[np.ndarray, list]) -> Tuple[np.ndarray]:
    '''Get bounding box coordinates.'''

    boxes = np.asarray(boxes)

    # ensure appropriate array shape
    if not boxes.ndim in (1, 2):
        raise ValueError('One or two dimensions expected')
    elif boxes.ndim == 1 and boxes.size != 4:
        raise ValueError('Four coordinate elements expected')
    elif boxes.ndim == 2 and boxes.shape[1] != 4:
        raise ValueError('Four elements expected in the coordinate axis')

    # get coordinates (the expected format is (x1, y1, x2, y2))
    x1 = boxes[...,0]
    y1 = boxes[...,1]
    x2 = boxes[...,2]
    y2 = boxes[...,3]

    # check for coordinate violations
    if (x2 < x1).any():
        raise ValueError('Coordinates violate x2 >= x1')
    elif (y2 < y1).any():
        raise ValueError('Coordinates violate y2 >= y1')

    return x1, y1, x2, y2


def compute_area(boxes: Union[np.ndarray, list]) -> np.ndarray:
    '''Compute bounding box areas.'''

    x1, y1, x2, y2 = _get_coords(boxes)

    return np.abs((x2 - x1) * (y2 - y1))


def compute_iou(
    box: Union[np.ndarray, list],
    others: Union[np.ndarray, list],
    eps: float = 1e-16
) -> np.ndarray:
    '''Compute intersections over unions.'''

    # compute intersections
    box_x1, box_y1, box_x2, box_y2 = _get_coords(box)
    others_x1, others_y1, others_x2, others_y2 = _get_coords(others)

    overlap_x1 = np.maximum(box_x1, others_x1) # compute elementwise maxima
    overlap_y1 = np.maximum(box_y1, others_y1)
    overlap_x2 = np.minimum(box_x2, others_x2) # compute elementwise minima
    overlap_y2 = np.minimum(box_y2, others_y2)

    intersection = (overlap_x2 - overlap_x1).clip(min=0) \
                 * (overlap_y2 - overlap_y1).clip(min=0)

    # compute unions
    box_area = compute_area(box)
    others_area = compute_area(others)

    union = box_area + others_area - intersection

    # compute IoUs
    iou = intersection / (union + abs(eps))

    return iou


def nms(
    boxes: Union[np.ndarray, list],
    confs: Union[np.ndarray, list],
    conf_thresh: Optional[float] = None,
    iou_thresh: float = 0.5
) -> list[int]:
    '''Perform non-maximum suppression.'''

    boxes = np.asarray(boxes)
    confs = np.asarray(confs)

    # check lengths
    if len(boxes) != len(confs):
        raise ValueError('Encountered unequal lengths of bounding boxes and confidences')

    # remove low-confidence boxes
    if conf_thresh is not None:
        high_conf_ids = [idx for idx, conf in enumerate(confs) if conf >= conf_thresh]

        boxes = boxes[high_conf_ids]
        confs = confs[high_conf_ids]

    # sort confidences in descending order
    sorted_ids = np.argsort(confs)[::-1]

    # iteratively select indices
    selected_ids = []

    while len(sorted_ids) > 0:

        # get highest-confidence index
        current_idx = sorted_ids[0]

        sorted_ids = sorted_ids[1:]

        selected_ids.append(current_idx.item())

        if len(sorted_ids) > 0:

            # remove high-IoU boxes
            ious = compute_iou(boxes[current_idx], boxes[sorted_ids])
            keep_ids = np.where(ious <= iou_thresh)[0]
            sorted_ids = sorted_ids[keep_ids]

    return selected_ids


if __name__ == '__main__':

    boxes = [
        [1., 1., 2., 3.],
        [1., 1.5, 2., 3.5],
        [0., 1., 2., 3.]
    ]

    confs = [0.9, 0.8, 0.7]

    selected_ids = nms(
        boxes,
        confs,
        iou_thresh=0.5
    )

    print(selected_ids)

