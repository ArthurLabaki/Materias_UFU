from skimage.filters import threshold_triangle, threshold_sauvola, threshold_niblack, threshold_li
from cv2 import VideoCapture, VideoWriter
from skimage import img_as_ubyte
from tqdm import tqdm
from time import time
from statistics import mean
from scipy.stats import entropy
from sewar import ssim, vifp, uqi
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import math

def histogram(array):
    hist = {}
    for value in array:
        if value in hist:
            hist[value] += 1
        else:
            hist[value] = 1
    return hist

def entropy(array):
	hist = histogram(array)
	length = len(array)
	entropy = 0
	for freq in hist.values():
		p = freq / length
		entropy += p * math.log2(p)
	return -entropy

# Generate videos, extract metrics and save comparison graphics from thresholds list
def createPreProcessMetrics():

    thresholds = [threshold_triangle, threshold_sauvola, threshold_niblack, threshold_li, 25]
    thf_labels = []

    thf_timestamps_list = []
    thf_entropies_list = []
    simSsimValues_list = []
    simVipfValues_list = []
    qualUqiValues_list = []
   
    for th in thresholds:

        thf_timestamps_ms = None
        thf_entropies = None
        simSsimValues = None
        simVipfValues = None
        qualUqiValues = None

        if type(th) != int:
            thf_labels.append(th.__name__.replace('threshold','Th'))
            thf_timestamps_ms, thf_entropies, simSsimValues, simVipfValues, qualUqiValues = createVideosRetTimestamp('neondrl.mp4', th, th.__name__)
        else:
            thf_labels.append(str(th))
            thf_timestamps_ms, thf_entropies, simSsimValues, simVipfValues, qualUqiValues = createVideosRetTimestamp('neondrl.mp4', th, str(th))

        thf_timestamps_list.append(thf_timestamps_ms)
        thf_entropies_list.append(thf_entropies)
        simSsimValues_list.append(simSsimValues)
        simVipfValues_list.append(simVipfValues)
        qualUqiValues_list.append(qualUqiValues)
    
    createComparison(thf_labels, thf_timestamps_list, 2, 'Tempo(MS)', 'Tempo gasto por diferentes técnicas de pré-processamento', 'Timestamp.png')
    createComparison(thf_labels, thf_entropies_list, 3, 'Valor entropia', 'Valores de entropias dos frames gerados por cada threshold', 'Entropies.png')
    createComparison(thf_labels, simSsimValues_list, 3, 'Valor de similaridade SSIM', 'Valores de similaridade SSIMs dos frames gerados por cada threshold', 'SSIMs.png')
    createComparison(thf_labels, simVipfValues_list, 3, 'Valor de similaridade VIPF', 'Valores de similaridade VIPFs dos frames gerados por cada threshold', 'VIPFs.png')
    createComparison(thf_labels, qualUqiValues_list, 3, 'Valor de qualidade UQI', 'Valores de qualidade UQIs dos frames gerados por cada threshold', 'UQIs.png')

