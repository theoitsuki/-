import librosa
import numpy as np
import matplotlib.pyplot as plt

def get_active_segments(y, top_db=20):
    active_intervals = librosa.effects.split(y, top_db=top_db)
    active_segments = []
    for start, end in active_intervals:
        active_segments.append(y[start:end])
    return active_segments

def get_speaking_time(y):
    active_intervals = librosa.effects.split(y, top_db=20)
    speaking_time = (active_intervals[-1][1] - active_intervals[0][0]) / 22050
    return speaking_time

def get_silent_time(y):
    active_intervals = librosa.effects.split(y, top_db=20)
    silents_time = []
    for i in range(1, len(active_intervals)):
        silents_time.append((active_intervals[i][0] - active_intervals[i-1][1]) / 22050)
    silents_time_sum = sum(silents_time)
    silents_time_std = np.std(silents_time)
    return silents_time_sum, silents_time_std

def get_db(y):
    rms = librosa.feature.rms(y=y)
    # db = librosa.amplitude_to_db(rms)
    db = np.mean(rms)
    return db

def get_db_features(ys):
    db_segments = []
    for y in ys:
        frames = librosa.util.frame(y, frame_length=2205, hop_length=2205)
        db_frames = [get_db(frame) for frame in frames.T]
        db_segments.append(db_frames)
    db_segments = [tmp for tmps in db_segments for tmp in tmps]
    mean_db = np.mean(db_segments)
    std_db = np.std(db_segments)
    return mean_db, std_db

def get_f0(y, show=False):
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    if show:
        plt.plot(librosa.times_like(f0), f0)
        plt.show()
    f0 = f0[~np.isnan(f0)]
    if len(f0) == 0:
        jitter = np.nan
    else:
        periods = 1 / f0
        jitter = np.mean(np.abs(np.diff(periods))) / np.mean(periods)
    return f0, jitter

def get_f0_features(ys):
    f0_segments = []
    jitters = []
    for y in ys:
        frames = librosa.util.frame(y, frame_length=2205, hop_length=2205)
        for frame in frames.T:
            f0, jitter = get_f0(frame)
            f0_segments.append(f0)
            jitters.append(jitter)
    f0_segments = [tmp for tmps in f0_segments for tmp in tmps]
    mean_f0 = np.mean(f0_segments)
    std_f0 = np.std(f0_segments)
    return mean_f0, std_f0, np.nanmean(jitters), np.nanstd(jitters)

def get_mfcc(y, show=False):
    mfcc = librosa.feature.mfcc(y=y, sr=22050, n_mfcc=13)
    if show:
        plt.imshow(mfcc, origin='lower', aspect='auto')
        plt.show()
    return mfcc

def get_mfcc_features(ys):
    mfcc_segments = []
    for y in ys:
        frames = librosa.util.frame(y, frame_length=2205, hop_length=2205)
        mfcc_frames = np.concatenate([get_mfcc(frame) for frame in frames.T], axis=1)
        mfcc_segments.append(mfcc_frames)
    mfcc_segments = np.concatenate(mfcc_segments, axis=1)
    mean_mfcc = np.mean(mfcc_segments, axis=1)
    std_mfcc = np.std(mfcc_segments, axis=1)
    return mean_mfcc, std_mfcc