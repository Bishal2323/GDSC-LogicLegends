from flask import Flask, render_template, request, jsonify
import openai

# haha

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    user_input = data.get("text")

    if not user_input:
        return jsonify({"result": "No input provided."})

    blueprint = """
    S   Washroom   Office     Office     Office    Storage     S
    S   Lab        Corridor   Lab        Lab       Corridor    S
    S   Storage    Office     Lab        Kitchen   Storage     S
    S   Office     Office     Washroom   Lab       Corridor    S
    Exit  Lab      Corridor   Corridor   Kitchen   Office      S
    """

    prompt = f"""
    You are a navigation guide inside a building.

    Here is the room layout in a grid format:
    
    {blueprint}
    
    You will be given a user's current location and their desired destination.
    Your job is to clearly explain how to navigate from where they are to the destination step-by-step.

    User input: "{user_input}"

    Provide clear directions using the room names. Mention turns or path landmarks if useful.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful indoor navigation assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        output = response['choices'][0]['message']['content']
        return jsonify({"result": output})
    except Exception as e:
        return jsonify({"result": f"Error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
