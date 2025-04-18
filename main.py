import math

"""
Juno boresight taken from https://space.stackexchange.com/questions/26457/juno-rf-power-output
"""

rf_sig_at_reciever_LNA = -165 #dBm
antenna_efficiency = 0.6
distance = 850949987 #km
frequency = 8.46 #GHz
juno_boresight_gain = 44.1 #dBi

fspl = 20*math.log10(distance) + 20*math.log10(frequency) + 92.45

gain_at_antenna = fspl - juno_boresight_gain + rf_sig_at_reciever_LNA


def calculate_antenna_diameter(G_dB, efficiency, frequency_ghz):
    # Speed of light factor for GHz: lambda = 0.3 / f(GHz)
    wavelength = 0.3 / frequency_ghz

    # Convert gain from dB to linear scale
    G_linear = 10 ** (G_dB / 10)

    # Apply the formula
    D = (wavelength / math.pi) * math.sqrt(G_linear / efficiency)

    return D


def print_stuff():
    print("Free space path loss: ", fspl, " dBm")
    print("Antenna gain needed: ", gain_at_antenna, " dBi")
    print("Dish size: ", calculate_antenna_diameter(gain_at_antenna, antenna_efficiency, frequency), " m")


if __name__ == '__main__':
    print_stuff()

