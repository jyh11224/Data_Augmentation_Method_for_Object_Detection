#!bin/bash

for image in input/train/desert_images/*.jpg
do
    python3 replace_anything.py \
        --input_img ${image} \
        --coords_type click \
        --point_coords 550 350 \
        --point_labels 2 \
        --text_prompt "desert" \
        --output_dir ./results/desert_images \
        --sam_model_type "vit_h" \
        --sam_ckpt ./weights/sam_vit_h_4b8939.pth \
        --seed 30
done
