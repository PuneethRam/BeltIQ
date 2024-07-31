# BeltIQ

This project aims to build a system that can predict the condition of ropes and belts in real-time, allowing us to take action to prevent failures and production loss.

Various sensors will be strategically deployed along the entire length of the conveyor system, providing comprehensive coverage.

In our approach, two types of predictive models will be used: 

MODULE 1 : Prediction based on past data. LSTM, a neural network architecture, excels in capturing temporal patterns and dependencies to understand the dynamic changes in the ropes and belt's condition over time.

MODULE 2: Prediction from live data. Random Forest, a machine learning model, adeptly handles non-linear relationships and intricate interactions, enabling accurate predictions of pulley wear and tear by modeling the impact of environmental variables (e.g., temperature, load, humidity, and operational hours).


This is test file Step-by-Step Code Execution Instructions:

Clone the repository.
Open the terminal
Run the command " pip install -r requirements.txt"
Run the command "python manage.py makemigrations"
Run the command "python manage.py migrate"
Run the command "python manage.py runserver"
The server would have been started at your local host http://127.0.0.1:8000/.
