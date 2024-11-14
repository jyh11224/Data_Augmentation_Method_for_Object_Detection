#!bin/bash

python3 fill_anything.py \
    --input_img /workspace/Inpaint-Anything/example/shoes.png \
    --point_labels 1 \
    --text_prompt "The image shows a glossy black formal shoe with bold red laces. The shoe features a textured pattern similar to crocodile leather and has a light tan sole. The overall look is stylish and modern." \
    --dilate_kernel_size 30 \
    --output_dir ./results/fill/shoes \
    --sam_model_type "vit_h" \
    --sam_ckpt ./weights/sam_vit_h_4b8939.pth
