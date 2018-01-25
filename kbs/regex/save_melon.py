import requests

def save():
    temp = requests.get('https://www.melon.com/chart/index.htm')
    f1 = open('melon.txt', 'wt')
    f1.write(temp.text)
    f1.close()

if __name__ == "__main__":
    save()