from os import path
import numpy as np
import math


def read_oscillatory_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)

    lengths = data[:, 0]
    amplitudes = data[:, 1]
    mean_amp = np.mean(amplitudes)
    max_amp = np.max(amplitudes)

    return lengths, amplitudes, mean_amp, max_amp


def read_standing_wave_data(filename):
    data = np.genfromtxt(filename, delimiter=",", skip_header=1)

    lengths = data[:, 0]
    tensions = data[:, 1]
    speeds = np.sqrt(tensions / 1)

    return lengths, tensions, speeds


def main():

    # Personalization values from MY ID
    d1 = 7
    d2 = 3
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    # Original files
    osc_file = "oscillatory_2672601.csv"
    stand_file = "standing_2672601.csv"

    # New personalized files
    new_osc_file = "oscillatory_2672601_personalized.csv"
    new_stand_file = "standing_2672601_personalized.csv"



    # Component A
   
    lengths1, amplitudes, mean_amp, max_amp = read_oscillatory_wave_data(osc_file)

    print("Original oscillatory amplitudes:", amplitudes)
    print("Original mean amplitude:", mean_amp)
    print("Original max amplitude:", max_amp)


    lengths2, tensions, speeds = read_standing_wave_data(stand_file)

    print("\nOriginal tensions:", tensions)
    print("Original wave speeds:", speeds)

    # Component B - Oscillatory

    rows_needed = 5 + d2

    new_lengths = lengths1[:rows_needed]
    new_amplitudes = amplitudes[:rows_needed] + shift

    np.savetxt(
        new_osc_file,
        np.column_stack((new_lengths, new_amplitudes)),
        delimiter=",",
        header="length,amplitude",
        comments=""
    )

    new_mean_amp = np.mean(new_amplitudes)
    new_max_amp = np.max(new_amplitudes)

    print("\nPersonalized Oscillatory Data")
    print("New mean amplitude:", new_mean_amp)
    print("New max amplitude:", new_max_amp)


    # -------------------------
    # Component B - Standing
    # -------------------------

    rows_needed2 = 4 + rows_keep

    new_lengths2 = lengths2[:rows_needed2]
    new_tensions = tensions[:rows_needed2] * k
    new_speeds = np.sqrt(new_tensions / 1)

    np.savetxt(
        new_stand_file,
        np.column_stack((new_lengths2, new_tensions)),
        delimiter=",",
        header="length,tension",
        comments=""
    )

    print("\nPersonalized Standing Wave Data")
    print("New wave speeds:", new_speeds)


if __name__ == "__main__":
    main()