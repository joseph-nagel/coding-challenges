'''Tests for non-maximum suppression.'''

import pytest

from challenges.non_max_suppression import nms


@pytest.mark.parametrize('boxes, confs, ids_expected', [
    (
        [[1, 1, 2, 3], [1, 1.5, 2, 3.5], [0, 1, 2, 3]],
        [0.9, 0.8, 0.7],
        [0, 2]
    ),
    ([], [], [])
])
def test_correctness(boxes, confs, ids_expected):

    ids_selected = nms(
        boxes,
        confs,
        iou_thresh=0.5
    )

    assert ids_selected == ids_expected

