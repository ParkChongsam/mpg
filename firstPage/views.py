from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

from sklearn.externals import joblib

reloadedModel = joblib.load('./models/RFModelforMPG.pkl')


def index(request):
    temp = {}
    temp['cylinders'] = 8
    temp['displacement'] = 307
    temp['horsepower'] = 130
    temp['weight'] = 3504
    temp['acceleration'] = 12
    temp['model_year'] = 70
    temp['origin'] = 1
    context = {'temp': temp}

    return render(request, 'index.html', context)
    # return HttpResponse({'a':1})


def predictMPG(request):
    # print(request)
    if request.method == 'POST':
        temp = {}
        temp['cylinders'] = request.POST.get('cylinderVal')
        temp['displacement'] = request.POST.get('dispVal')
        temp['horsepower'] = request.POST.get('hrsPwrVal')
        temp['weight'] = request.POST.get('weightVal')
        temp['acceleration'] = request.POST.get('accVal')
        temp['model_year'] = request.POST.get('modelVal')
        temp['origin'] = request.POST.get('originVal')

        temp2 = temp.copy()
        temp2['model year'] = temp['model_year']
        print(temp.keys(), temp2.keys())
        # del temp2['model_year']

    testData = pd.DataFrame({'x': temp2}).transpose()
    scoreval = reloadedModel.predict(testData)[0]

    context = {'scoreval': scoreval, 'temp': temp}
    # 기본값을 입력후 결과와 함께 입력한 값이 보여지도록 하기 위해 'temp':temp 를 context에 넣어준다.

    return render(request, 'index.html', context)