def createComparison(eLabels, eLists, roundValue, yLabel, title, saveFName):
    
    minList = []
    meanList = []
    maxList = []

    for eList in eLists:
        minList.append(round(min(eList), roundValue))
        meanList.append(round(mean(eList), roundValue))
        maxList.append(round(max(eList), roundValue))
    
    x = np.arange(len(eLabels))
    width = 0.90

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/3, minList, width/3, label='Mínimo')
    rects2 = ax.bar(x, meanList, width/3, label='Média')
    rects3 = ax.bar(x + width/3, maxList, width/3, label='Máximo')

    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks(x, eLabels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.savefig('./comparativos/' + saveFName, dpi=250)

# Creates 5 videos using preprocessing filters and return threshold metrics
def createVideosRetTimestamp(videoInputName, thresholdFunction, videoOutputDict, w = 1920, h = 1080):

    # create save path if not exists
    if not os.path.exists('./media'):
        os.makedirs('./media')

    if not os.path.exists('./media/' + videoOutputDict):
        os.makedirs('./media/' + videoOutputDict)

    cap = VideoCapture(videoInputName)
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h1, w1 = gray_frame.shape

    cropped_bw_frame = gray_frame[int(7 * (h / 13.0)):int(h - (h / 5)), int(w / 5):int(w - (w / 5))]
    h2, w2 = cropped_bw_frame.shape

    # threshold
    if type(thresholdFunction) != int:
        threshold_frame = thresholdFunction(cropped_bw_frame)
        binary_frame = cropped_bw_frame > threshold_frame
    
    # int
    else:
        binary_frame = cropped_bw_frame > thresholdFunction

    binary_frame = img_as_ubyte(binary_frame)
    h3, w3 = binary_frame.shape

    resized_bw_frame = cv2.resize(binary_frame, (int(160), int(90)), interpolation=cv2.INTER_AREA)
    h4, w4 = resized_bw_frame.shape

    bw_frame = cv2.bitwise_not(resized_bw_frame)
    h5, w5 = bw_frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out1 = VideoWriter('./media/' + videoOutputDict + '/1_gray.mp4', fourcc, 60.0, (w1, h1))
    out2 = VideoWriter('./media/' + videoOutputDict + '/2_cropped.mp4', fourcc, 60.0, (w2, h2))
    out3 = VideoWriter('./media/' + videoOutputDict + '/3_binary.mp4', fourcc, 60.0, (w3, h3))
    out4 = VideoWriter('./media/' + videoOutputDict + '/4_resized.mp4', fourcc, 60.0, (w4, h4))
    out5 = VideoWriter('./media/' + videoOutputDict + '/5_difference.mp4', fourcc, 60.0, (w5, h5))
    
    bw = list()
    thf_timestamps_ms = []
    thf_entropies = []
    simSsimValues = []
    simVipfValues = []
    qualUqiValues = []

    for i in tqdm(range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))):
        ret, frame = cap.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out1.write(cv2.cvtColor(gray_frame, cv2.COLOR_BGR2RGB))

            cropped_bw_frame = gray_frame[int(7 * (h / 13.0)):int(h - (h / 5)), int(w / 5):int(w - (w / 5))]
            out2.write(cv2.cvtColor(cropped_bw_frame, cv2.COLOR_BGR2RGB))
            
            binary_frame = None

            ### threshold ###
            # calculate timestamp
            start_thf_time = time()*1000
            if type(thresholdFunction) != int:
                threshold_frame = thresholdFunction(cropped_bw_frame)
                binary_frame = cropped_bw_frame > threshold_frame

            # int
            else:
                binary_frame = cropped_bw_frame > thresholdFunction
            end_thf_time = time()*1000
            
            # calculate entropy
            pk = np.array(binary_frame).flatten()
            thf_entropies.append(entropy(pk))

            # calculate ssim, vifp and uqi from gray frame as original image and binary(threshold applied) as distortion image
            simSsimValues.append(ssim(cropped_bw_frame, binary_frame)[0])
            simVipfValues.append(vifp(cropped_bw_frame, binary_frame))
            qualUqiValues.append(uqi(cropped_bw_frame, binary_frame))

            thf_timestamps_ms.append(end_thf_time-start_thf_time)
            
            binary_frame = img_as_ubyte(binary_frame)
            out3.write(cv2.cvtColor(binary_frame, cv2.COLOR_BGR2RGB))

            resized_bw_frame = cv2.resize(binary_frame, (int(160), int(90)), interpolation=cv2.INTER_AREA)
            bw_frame = cv2.bitwise_not(resized_bw_frame)
            bw.append(bw_frame)
            out4.write(cv2.cvtColor(bw_frame, cv2.COLOR_BGR2RGB))

            if i > 20:
                difference = cv2.bitwise_not(bw[i-20] - bw_frame)
                out5.write(cv2.cvtColor(difference, cv2.COLOR_BGR2RGB))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out1.release()
    out2.release()
    out3.release()
    out4.release()
    out5.release()

    return thf_timestamps_ms, thf_entropies, simSsimValues, simVipfValues, qualUqiValues

createPreProcessMetrics()