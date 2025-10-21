import io
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import json
import requests
from docxtpl import DocxTemplate
from datetime import datetime
from .models import Template


def main_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')

def template(request):
    if request.method == 'GET':
        templates = Template.objects.all()
        context = {
            'templates': templates
        }
        print(templates)
        return render(request, 'template_selection.html', context=context)
    
        

def build_page(request, name):
    if request.method == 'GET':
        template = Template.objects.get(name=name)
        if template != None:
            tpl_name = template.name
            tpl_inst = template.instruction
            context = {
                'name': tpl_name,
                'instruction': tpl_inst
            }
            return render(request, 'build_page.html', context=context)
        else:
            return HttpResponse(f"Template {tpl_name} not found!")
    elif request.method == 'POST':
        template = Template.objects.get(name=name)
        text = request.POST.get('prompt')
        if template != None:
            API_KEY = "AIzaSyCdRoWHiPiq0XrnPHjP2aw--i8eBfHT0-M"

            MODEL_NAME = "gemini-2.0-flash"
            API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

            headers = {
                "Content-Type": "application/json"
            }

            payload = {
                "contents": [{
                    "parts": [{
                        "text": template.prompt.replace("++%text%++", text)
                    }]
                }],
                "generationConfig": {
                    "responseMimeType": "application/json",
                    "temperature": 0.1,
                }
            }

            print("Sending request to Gemini API...")
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                
                response.raise_for_status() 
                
                response_data = response.json()
                
                content_text = response_data['candidates'][0]['content']['parts'][0]['text']
                print(content_text)
                context = json.loads(content_text)
                doc = DocxTemplate(template.word_doc.path)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                doc.render(context)
                buffer = io.BytesIO()
                doc.save(buffer)
                buffer.seek(0)
                return FileResponse(
                    buffer, 
                    as_attachment=True, 
                    filename= f"CV_{str(timestamp).replace(' ', '_')}.docx"
                )
            
            except requests.exceptions.RequestException as e:
                print(f"An HTTP error occurred: {e}")
                print(f"Response body: {response.text}")
                return HttpResponse(f"An HTTP error occurred: {e}\n\n\n Response body: {response.text}")
            
            except (KeyError, IndexError, json.JSONDecodeError) as e:
                print(f"Failed to parse the API response: {e}")
                print(f"Raw response content: {content_text}")
                return HttpResponse(f"Failed to parse the API response: {e}\n\n\nRaw response content: {content_text}")

        else:
            return HttpResponse(f"Template {tplID} not found!")

def thanks(request):
    return render(request, 'thanks.html')
