from django.shortcuts import render
import pickle
# Create your views here.

def home(request):
    return render(request,'home.html')



with open('model/mushroom.sav','rb') as f:
    mp = pickle.load(f)
l = {1 : 'Poisonous',0:'Edible'}
def Preedict(request):
    if request.method == "POST":
        capSurface = request.POST.get('capSurface', '')
        capColor = request.POST.get('capColor', '')
        bruishes = request.POST.get('bruishes', '')
        odour = request.POST.get('odour', '')
        gillSize = request.POST.get('gillSize', '')
        gillColour = request.POST.get('gillColour', '')
        stalkShape = request.POST.get('stalkShape', '')
        stalkRoot = request.POST.get('stalkRoot', '')
        surfaceBelow = request.POST.get('surfaceBelow', '')
        colorAbove = request.POST.get('colorAbove', '')
        colorBelow = request.POST.get('colorBelow', '')
        sporePrint = request.POST.get('sporePrint', '')
        population = request.POST.get('population', '')
        habitat = request.POST.get('habitat', '')
        result = l[mp.predict([[capSurface,capColor,bruishes,odour,gillSize,gillColour,stalkShape,stalkRoot,surfaceBelow,colorAbove,colorBelow,sporePrint,population,habitat]])[0]]
        return render(request,'message.html',{'result':result})
        # print("**",capSurface,capColor,bruishes,odour,gillSize,gillColour,stalkShape,stalkRoot,surfaceBelow,colorAbove,colorBelow,sporePrint,population,habitat)
    return render(request, 'prediction.html')


def Description(request):
    return render(request,'terms.html')