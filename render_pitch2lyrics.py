import matplotlib.pyplot as plt
import numpy as np
from lyric_parser import Lyric as l

plt.rcParams['font.family'] = ['Arial Unicode MS']

if __name__ == "__main__":

    result = np.loadtxt("./dye/result.txt")
    postgram = np.loadtxt("./dye/postgram.txt")
    lyric_path = "/Users/LEE/PycharmProjects/devocal_v2/test/64335_擊敗人/64335_擊敗人.lyric"

    a = l(lyric_path)
    time_stamp_ori = []
    text_ = []

    for seq in a.seq:
        time_stamp_ori.append(seq[0] / 1000)
        text_.append(seq[2])

    time_stamp = np.array(time_stamp_ori)
    print(".")

    start_sec = 34
    stop_sec = 49

    myth = 50

    # result (sample = 20ms)
    start = int(start_sec * myth) - 1
    stop = int(stop_sec * myth) + 1

    plt.subplot(211)
    plt.plot(result[start:stop, 0], result[start:stop, 1])
    plt.ylim((100, 250))

    x = -1
    i = 0
    for t in time_stamp:
        if t > stop_sec:
            x = i - 1
            break
        i = i + 1

    last_text = text_[i]
    last_time_stamp = time_stamp[i]
    l_txt = text_[:i]
    l_time = time_stamp[:i]
    plt.xticks(l_time, l_txt)
    # plt.show()

    plt.subplot(212)
    plt.imshow(postgram, aspect='auto')
    P_start = start
    plt.imshow(postgram[:, start:stop], aspect='auto', origin="lower")
    plt.xticks(l_time * myth - start, l_txt)
    plt.show()

    print(".")
