[song, fs] = audioread('[org][jaz_blu]1040__3.wav');
song = song(1:fs*3);
%spectrogram(song, windowSize, windowOverlap, freqRange, fs, 'yaxis');

%Larger Window Size value increases frequency resolution
%Smaller Window Size value increases time resolution
%Specify a Frequency Range to be calculated for using the Goertzel function
%Specify which axis to put frequency

% Window duration (in seconds):
dur = 0.1;
% Spectrogram settings (in samples):
winSize = round(fs*dur);
overlap = round(winSize/2);
fftSize = winSize;
% Plot the spectrogram:
[S,F,T] = spectrogram(song,winSize,overlap,fftSize,fs,'yaxis');

[coeffs,delta,deltaDelta,loc] = mfcc(song,fs);
