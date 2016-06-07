#!/usr/bin/python
from train_manage import manage
from sliding_window import slidingw

m = manage()
df = m.loadPatchData()
s = slidingw(640.0,480.0)
litems = []
for l in m.train1Labels:
    for row in df.itertuples():
        if getattr(row,'Image'):
            litems.append((getattr(row,'Image'),getattr(row,l + '_X'),getattr(row,l + '_Y')))

    for item in litems:
        ip = s.generateIntersectingPatches(item[1],item[2],4)
        for i in ip:
            print '{},{},{},{},{},{}'.format( item[0] ,l , i[0], i[1], i[2]/s.patchsize[0],i[3]/s.patchsize[1])

