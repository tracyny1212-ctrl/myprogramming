import numpy as np
import math

# Personalization values
# Student ID: 6309037

d1 = 7
d2 = 3
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2

print("d1 =", d1)
print("d2 =", d2)
print("k =", k)
print("shift =", shift)
print("rows_keep =", rows_keep)
print()

# Component A
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

    osc_file = "oscillatory_6309037.csv"
    stand_file = "standing_6309037.csv"

    # Component A

    lengths1, amplitudes, mean_amp, max_amp = read_oscillatory_wave_data(osc_file)

    print("Original oscillatory amplitudes:", amplitudes)
    print("Mean amplitude:", mean_amp)
    print("Max amplitude:", max_amp)


    lengths2, tensions, speeds = read_standing_wave_data(stand_file)

    print("\nOriginal tensions:", tensions)
    print("Wave speeds:", speeds)

    # Component B
 

    # Oscillatory personalization

    new_amplitudes = amplitudes + shift

    new_mean = np.mean(new_amplitudes)
    new_max = np.max(new_amplitudes)

    print("\nShifted amplitudes:", new_amplitudes)
    print("New mean:", new_mean)
    print("New max:", new_max)


    # Standing wave personalization

    new_tensions = tensions * k
    new_speeds = np.sqrt(new_tensions / 1)

    print("\nScaled tensions:", new_tensions)
    print("New wave speeds:", new_speeds)

if __name__ == "__main__":
    main()