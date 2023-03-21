import os
import openai
from flask import Flask, request, render_template_string

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
    <title>使用OpenAI生成信件內容</title>
    <style>
    body {
        font-family: 'Noto Sans', sans-serif;
        background-color: #E7ECEF;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        color: #274C77
    }
    .container {
        display: inline-block;
        text-align: left;
        background-color: white;
        padding: 1.875rem;
        border-radius: 0.625rem;
        flex-direction: column;
        align-items: stretch;
    }
    h1 {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 1.875rem;
    }
    input[type="text"], button {
        box-sizing: border-box;
    }
    input[type="text"] {
        height: 2.5em;
        border-radius: 0.3125rem;
        width: 100%;
        max-width: calc(100% - 1.25rem);
    }
    button {
        background-color: #A3CEF1;
        font-size: 1rem;
        color: #274C77;
        border-radius: 0.4375rem;
        cursor: pointer;
        padding: 0.3125rem 0.625rem;
    }
    form {
        position: relative;
        width: 100%;
    }
    label {
        font-size: 1rem;
    }
    pre {
        width: 100%;
        white-space: pre-wrap;
        word-wrap: break-word;
        background-color: white;
        overflow: auto;
    }
    h2 {
        text-align: center;
    }
    @media (max-width: 768px) {
        .container {
            width: 80%;
            display: block;
        }
    }
    @media (min-width: 769px) {
        .container {
            width: 40%;
        }
    }

</style>
</head>
<body>
    <div class="container">
        <h1>使用OpenAI生成信件內容</h1>
        <form method="post">
            <label for="sender">寄件人是誰：</label>
            <input type="text" id="sender" name="sender" required><br><br>
            <label for="recipient">收件人是誰：</label>
            <input type="text" id="recipient" name="recipient" required><br><br>
            <label for="subject">信件主題：</label>
            <input type="text" id="subject" name="subject" required><br><br>
            <button type="submit">生成信件內容</button>
        </form>
        {% if content %}
            <h2>生成的信件內容：</h2>
            <pre> {{content}} </pre>
        {% endif %}
    </div>
</body>
</html>
    '''
    
@app.route('/', methods=['GET', 'POST'])
def generate_letter():
        content = None
        if request.method == 'POST':
            sender = request.form['sender']
            recipient = request.form['recipient']
            subject = request.form['subject']
    
            prompts = f"1.請給我一封電子郵件內容，用繁體中文撰寫\n2.信件內容為{subject}\n3.信件最後需寫{sender}敬上，記得要獨立一行\n4.請從親愛的{recipient}開始撰寫\n"
            
            #使用davinci model每次生成2個回答（n=2)，並取用第一個回答（chioces[0])
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=prompts,
                max_tokens=300,
                n=2,
                stop=None,
                temperature=0.6,
            )
            content = response.choices[0].text.strip(" ")
    
        return render_template_string(template, content=content)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
