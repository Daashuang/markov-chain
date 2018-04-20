import numpy as np

states = ('healthy','faver')
observations = ('normal','cold','dizzy')
start_probability = {'health':0.6,'faver':0.4}
transition_probability = {
    'healthy':{'healthy':0.7,'faver':0.3},
    'faver':{'healthy':0.4,'faver':0.6}
}
emission_probability = {
    'healthy':{'normal':0.5,'cold':0.4,'dizzy':0.1},
    'faver':{'normal':0.1,'cold':0.3,'dizzy':0.6}
}

def simulate(T):
    def draw_from(probs):
        return np.where(np.random.multinomial(1,probs) == 1)[0][0]

    observations = np.zeros(T,dtype=int)
    states = np.zeros(T,dtype=int)
    states[0] = draw_from(pi)
    observations[0] = draw_from(B[states[0],:])
    for t in range(1,T):
        states[t] = draw_from(A[states[t-1],:])
        observations[t] = draw_from(B[states[t],:])
    return observations,states

def generate_index_map(lables):
    id2label = {}
    label2id = {}
    i = 0
    for l in lables:
        id2label[i] = l
        label2id[l] = i
        i += 1
        return id2label,label2id

states_id2label, states_label2id = generate_index_map(states)
observations_id2label, observations_label2id = generate_index_map(observations)
print(states_id2label, states_label2id)
print(observations_id2label, states_label2id)

def convert_map_to_vector(map_,label2id):
    v = np.zeros(len(map_),dtype=float)
    for e in map_:
        v[states_label2id[e]] = map_[e]
    return  v

def convert_map_to_matrix(map_,label2id1,label2id2):
    m = np.zeros((len(label2id1),len(label2id2)),dtype=float)
    for line in map_:
        for col in map_[line]:
            m[label2id1[line]][label2id2[col]] = map_[line][col]
    return m

A = convert_map_to_matrix(transition_probability,states_label2id,states_label2id)
print(A)
B = convert_map_to_matrix(emission_probability,states_label2id,observations_label2id)
print(B)
observations_index = [observations_label2id[o] for o in observations]
pi = convert_map_to_vector(start_probability,states_label2id)
print(pi)

observations_data, states_data = simulate(10)
print(observations_data)
print(states_data)
print("病人的状态：",[states_id2label[index] for index in state_data])
print("病人的观察：", [observations_id2label[index] for index in observations_data])



