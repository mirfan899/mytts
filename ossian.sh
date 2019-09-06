#!/usr/bin/env bash
FILE=$1
TRANSCRIPT=$2
sudo su
export OSSIAN=/home/virtuoso_irfan/Ossian
export OSSIAN_LANG=cn
export DATA_NAME=toy_cn_corpus
export RECIPE=naive_01_nn

cd $OSSIAN
source $OSSIAN/.mytts/bin/activate

MYTTS_MEDIA=/home/virtuoso_irfan/mytts/media

# write file
touch $MYTTS_MEDIA/txt/${FILE}.txt
echo $TRANSCRIPT > $MYTTS_MEDIA/txt/${FILE}.txt

python $OSSIAN/scripts/speak.py -l $OSSIAN_LANG -s $DATA_NAME -o $MYTTS_MEDIA/wav/${FILE}.wav $RECIPE
$MYTTS_MEDIA/txt/${FILE}.txt