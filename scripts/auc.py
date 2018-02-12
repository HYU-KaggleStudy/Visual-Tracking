import numpy as np

size = lambda obj: obj[2] * obj[3]
xclash = lambda tar, obj: 0 if tar[0] + tar[2] < obj[0] or obj[0] + obj[2] < tar[0] else max(tar[0] + tar[2] - obj[0], obj[0] + obj[2] - tar[0])
yclash = lambda tar, obj: 0 if tar[1] + tar[3] < obj[1] or obj[1] + obj[3] < tar[1] else max(tar[1] + tar[3] - obj[1], obj[3] + obj[3] - tar[1])
clash = lambda tar, obj: xclash(tar, obj) * yclash(tar, obj) / size(obj)
overlap = lambda tar, obj, rat: clash(tar, obj) >= rat
performonce = lambda t, o: sum([overlap(t, o, r) for r in x]) / len(x)
performance = lambda tar, obj, rat: [sum([overlap(t, o, r) for t, o in zip(tar, obj)])/len(tar) for r in rat]
perframe = lambda tar, obj: [sum([overlap(t, o, r) for r in x]) / len(x) for t, o in zip(tar, obj)]
scale = lambda box, ratio=0.01: [box[0] - box[2] * ratio, box[1] - box[3] * ratio, box[2] + box[2] * ratio * 2, box[3] + box[3] * ratio * 2]

def auc(results, truths, x = np.arange(0.001, 1.001, 0.001)):
    return performance(results, truths, x)

def auc_frame(results, truths):
    return perframe(results, truths)