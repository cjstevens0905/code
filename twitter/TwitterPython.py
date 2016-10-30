import twitter
import urllib2
#loads my twitter user account into the code
user = 792015036235603968
#opens the twittercredentials into the code to access the twitter account
credentialsText = open("TwitterCredentials.txt")
#reads the credentials and splits it 
credentialsList = credstextfile.read().split('\n')

#opens up the user internet history through chrome
filename = open("/Users/Courtney/Library/Application Support/Google/Chrome/Default/Current Session")
myWebsites = filename.read()

#code finds the 'http' and last url in current internet history via google chrome
previousWebsite= myWebsites.rfind("http")

endOfURL = mywebsites.find(chr(0),previousWebsite)
lastURL = mywebsites[previousWebsite:endIndex]

lastURLhtmlFile = urllib2.urlopen(LastURL)
htmlRawText = lastURLhtmlFile.read()
titleStart = htmlRawText.find("<title>")
titleEnd = htmlRawText.find("</title>")

htmlTitle = html[StartIndex+7:EndIndex]

#twitter api
TAPI = twitter.Api(credentialsList[0],credentialsList[1],credentialsList[2],credentialsList[3])

#tweet uses the twitter api and the last url TITLE to post a "So Interesting" tweet onto twitter 
tweet = TAPI.PostUpdate("So Interesting " + str(htmlTitle))