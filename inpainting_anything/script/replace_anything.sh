#!bin/bash

python3 replace_anything.py \
        --input_img  "/workspace/Inpaint-Anything/example/shoes.png"\
        --detect "person" \ 
        --point_labels 5 \
        --text_prompt "shoes" \
        --output_dir ./results/shoes \
        --sam_model_type "vit_h" \
        --sam_ckpt ./weights/sam_vit_h_4b8939.pth \
        --seed 30
