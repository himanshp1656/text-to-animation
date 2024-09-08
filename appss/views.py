from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import EmailMessage, get_connection
import random
import string
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# pass himanshu username himanshu
# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


def note_taking(request):
    return render(request, 'note_taking.html')

from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import sys
import sys
from io import StringIO
import os
import os
from django.http import Http404

import os
import time
import subprocess
from django.shortcuts import redirect
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv('GEMINI_API_KEY')
# API_KEY='AIzaSyCOxPtTgqfxVBhUADkAk96GjkgtJqHTDVs'
list='hihi'

def generating(response1):
    print('Attempting to generate Manim code...')
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    convo = model.start_chat(history=[])
    print(response1)
    # Constructing the prompt for the AI model
    response = f"{response1}, write manim code to visualize the above concept in mp4 video only. Give me only the code. Give no explanation. Also add the last line if __name__ == '__main__': scene = ... scene.render() for the code to run. Don't use any image or other source, it should be pure Manim code and also add this line: from manim.utils.color.XKCD import *. Use RoundedRectangle instead of round_corners, also ArcBetweenPoints instead of get_paths if needed. Focus on every point, use only GREEN, BLUE, RED, DARK_BROWN color. Don't add any image, I repeat don't use any image or extra color, and use fadein instead of create. Write the minimal code for v0.18.0.post0. The code provided by you should run 100%."

    convo.send_message(response)
    response_text = convo.last.text

    if response_text.startswith("```python"):
        response_text = response_text[9:-5]  # Slice the string to remove the code block markers

    # Writing the generated code to a file
    with open('manimm.py', 'w') as file:
        file.write(response_text)


def generating_again(response1):
    print('Attempting to generate Manim code...')
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    convo = model.start_chat(history=[])
    print(response1)
    # Constructing the prompt for the AI model
    response = f"{response1}, write manim code to visualize the above concept in mp4 video only. Give me only the code. Give no explanation. Also add the last line if __name__ == '__main__': scene = ... scene.render() for the code to run. Don't use any image or other source, it should be pure Manim code and also add this line: from manim.utils.color.XKCD import *. Use RoundedRectangle instead of round_corners, also ArcBetweenPoints instead of get_paths if needed. Focus on every point, use only GREEN, BLUE, RED, DARK_BROWN color. Don't add any image, I repeat don't use any image or extra color, and use fadein instead of create. Write the minimal code for v0.18.0.post0. The code provided by you should run 100%. always close the scene.render() bracket"

    convo.send_message(response)
    response_text = convo.last.text

    if response_text.startswith("```python"):
        response_text = response_text[9:-5]  # Slice the string to remove the code block markers

    # Writing the generated code to a file
    with open('manimm.py', 'w') as file:
        file.write(response_text)

def filename():
    with open('manimm.py', 'r') as file:
        content = file.read()
        index = content.find('class')
        if index != -1:
            next_word_index = content.find(' ', index + len('class') + 1)
            if next_word_index != -1:
                word_after_class = content[index + len('class'): next_word_index].strip()
                word_after_class = word_after_class[:-8]  # Adjust this if needed
                print("Word after 'class':", word_after_class)
                file_path = f'media/videos/1080p60/{word_after_class}.mp4' 
                if(os.path.exists(file_path)):
                    return file_path
                return '/'+file_path
    return None

def manim_runner():
    try:
        with open('manimm.py', 'r') as file:
            content = file.read()
        # Check if the last character is an opening parenthesis '('
        if content.endswith('('):
            # If so, add a closing parenthesis ')'
            print('yes adding )')
            content += ')'
        # If you want to save the modified content back to the file (optional):
        with open('manimm.py', 'w') as file:
            file.write(content)
            
        result = subprocess.run(["python3", "manimm.py"], capture_output=True, text=True)
        errors = result.stderr
        if errors:
            print("Script Errors:\n", errors)
            list=errors
            return 'haha'
        time.sleep(3)
        print('yes pressing s')
        list='hihi'
        return 'hihi'
    except Exception as e:
        print("Error running manimm.py:", str(e))
        return str(e)
    

def generate_video(request):
    if request.method == 'POST':
        inp = request.POST.get('inp')
        # Initial AI query to generate a note
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
        convo = model.start_chat(history=[])
        response1 = f"Write a note in 100 words for '{inp}' so that I can generate Manim code for it. Try to give specific info about using which color and shapes"
        convo.send_message(response1)
        response1 = convo.last.text

        # Generating the Manim code
        generating(response1)
        
        # Running the Manim code to generate the video
        manim_runner()

        file_path = filename()
        print(f"File path: {file_path}")
    
        # Attempting to redirect if the video is generated
        if file_path and os.path.exists(file_path):
            print('Redirecting to generated video...')
            return redirect("/"+file_path)
        else:
            print('Video not generated, attempting again...')
            
            # Retry up to 5 times
            while(True):
                time.sleep(15)
                print('jejejje',list)
                if list!='hihi':
                    with open('manimm.py', 'r') as file:
                        content = file.read()
                    response1 = f"{content} it is producing this error: {list}"
                generating_again(response1)
                resperrors = manim_runner()
                file_path = filename()
                print('hihihihihihiii',file_path)
                if file_path and os.path.exists(file_path):
                    print('Redirecting to generated video...')
                    return redirect("/"+file_path)
                
                if list!='hihi':
                    continue
                time.sleep(30)

    # If all attempts fail, return an error response
    return redirect('/error-page/')  # Redirect to an error page if needed

























