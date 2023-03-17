from django.shortcuts import render
from django.http import HttpResponse
import tensorflow as tf
import os
import tensorflow_text as text

# Get the current working directory of the Python script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the SavedModel directory
model_dir = os.path.join(base_dir, 'BigBert')

# Load the SavedModel
reloaded_model = tf.saved_model.load(model_dir)


def home(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        try:
            input_text = tf.constant([input_text])
            score = int(tf.sigmoid(reloaded_model(input_text).numpy()[0][0]) * 9 + 1)
            score = round(score)
            context = {'input_text': input_text.numpy()[0].decode(), 'score': score}
            return render(request, 'home.html', context)
        except ValueError as e:
            error_message = f"Could not evaluate the review: {str(e)}"
            context = {'error_message': error_message}
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html') 