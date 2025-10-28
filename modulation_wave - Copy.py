import numpy as np
import matplotlib.pyplot as plt

def save_plot_with_labels(t, signal, filename, ylabel, title, figsize=(8,3)):
    plt.figure(figsize=figsize)
    plt.plot(t, signal, color='black')
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

Am, Ac, fm, fc, ka = 2.6, 5.3, 564, 5640, 0.5
fs_am = int(20 * fc)
t = np.arange(0, 2/fm, 1/fs_am)
m_t = Am * np.cos(2 * np.pi * fm * t)
c_t = Ac * np.cos(2 * np.pi * fc * t)
am_t = Ac * (1 + ka * m_t) * np.cos(2 * np.pi * fc * t)
save_plot_with_labels(t, m_t, "am_message.png", "Amplitude", "AM Message Signal")
save_plot_with_labels(t, c_t, "am_carrier.png", "Amplitude", "AM Carrier Signal")
save_plot_with_labels(t, am_t, "am_modulated.png", "Amplitude", "AM Modulated Wave")

Am, Ac, fm, fc, B, fs = 2.9, 5.8, 594, 5940, 4.3, 59400
t = np.arange(0, 2/fm, 1/fs)
m = Am * np.cos(2 * np.pi * fm * t)
c = Ac * np.cos(2 * np.pi * fc * t)
Efm = Ac * np.cos(2 * np.pi * fc * t + B * np.sin(2 * np.pi * fm * t))
save_plot_with_labels(t, m, "fm_message.png", "Amplitude", "FM Message Signal")
save_plot_with_labels(t, c, "fm_carrier.png", "Amplitude", "FM Carrier Signal")
save_plot_with_labels(t, Efm, "fm_modulated.png", "Amplitude", "FM Modulated Wave")

Am, Ac, fm, fc, fs = 2.7, 5.4, 574, 5740, 57400
t = np.arange(0, 2/fm, 1/fs)
m = Am * np.cos(2 * np.pi * fm * t)
c = Ac * np.cos(2 * np.pi * fc * t)
s1 = (Ac + m) * np.cos(2 * np.pi * fc * t)
s2 = (Ac - m) * np.cos(2 * np.pi * fc * t)
dsbsc = s1 - s2
save_plot_with_labels(t, m, "dsbsc_message.png", "Amplitude", "DSBSC Message Signal")
save_plot_with_labels(t, c, "dsbsc_carrier.png", "Amplitude", "DSBSC Carrier Signal")
save_plot_with_labels(t, dsbsc, "dsbsc_modulated.png", "Amplitude", "DSBSC Modulated Wave")

Am, Ac, fm, fc, fs = 2.8, 5.6, 584, 5840, 58400
t = np.arange(0, 2/fm, 1/fs)
m1 = Am * np.cos(2 * np.pi * fm * t)
c1 = Ac * np.cos(2 * np.pi * fc * t)
s1 = c1 * m1
m2 = Am * np.cos(1.57 - (2 * np.pi * fm * t))
c2 = Ac * np.cos(1.57 - (2 * np.pi * fc * t))
s2 = c2 * m2
lsb = s1 + s2
usb = s1 - s2
save_plot_with_labels(t, m1, "ssbsc_message.png", "Amplitude", "SSBSC Message Signal")
save_plot_with_labels(t, c1, "ssbsc_carrier.png", "Amplitude", "SSBSC Carrier Signal")
save_plot_with_labels(t, lsb, "ssbsc_lsb.png", "Amplitude", "SSBSC LSB Signal")
save_plot_with_labels(t, usb, "ssbsc_usb.png", "Amplitude", "SSBSC USB Signal")