def expense(request):
    return render(request,'expense.html')
def optimize(request):
    return render(request,'time.html')
def send_otp(email):
    otp = ''.join(random.choice(string.digits) for _ in range(6))
    subject = 'Your OTP for Signup'
    message = f'Your OTP is {otp}. Please use this OTP to complete your registration.'
    from_email = 'neoncreater69@outlook.com'  # Update with your email address
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return otp


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['mail']
        password = request.POST['pass']

        # Create a new user
        user = User.objects.create_user(username=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Log in the user
        login(request, user)

        # Redirect to a success page or homepage
        return redirect('/')

    # If it's not a POST request, render the signup form
    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Authentication failed, show an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # If it's not a POST request, render the login form
        return render(request, 'login.html')



from django.shortcuts import render, redirect
from .models import teacher  # Import your model
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


@login_required
def teacher_submit(request):
    if request.method == 'POST':
        # Get the form data from the request
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mail_id = request.POST['mail_id']
        subject = request.POST['subject']   
        degree = request.FILES['degree'] 

        # Create a new class_teacher object and save it to the database
        new_teacher = teacher(
            user=user,
            first_name=first_name,
            last_name=last_name,
            mailid=mail_id,
            subject=subject,
            degree=degree
        )
        new_teacher.save()

        # Optionally, you can redirect the user to a success page
        return redirect('/')

    # Handle GET requests or form rendering here
    else:
        # Render the form template for GET requests
        return render(request, 'teacher.html')

from appss.models import teacherlist
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import teacherlist  # Import your TeacherList model

 # Import your TeacherList model
import random
import re

def search(request):
    if request.method == 'POST':
        text = request.POST['search']
        r = requests.get(f'https://www.teacheron.com/{text}-tutors')
        matching_teachers = teacherlist.objects.filter(subject__icontains=text)

        if r.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(r.text, 'html.parser')
            
            

            # Find all elements with the class "profile-description"
            profile_descriptions = soup.find_all(class_="profile-description")

            # Find all elements with itemprop="name"
            names = soup.find_all(itemprop="name")

            # Find all elements with itemprop="url"
            urls = soup.find_all(itemprop="url")
            profile_images = soup.find_all(class_="lozad-custom-profile-img")
           
            teacherlist_data = []

            

        
            i=0
            # Iterate through names, descriptions, and URLs
            for name, description, url ,profile_image in zip(names, profile_descriptions, urls , profile_images):
                teacher_name = name.get_text()
                teacher_desc = description.get_text()
                teacher_url = url.get('content')
                email_username = re.sub(r'\s', '_', teacher_name)

                import random

# List of common email domains
                email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "example.com"]

                random_domain = random.choice(email_domains)

                # Create the random email address
                random_email = f"{email_username}{random.randint(10000,99999)}@{random_domain}"

                # print(random_email)

                

                # Check if the name has 20 or fewer words
                if len(teacher_name.split()) <= 20:
                    teacher_location = ''
                    teacher_charge=''
                    teacher_online_experience=''
                    teacher_total_experience=''

                    # Find the elements containing experience and location information
                    location_element = name.find_next(class_="tooltips")  # Assuming experience is located after the name
                    charge_element = location_element.find_next(class_="tooltips")
                    online_element = charge_element.find_next(class_="tooltips")
                    total_element = online_element.find_next(class_="tooltips")
                    
                    if location_element:
                        teacher_location = location_element.get_text(strip=True)
                   
                    if location_element:
                        teacher_charge = charge_element.get_text(strip=True)
                        
                    if location_element:
                        teacher_online = online_element.get_text(strip=True)
                        
                    if location_element:
                        teacher_total = total_element.get_text(strip=True)
                        

                    if 'data-src' in profile_image.attrs:
                        teacher_profile_image = profile_image['data-src']
                    else:
                        # Handle the case where 'data-src' attribute doesn't exist or is empty
                        teacher_profile_image = 'default_image_url.jpg'

                    
                    teacherlist_data.append({
                        'name': teacher_name,
                        'description': teacher_desc,
                        'url': teacher_url,
                        'i':i,
                        'profile_image': teacher_profile_image,
                        'online': teacher_online,
                        'total': teacher_total,
                        'charge': teacher_charge,
                        'location': teacher_location,
                        'email': random_email

                    })
                    i+=1

                    # print("Name:", teacher_name)
                    # print("Description:", teacher_desc)
                    # print("URL:", teacher_url)
                    # print()

            # Save the data to your TeacherList model
            # for data in teacherlist_data:
            #     teacherlist1 = teacherlist(**data)
            #     teacherlist1.save()
            combined_results = list(matching_teachers) + teacherlist_data

            return render(request, 'search.html', {'teacherlist': combined_results})
        else:
            print("Failed to retrieve the page. Status code:", r.status_code)
    else:
        teacherlist_data = teacherlist.objects.all()
        text = 'java'
        r = requests.get(f'https://www.teacheron.com/{text}-tutors')
        matching_teachers = teacherlist.objects.filter(subject__icontains=text)

        if r.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(r.text, 'html.parser')
            
            

            # Find all elements with the class "profile-description"
            profile_descriptions = soup.find_all(class_="profile-description")

            # Find all elements with itemprop="name"
            names = soup.find_all(itemprop="name")

            # Find all elements with itemprop="url"
            urls = soup.find_all(itemprop="url")
            profile_images = soup.find_all(class_="lozad-custom-profile-img")
           
            teacherlist_data = []

            

        
            i=0
            # Iterate through names, descriptions, and URLs
            for name, description, url ,profile_image in zip(names, profile_descriptions, urls , profile_images):
                teacher_name = name.get_text()
                teacher_desc = description.get_text()
                teacher_url = url.get('content')
                email_username = re.sub(r'\s', '_', teacher_name)

                import random

