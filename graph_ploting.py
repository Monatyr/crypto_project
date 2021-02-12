import matplotlib.pyplot as plt
import csv

def get_data_from_csv(crytpo_name = 'BTC'):
    x_axis = []
    y_axis = []

    with open('{}_data.csv'.format(crytpo_name), 'r') as file:
        
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            x_axis.append(row[0])
            y_axis.append(row[1])
            print(row[0], row[1])

    return (x_axis, y_axis)


def plot_graph(data, crypto_name = 'BTC'):
    x = data[0]
    y = data[1]

    plt.plot(x,y)
    plt.xlabel('Datetime')
    plt.ylabel('Value')
    plt.title(crypto_name)
    plt.show()

plot_graph(get_data_from_csv())