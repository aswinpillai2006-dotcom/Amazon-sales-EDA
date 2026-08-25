print("🏥 Welcome to the Medical Chatbot")
print("Enter a symptom: fever, cough, cold, headache")
print("Type 'exit' to quit.\n")

while True:
    symptom = input("Enter your symptom: ").lower()

    if symptom == "fever":
        print("You may have a fever. Rest, drink plenty of fluids, and monitor your temperature.")

    elif symptom == "cough":
        print("You have entered cough. Drink warm fluids and get adequate rest.")

    elif symptom == "cold":
        print("You may have a common cold. Rest, stay hydrated, and monitor your symptoms.")

    elif symptom == "headache":
        print("For a headache, rest in a quiet place, stay hydrated, and avoid excessive screen time.")

    elif symptom == "exit":
        print("Thank you for using the Medical Chatbot. Stay healthy!")
        break

    else:
        print("Sorry, I can only provide information for fever, cough, cold, or headache.")

    print("\n⚠️ If your symptoms are severe, persistent, or worrying, please consult a qualified doctor.\n")