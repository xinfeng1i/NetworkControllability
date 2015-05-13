import numpy as np
import networkx as nx
import exact_controllability
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import csv
import operator

def exact_controllability_run_on_ER_one_time(n, prob_start, prob_end, data_cnt):
    probs = np.linspace(prob_start, prob_end, num = data_cnt);
    driver_nodes = [0.0] * len(probs)
    driver_dense = [0.0] * len(probs)
    for i in range(len(probs)):
        p = probs[i]
        G = nx.erdos_renyi_graph(n, p)
        (ND, ND_lambda) = exact_controllability.get_number_of_driver_nodes(G)
        driver_nodes[i] = ND
        driver_dense[i] = (ND + 0.0) / (n + 0.0)
    return (probs, driver_dense)

def exact_controllability_run_on_ER(n, prob_start, prob_end, data_cnt, runcnt):
    tot_probs = [0.0] * data_cnt
    tot_dense = [0.0] * data_cnt
    for run_cnt in range(runcnt):
        (probs, driver_dense) = exact_controllability_run_on_ER_one_time(n, prob_start, prob_end, data_cnt)
        tot_probs = map(operator.add, tot_probs, probs)
        tot_dense = map(operator.add, tot_dense, driver_dense)
    
    tot_probs = [x / (runcnt + 0.0)  for x in tot_probs]
    tot_dense = [x / (runcnt + 0.0)  for x in tot_dense]
    with open("ER_Result.csv", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(tot_probs, tot_dense))

    plt.plot(tot_probs, tot_dense, 'ro')
    plt.title('Exact Controllability Run on ER network')
    plt.xlabel('$p$')
    plt.ylabel('$n_D$')
    plt.show()

class A():
    def __init__(self):
        self.x = 10
        self.y = 20
class B():
    def __init__(self):
        self.a = 30
        self.b = 40
        self.A = A()

if __name__ == "__main__":
    d = {1:0, 2:5, 3:100, 6:3, 100:3}

    min_value = min([x for x in d.values() if x - 0.0 > 1E-8])
    min_key = None
    for k, v in d.iteritems():
        if v == min_value:
            min_key = k
            break