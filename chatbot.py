import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    """Load and preprocess the MedQuAD dataset."""
    print("Loading MedQuAD dataset...")
    df = pd.read_csv('medquad.csv')
    
    # Fill missing values
    df['question'] = df['question'].fillna('')
    df['answer'] = df['answer'].fillna('No detailed answer available for this entry.')
    return df

def main():
    df = load_data()

    # Index dataset questions using TF-IDF
    print("Indexing dataset questions for text retrieval...")
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['question'])

    DISCLAIMER = (
        "\n" + "="*60 + "\n"
        "DISCLAIMER:\n"
        "This information is for educational purposes only and is not a\n"
        "substitute for professional medical advice. Please consult a qualified doctor."
        "\n" + "="*60
    )

    print("\n" + "*"*50)
    print("      MedQuAD Medical QA Chatbot Ready!")
    print("*"*50)
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("\nExiting chatbot. Stay healthy!")
            break

        if not user_input:
            continue

        # Convert user query and compare similarity with all dataset questions
        query_vec = vectorizer.transform([user_input])
        similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

        best_match_idx = similarities.argmax()
        best_score = similarities[best_match_idx]

        print("\nChatbot:")
        # Check if score meets minimum similarity threshold
        if best_score < 0.2:
            print("I'm sorry, I couldn't find a relevant answer to your question in the database.")
        else:
            answer = df.iloc[best_match_idx]['answer']
            print(answer)

        # Display required medical disclaimer
        print(DISCLAIMER)

if __name__ == "__main__":
    main()