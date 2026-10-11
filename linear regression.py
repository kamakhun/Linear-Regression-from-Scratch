X = [2,3,4,5,6,7,8,9,10]
Y = [4,6,8,9,10,12,13,15,16]

w = 1
b = 1
n = len(X)
La = 0.01  #learning rate
for epoch in range (966):    # 960-1000 and more
    Yp_list = []  # list of predictions
    loss = 0
    dw = 0
    db = 0
    for i in X:
        Yp = w*i+b
        Yp_list.append(Yp)

    for i in range (n):
        loss += (Y[i] - Yp_list[i])**2

    MSE = loss/len(Y)

    for i in range(n):
        yp = w * X[i] + b
        error = Y[i] - yp
        dw += -2 * X[i] * error
        db += -2 * error

    dw /= n  # MSE derivative w
    db /= n  # MSE derivative b
    w = w - (La*dw)   # update for w
    b = b - (La*db)   # update for b

Yp_list = []
loss = 0
for i in X:
    Yp = w * i + b
    Yp_list.append(Yp)
for i in range(len(Y)):
    loss += (Y[i] - Yp_list[i]) ** 2
MSE = loss / len(Y)


print(w, b, MSE)