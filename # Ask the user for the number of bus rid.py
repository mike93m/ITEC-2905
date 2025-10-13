
import requests

# Ask the user for a yes–no question
question = input("Ask the Magic 8 Ball a yes–no question: ")

# Prepare the API URL (encode the question for safe URL usage)
url = f"https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question.replace(' ', '%20')}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    answer = data.get("answer", "Hmm... the spirits are silent.")
    print("🎱 The Magic 8 Ball says:", answer)
else:
    print("Oops! Couldn't reach the Magic 8 Ball. Try again later.")