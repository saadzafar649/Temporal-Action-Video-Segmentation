# Temporal-Action-Video-Segmentation


Create a folder and add videos in it
#Input

To run
`
python Asformer/main.py --action=train --dataset=50salads/gtea/breakfast --split=1/2/3/4/5
`

To train
`
python main.py --action=train --dataset=50salads --split=1
`


To predict
`
python main.py --action=predict --dataset=50salads --split=1
`




To test
`
python main.py --action=test --dataset=50salads --split=1
`


To eval
`
python eval.py --dataset=50salads --split=0
`


All commands
`
python main.py --action=train --dataset=50salads --split=1 & python main.py --action=predict --dataset=50salads --split=1 & python eval.py --dataset=50salads --split=0
`
