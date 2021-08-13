from django.shortcuts import render
from translation.models import login
output_text = ""

def button(request):
    return render(request,'translate.html')

def homee(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        ins = login(email=email,password=password, password_confirmation=password_confirmation)
        ins.save()
        print("data saved")
    return render(request,'home.html')

def aboutt(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

def set_input(request):
    if request.method == 'POST':
        input = request.POST.get('input')
        return render(request,'translate.html')

def set_output(request):
    if request.method == 'POST':
        output = request.POST.get('output')
        return render(request,'translate.html')

def output(request):
    output = request.POST.get('output')
    input = request.POST.get('input')
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    ''' recording the sound '''

    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    ''' Recorgnizing the Audio '''

    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language=input
            )
        print("Decoded Text : {}".format(text))

    except Exception as ex:
        print(ex)

    from googletrans import Translator

    translater= Translator()

    out=translater.translate(text, dest=output)
    
    print(out.text)
    test=out.text
    from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
    import os
    text=out.text

    language = input #hindi
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save('medium_hindi.wav')
#to play string in wav
    os.system('start medium_hindi.wav')
    
    return render(request,'translate.html', {'test':test})

    


    