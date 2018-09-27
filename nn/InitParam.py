# -*- coding: utf-8 -*-

import numpy as np


def InitParam(OldWeights, num=None, newWeights=None, upper=None, lower=None):
    """
    生成随机的向量，并且和原来的向量拼接
    :param OldWeights:
    :param num:     新向量的长度
    :param newWeights:
    :param upper:
    :param lower:
    :return:旧的向量+新的向量，新向量的坐标(range 对象)
    """
    oldlen = len(OldWeights)
    if newWeights is not None:
        newWeights = np.array(newWeights)
        num = len(newWeights)
        OldWeights = np.concatenate((OldWeights, newWeights.reshape(-1)))

    else:
        if upper is None:
            upper = -.002
            lower = 0.002
        tmpWeights = np.random.uniform(lower, upper, num)
        OldWeights = np.concatenate((OldWeights, tmpWeights.reshape(-1)))
    return OldWeights, range(oldlen, oldlen + num)


if __name__ == '__main__':
    Weights = []
    Weights, idx1 = InitParam(Weights, 10)
    Weights, idx2 = InitParam(Weights, 5)
    Weights, idx3 = InitParam(Weights, newWeights=[1, 2, 3])
    # print idx1
    # print idx2
    # print Weights
