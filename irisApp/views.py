from django.shortcuts import render
from joblib import load

#model = load('./savedModels/model.joblib')
model = load('./savedModels/knn.joblib')

# Create your views here.
def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    sepal_length = request.GET['sepal_length']
    sepal_width = request.GET['sepal_width']
    petal_length = request.GET['petal_length']
    petal_width = request.GET['petal_width']
    ypred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    print(ypred)
    return render(request, 'result.html')
