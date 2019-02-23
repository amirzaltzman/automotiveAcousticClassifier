# coding: utf-8

import csv
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import time

import parameters

def wav_to_image_to_file(path_in, path_out, label, index):
    y, sr  = librosa.load(path_in)
    #y, sr = librosa.load("audio/fold" + str(row[5]) + "/" + str(row[0]))

    # Let's make and display a mel-scaled power (energy-squared) spectrogram
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=512)

    # Convert to log scale (dB). We'll use the peak power as reference.
    log_S = librosa.amplitude_to_db(S, ref=np.max)

    # Make a new figure
    fig = plt.figure(figsize=(12, 4))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    # Display the spectrogram on a mel scale
    # sample rate and hop length parameters are used to render the time axis
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')

    # Make the figure layout compact

    #plt.show()
    png_name = '%s\%s_%s.png' %(path_out, label, index)
    plt.savefig(png_name)
    jpg_name = '%s\%s_%s.jpg' % (path_out, label, index)
    png2jpg(png_name,jpg_name)

    plt.close()

def parse_images_from_folder():
    paths = os.listdir(parameters.WAV_DATA_TRAIN) #TODO - fix so that is will get directories only
    for label in paths:
        print("label = %s\n-----------------------'\n" %label)

        samples_counter = 1

        label_wav_path = '%s\%s' %(parameters.WAV_DATA_TRAIN, label) #TODO - fix so that is will get wavs only
        wav_names = os.listdir(label_wav_path)
        label_image_path = '%s\%s' %(parameters.IMAGES_DATA_TRAIN, label)
        if not os.path.exists(label_image_path):
            os.makedirs(label_image_path)

        for wav_name in wav_names:
            if (samples_counter < parameters.SAMPLES_PER_CLASS):
                print("label: %s, iteration: %d, name: %s" %(label, samples_counter, wav_name))
                wav_to_image_to_file(label_wav_path + '\\' + wav_name, label_image_path, label, samples_counter)
                samples_counter = samples_counter + 1


def png2jpg(png_path,jpg_path):
    from PIL import Image

    im = Image.open(png_path)
    rgb_im = im.convert('RGB')
    rgb_im.save(jpg_path)

if __name__ == "__main__":
    parse_images_from_folder()




