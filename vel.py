import numpy as np

binWidth = 0.25
oneOverBW = 1./binWidth

cntz = []
for i in range(0,20000):
    try:
        f = open('%i.gro' %i, 'r')
        cntz.append(int(i))
        f.close()
    except:
        break


cntz = np.array(cntz)
dicts = {}
for i in range(0, cntz.max()-1):
    f1 = open('%i.gro' %i, 'r')
    f1.readline()
    nPart = int(f1.readline())
    
    for i in range(nPart):
        line = f1.readline()
        v = float(line.split()[-1])
        y = round(float(line.split()[-5])*oneOverBW,0)/oneOverBW

        if y not in dicts.keys():
            dicts[y] = {}
            dicts[y]['val'] = [v]
        else:
            dicts[y]['val'].append(v)

    f1.close()

jArr = []
for i in dicts.keys():
    dicts[i]['mean'] = np.mean(dicts[i]['val'])
    jArr.append([i, dicts[i]['mean']])
jArr = np.array(jArr)

jArr = jArr[jArr[:, 0].argsort()]

print 'this bit is done'
for i in range(len(jArr)):
    print jArr[i,0], jArr[i,1]
#print np.mean(jArr[:,0]), np.mean(jArr[:,1])


