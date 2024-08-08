import numpy as np
import matplotlib.pyplot as plt
X1 = np.load('..\data\data1\X_data_subject_1.2.npy')
X2 = np.load('..\data\data1\X_data_subject_2.2.npy')
X3 = np.load('..\data\data1\X_data_subject_3.2.npy')
Y1 = np.load('..\data\data1\y_labels_subject_1.2.npy')
Y2 = np.load('..\data\data1\y_labels_subject_2.2.npy')
Y3 = np.load('..\data\data1\y_labels_subject_3.2.npy')


t = np.arange(0, 1, 0.002)
# signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
fft_result=np.zeros((250,))
freqs = np.fft.fftfreq(len(t), t[1] - t[0])
f_idx=10
for k in range(8):
    signal=X1[0+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]
    signal=X1[1+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]
    signal=X2[0+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]
    signal=X2[1+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]
    signal=X3[0+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]
    signal=X3[1+f_idx,k,:]
    fft_result += np.abs(np.fft.fft(signal))[:len(freqs)//2]


# # 绘制原始信号
# plt.subplot(2, 1, 1)
# plt.plot(t, signal)
# plt.title('Original Signal')

# # 绘制频谱
# plt.subplot(2, 1, 2)

plt.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(freqs)//2])
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(5, 20)
plt.grid(True)
plt.tight_layout()
plt.show()