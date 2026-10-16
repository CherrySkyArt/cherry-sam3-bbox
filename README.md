# cherry-sam3-bbox

ComfyUI custom node: **SAM3 Segment (Cherry)** (`CherrySAM3Segment`).

Text-prompted SAM3 segmentation that outputs the cut-out image, mask, mask image, and bounding boxes
(single bbox in `Merged` mode, a list of bboxes in `Separate` mode).

Split out of `cherry-nodez`. Node code adapted from
[1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG/blob/112fd6141d07663d5e4a35d66d269542b58f4438/py/AILab_SAM3Segment.py)
(~April 2026); `models/sam3` is the SAM3 package copied from that repo.

## Install

```
cd ComfyUI/custom_nodes
git clone <this repo> cherry-sam3-bbox
pip install -r cherry-sam3-bbox/requirements.txt
```

The checkpoint (`sam3.pt`) is downloaded on first run into `ComfyUI/models/sam3/`.
