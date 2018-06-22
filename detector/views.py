from django.shortcuts import render, redirect
from detector.forms import SignUpForm, LogInForm, Detect
from detector.models import UserModel, Values
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('HELLO FROM DETECTOR')

    return render(request, 'detector/index.html')

def user(request):
    if request.method=="POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            #fetchin the signup form....................................................................................
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']
            user = UserModel(name = name, address = address, contact=contact, email = email, age=age, gender=gender, password = password)
            user.save()
#        #redirecting user accordingly...............................................................................
            return redirect('login/')

        #handling form error and get request............................................................................
        else:
            errors = form.errors
            return render(request, 'detector/user.html', {'form': form, 'errors':errors})

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'detector/user.html', {'form': form})


def login_view(request):
    getform = LogInForm()
    if request.method == "POST":
        form = LogInForm(request.POST or None)
        if form.is_valid():
            #fetching the form details..................................................................................
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = UserModel.objects.filter(name = name)
            if user:
                user1 = UserModel.objects.get(name= name)
                #authenticating user............................................................
                if password==user1.password:
                    return redirect('input/')

                else:

                    message = "Wrong Password."
                    return render(request, 'detector/login.html', {'form':getform,"login_error":message})
            else:
                message = "User does not exist."
                return render(request, 'detector/login.html', {'form':getform,"login_error":message})
        #handling form error............................................................................................
        else:
            errors = form.errors
            return render(request, 'detector/login.html',{'form':getform,"errors":errors})

    elif request.method == 'GET':
        getform = LogInForm()

    return render(request, 'detector/login.html', {'form': getform})

def input_user(request):
    if request.method=="POST":
        form = Detect(request.POST or None)
        if form.is_valid():
            # fetching the details form....................................................................................
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            cp = form.cleaned_data['cp']
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            thalach = form.cleaned_data['thalach']
            exang = form.cleaned_data['exang']
            slope = form.cleaned_data['slope']
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']
            #user = Input(age =age, chest_pain =chest_pain, rest_bpress=rest_bpress , blood_sugar=blood_sugar, rest_electro=rest_electro,
            #             max_heart_rate=max_heart_rate, exercice_angina=exercice_angina)
            #user.save()
            #......................temp.........................


            user = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,slope,ca,thal]]
            df = pd.read_csv(r'C:\Users\SATYAM MITTAL\pythonproject\djangoproject\detector\old.csv')
            x = df.iloc[:, :12]
            y = df.iloc[:, 12:]
            # split
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

            # Applying RandonForestClassifier
            clf = RandomForestClassifier(n_estimators=100)
            clf.fit(x_train, y_train)
            yp = clf.predict(user)
            if yp >2:
                return render(request, 'detector/detect.html', {"result":"Risk Of Heart Attack.You might concern a doctor"})
                   #redirecting user accordingly...............................................................................
            else:
                return render(request, 'detector/detect.html', {"result": "No Risk Of Heart Attack.You might not concern a doctor"})

        # handling form error and get request............................................................................
        else:
            errors = form.errors
            message = "Please Enter Values."
            return render(request, 'detector/input.html', {'form': form, "error":message})

    elif request.method == 'GET':
        form = Detect()

    return render(request, 'detector/input.html', {'form': form})

def detect(request):
    return render(request, "detector/detect.html")

def admin(request):
    return HttpResponse("YOU ARE UNDER ADMIN")