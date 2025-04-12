from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"  # Replace with your actual key

BUILDING_LAYOUT = """
S   Washroom   Office     Office     Office    Storage     S
S   Lab        Corridor   Lab        Lab       Corridor    S
S   Storage    Office     Lab        Kitchen   Storage     S
S   Office     Office     Washroom   Lab       Corridor    S
Exit  Lab      Corridor   Corridor   Kitchen   Office      S
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/navigate", methods=["POST"])
def navigate():
    try:
        data = request.get_json()
        start = data.get("start")
        end = data.get("end")

        if not start or not end:
            return jsonify({"error": "Both locations are required"}), 400

        prompt = f"""Act as an indoor navigation system. Use this building layout:
        
        {BUILDING_LAYOUT}
        
        Provide step-by-step directions from {start} to {end}. 
        Mention specific rooms, turns, and landmarks. 
        Keep instructions clear and concise."""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert indoor navigation assistant"},
                {"role": "user", "content": prompt}
            ]
        )

        return jsonify({
            "directions": response.choices[0].message.content,
            "layout": BUILDING_LAYOUT
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)