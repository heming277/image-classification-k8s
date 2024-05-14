from django.shortcuts import render
from django.http import JsonResponse
import torch
from torchvision import transforms
from PIL import Image
import io
from .model import Net  # Use relative import
import os
# Load the trained model
model = Net()
model_path = os.path.join(os.path.dirname(__file__), '../model.pth')
model.load_state_dict(torch.load(model_path))  
model.eval()

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Define the class names
classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def index(request):
    return render(request, 'classifier/index.html')

def predict(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        img = Image.open(file)

        # Convert image to RGB if it has an alpha channel
        if img.mode != 'RGB':
            img = img.convert('RGB')

        img = transform(img).unsqueeze(0)
        with torch.no_grad():
            outputs = model(img)
            _, predicted = torch.max(outputs, 1)
            class_name = classes[predicted.item()]
        return JsonResponse({'class': class_name})
    return JsonResponse({'error': 'Invalid request'}, status=400)