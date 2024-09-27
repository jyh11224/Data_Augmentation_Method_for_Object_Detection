#!bin/bash

lists=$(ls input/labels)

echo ${lists}

for image in input/labels
do
    for list in ${lists}
    do
        cp ${image}/${list} results/inpainting_labels/inpainting_${list}
    done
done
