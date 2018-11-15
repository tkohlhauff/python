import praw
import config
import time
import os
from bs4 import BeautifulSoup
import requests


#Int to limit the amount of comments the bot will search through at a time
commentLimit = 25

#To stream comments from the subreddit constantly use this: .stream.comments()

#The string that the bot will look for (what the Reddit user will type)
botString = "!pullthatupjamie"


#Logs the JamieJREBot account into Reddit
def bot_login():
    print "Logging in..."
    handle = praw.Reddit(username = config.username,
                             password = config.password,
                             client_id = config.client_id,
                             client_secret = config.client_secret,
                             user_agent = "TexasForever_'s JamieJREBot comment responder v1.0")
    print ("Logged in!")
                             
    return handle


#The work of the bot meaning writing the comment and doing the work
def run_bot(handle, comments_replied_to):
    print "Obtaining comments..."
    for comment in handle.subreddit('test').stream.comments():
        
        if botString in comment.body.lower() and comment.id not in comments_replied_to and comment.author != handle.user.me():
        	#Adds the comment ID to a txt file so it won't repeat comments
            comments_replied_to.append(comment.id)
            print "String with \"" + botString + "\" found! in comment " + comment.id
            print "Replied to comment " + comment.id

            #Writes to the file
            with open ("comments_replied_to.txt", "a") as f:
            	f.write(comment.id + "\n")
            
        	
        	try:
        		check_search(comment)
        		comment_body = create_search(comment)

        		results = search_yt(comment_body)

        		x = 0
        		for title in results[0]:
        			results[0][x] = fix_result(title)
        			x += 1

        		comment.reply("Here's a few videos that I found, Joe: \n\n" +
        				"Title | Length\n" +
        				"---|---\n" +
        				"[" + results[0][0] + "](" + results[1][0] + ") | " + results[2][0] + "\n" +
        				"[" + results[0][1] + "](" + results[1][1] + ") | " + results[2][1] + "\n" +
        				"[" + results[0][2] + "](" + results[1][2] + ") | " + results[2][2] + "\n\n"
        				+ "I am a bot.")

        	except:
        		comment.reply("Either there were no results or your search wasn't in quotations!"
        			+ "\n\nI am a bot.")




def get_saved_comments():
    #Checks if there is a .txt named "comments_replied_to.txt". If it doesn't exist, it creates it.
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
        
    return comments_replied_to


def search_yt(comment):
    link = []
    title = []
    length = []
    yt_page = requests.get("https://www.youtube.com/results?search_query=" + comment)
    
    if yt_page.status_code < 400 and yt_page.status_code >= 200:
        soup = BeautifulSoup(yt_page.content, 'html.parser')
        soup.prettify()
		
        x = 0
        for a in soup.find_all('a',class_=" yt-uix-sessionlink spf-link "):
            x += 1
            if x < 4:
                link.append("https://www.youtube.com"+a['href'])
				
        x = 0
        for a in soup.find_all('a',class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "):
            x += 1
            if x < 4:
                title.append(a['title'])
				
        x = 0
        for a in soup.find_all('span',class_="video-time"):
            x += 1
            if x < 4:
                length.append(a.string)
				
        yt_results = [title,link,length]
		
    return yt_results


def create_search(comment):
    comment_body = list(comment.body.split('\"',1)[1].split('\"')[0])
    x = 0
    for char in comment_body:
        if char == " ":
            comment_body[x]="+"
        elif char =="(":
            comment_body[x]="%28"
        elif char ==")":
            comment_body[x]="%29"
        x += 1
    comment_body = ''.join(comment_body)

    return comment_body

def check_search(comment):
	comment_body=list(comment.body)
	x = 0
	for char in comment_body:
		if char == '\"':
			x += 1
	if x<2:
		raise Exception
	
def fix_result(comment):
	comment_body = list(comment)
	x = 0
	for char in comment_body:
		if char == "|":
			comment_body[x]="-"

		x += 1
	comment_body = ''.join(comment_body)

	return comment_body

	
handle = bot_login()
comments_replied_to = get_saved_comments()


while True:
    run_bot(handle, comments_replied_to)