# List of common email domains
                email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "example.com"]

                random_domain = random.choice(email_domains)

                # Create the random email address
                random_email = f"{email_username}{random.randint(10000,99999)}@{random_domain}"

                # print(random_email)

                

                # Check if the name has 20 or fewer words
                if len(teacher_name.split()) <= 20:
                    teacher_location = ''
                    teacher_charge=''
                    teacher_online_experience=''
                    teacher_total_experience=''

                    # Find the elements containing experience and location information
                    location_element = name.find_next(class_="tooltips")  # Assuming experience is located after the name
                    charge_element = location_element.find_next(class_="tooltips")
                    online_element = charge_element.find_next(class_="tooltips")
                    total_element = online_element.find_next(class_="tooltips")
                    
                    if location_element:
                        teacher_location = location_element.get_text(strip=True)
                   
                    if location_element:
                        teacher_charge = charge_element.get_text(strip=True)
                        
                    if location_element:
                        teacher_online = online_element.get_text(strip=True)
                        
                    if location_element:
                        teacher_total = total_element.get_text(strip=True)
                        

                    if 'data-src' in profile_image.attrs:
                        teacher_profile_image = profile_image['data-src']
                    else:
                        # Handle the case where 'data-src' attribute doesn't exist or is empty
                        teacher_profile_image = 'default_image_url.jpg'

                    
                    teacherlist_data.append({
                        'name': teacher_name,
                        'description': teacher_desc,
                        'url': teacher_url,
                        'i':i,
                        'profile_image': teacher_profile_image,
                        'online': teacher_online,
                        'total': teacher_total,
                        'charge': teacher_charge,
                        'location': teacher_location,
                        'email': random_email

                    })
                    i+=1

                    # print("Name:", teacher_name)
                    # print("Description:", teacher_desc)
                    # print("URL:", teacher_url)
                    # print()

            # Save the data to your TeacherList model
            # for data in teacherlist_data:
            #     teacherlist1 = teacherlist(**data)
            #     teacherlist1.save()
            combined_results = list(matching_teachers) + teacherlist_data

            return render(request, 'search.html', {'teacherlist': combined_results})
 # Fetch all teacherlist objects from the database

        return render(request, 'search.html', {'teacherlist': teacherlist_data})


def chat_view(request):
    return render(request, 'chat.html')


from django.http import JsonResponse
import openai
from django.conf import settings
def chat_with_gpt(request):
    user_input = request.GET.get('user_input')
    if not user_input:
        return JsonResponse({'response': 'Please provide user input'})

    # Initialize OpenAI API client
    openai.api_key = settings.OPENAI_API_KEY

    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=1000
    )

    return JsonResponse({'response': response.choices[0].text})

import google.generativeai as genai

from django.shortcuts import render

def teacherprofie(request , teacher_id):
    pass



import re
from django.http import JsonResponse
from django.shortcuts import render

def roadmap(request):
    if request.method == 'POST':
        topic = request.POST.get('inp')

        if not topic:
            return JsonResponse({'response': 'Please provide a topic'})

        user_input = f'steps to become {topic} in bullet points only without any subpoint or description use @ as bulletpoint and dont use numbers anywhere in your text and no extra lines only bulletpoints'

        if not user_input:
            return JsonResponse({'response': 'Please provide user input'})

        # Assuming you have configured and imported the genai module correctly
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

        convo = model.start_chat(history=[])
        convo.send_message(user_input)
        processed_response = convo.last.text

        # Split the response by '@' and add numbers (1), (2), (3), etc.
        processed_response_lines = processed_response.split('@')
        processed_response = ''
        processed_response += '1) Believe in yourself' 
        
        for i, line in enumerate(processed_response_lines, start=1):

            if i != 1:  # Skip adding "1)" before the first line
                processed_response += f'{i}) '
            processed_response += f'{line}<br>'

        print(processed_response)

        return render(request, 'roadmap.html', {'topic': topic, 'response': processed_response})
    else:
        return render(request, 'roadmap.html')
