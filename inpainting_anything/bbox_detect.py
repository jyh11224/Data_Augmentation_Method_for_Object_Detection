import warnings
import argparse
import sys
import numpy as np
import shutil
import os
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
from lang_sam import LangSAM



def setup_args(parser):
    parser.add_argument(
        "--input_img", type=str, required=True,
        help="Path to a single input img",
    )
    parser.add_argument(
        "--text_prompt", type=str, required=True,
        help="Text prompt",
    )
    
if __name__ == "__main__":
    # Suppress warning messages
    warnings.filterwarnings("ignore")

    # org_path = "/workspace/Inpaint-Anything/results/desert_images_mask"
    # dst_path = "/workspace/Inpaint-Anything/results/desert_images_final"

    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])
    image_pil = Image.open(args.input_img).convert("RGB")

    model = LangSAM()
    masks, boxes, phrases, logits = model.predict(image_pil, args.text_prompt)
    boxes = boxes.tolist()
    # print(phrases)

    # file_name = args.input_img[55:]
    # if (len(phrases) > 0):
    #     shutil.copy(os.path.join(org_path, file_name), os.path.join(dst_path, file_name))
    

#workspace/Inpaint-Anything/results/desert_images_mask/20231128_162639_VIS_H264-5_inpainting_mask_2.png
