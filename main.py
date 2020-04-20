weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(4):
    print("--------\n Weight: " + str(weight))
    pred = input * weight
    error = (pred - goal_pred) **2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error: " + str(error) + "\n Prediction: " + str(pred))
    print("Delta: " + str(delta) + "\n Weight Delta: " + str(weight_delta))
