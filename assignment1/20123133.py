#%%
import numpy as np, pandas as pd
import operator
import matplotlib.pyplot as plt

seed = 0 #seed for reproduction

def fitness(input_data, label, weight):
    """
    calculate the fitness function, which returns the correcr rate (float)
    """

    temp = np.dot(input_data, weight)
    calculation = np.where(temp >= 0, 1, 0)
    correct_rate = np.equal(calculation, label).mean()
    return correct_rate


def tournament_selection(input_data, label, weights, number_of_model, tournament_selection_count, seed=None):
    """
    Run the tournament selection here
    Noted that the tournament_selection_count is the number in out tournament selection (number of competitor)
    """
    tournament_random_list = np.random.RandomState(seed).randint(0, number_of_model-1, size=tournament_selection_count)
    correct_rate_temp = {}
    for ts in tournament_random_list:
        correct_rate_temp[ts] = fitness(input_data, label, weights[ts])
    best_model_number = max(correct_rate_temp.items(), key=operator.itemgetter(1))[0]
    return best_model_number

#preparation
data = pd.read_csv('training-set.csv', header=None)
label = data.iloc[:, -1]
input_data = data.iloc[:, :-1]
input_data['threshold'] = 1 #threshold is 1 nothing but with weighting
row, col = input_data.shape

loop = 100 #100 iteration
number_of_model = 5000 #the tournament selection is based on the 5000 models
tournament_selection_count = 5 #for each time, we will run the competition within 5 models
copy = .09
crossover = .9
mutation = .01
#copy + crossover + mutation = 1

weights = np.random.RandomState(seed).normal(loc=0, scale=1.2, size=[number_of_model , col]) #we have 10 parameter
average_correct_rate_loop = []

for l in range(loop):
    updated_weights = []
    #copy 
    for k in range(int(copy*number_of_model)):
        best_model_number = tournament_selection(input_data, label, weights, number_of_model, tournament_selection_count, seed=seed+(l+1)*10000+k)
        updated_weights.append(weights[best_model_number])

    #crossover
    for k in range(int(crossover*number_of_model)):
        parents_temp = []
        for p in range(2): #mother & father
            parents_temp.append(tournament_selection(input_data, label, weights, number_of_model, tournament_selection_count, seed=seed+(l+1)*10000+k+p))
        rng1 = np.random.RandomState(seed+(l+1)*10000+k)
        crossover_factor = rng1.randint(0, col)
        crossover_weight = np.append(weights[parents_temp[0]][0:crossover_factor], weights[parents_temp[1]][crossover_factor:col])
        updated_weights.append(crossover_weight)

    #mutation
    for k in range(int(mutation*number_of_model)):
        best_model_number = tournament_selection(input_data, label, weights, number_of_model, tournament_selection_count, seed=seed+(l+1)*10000+k)
        rng2 = np.random.RandomState(seed+(l+1)*10000+k)
        mutation_factor = rng2.randint(0, col)
        mutation_weight = np.append(weights[best_model_number][0:mutation_factor], [r for r in rng2.normal(loc=0, scale=1, size=[col-mutation_factor])])
        updated_weights.append(mutation_weight)

    weights = updated_weights.copy()
    average_correct_rate = []
    for weight in weights:
        average_correct_rate.append(fitness(input_data, label, weight))
    average_correct_rate_loop.append(sum(average_correct_rate)/len(average_correct_rate))

#final model
correct_rate_final = {}
for n in range(len(weights)):
    correct_rate_final[n] = fitness(input_data, label, weights[n])
best_model_number = max(correct_rate_final.items(), key=operator.itemgetter(1))[0]
print('final correct rate:{}, with coresponding weight{}'.format(correct_rate_final[best_model_number], weights[best_model_number]))
# final correct rate:1.0, with coresponding weight[-0.08338671, -0.35673308, 0.99734321, -0.21327968, 2.42218153, 0.75691467, -2.37031905, -1.2437123, 0.59354745, 0.0094335]

#plot the result
num = np.arange(loop)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(num, average_correct_rate_loop)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.show()
