import math

rf_sig_at_reciever_LNA = -165 #dBm
antenna_efficiency = 0.6
distance = 850949987 #km
frequency = 8.46 #GHz

fspl = 20*math.log(distance) + 20*math.log(frequency) + 92.45


def print_stuff():
    print("Free space path loss: ", fspl, " dBm")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_stuff()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
