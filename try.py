import pickle as pkl

model1 = pkl.load(open('encoder_condition.pkl' , 'rb'))
model2 = pkl.load(open('condition_model.pkl' , 'rb'))

output = model2.predict([[23.8,4.7,1004.0,41.0,24.8,24.8]])
print(model1.inverse_transform([output]))

print(model1.inverse_transform([2]))