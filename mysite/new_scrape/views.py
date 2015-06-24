from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy import create_engine
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import random

Base = automap_base()
metadata = MetaData()
engine = create_engine('postgresql://timothychung:submarine@localhost:5432/timothychung')
session = Session(engine)

Base.prepare(engine, reflect=True)
newComment = Base.classes.new_scrape_newcomment

def processBody(text):
   openBrackets = '{(['
   closeBrackets = '}])'
   punctuation = '.!?'
   quotations = '"'   

   myBody = text.replace('\n','<br>')
   newString = myBody[0]
   checkCounter = 0
   counter = 1
   bracketCounter = 0
   quoteCounter = 0
            
   while (checkCounter < 2) & (counter < len(myBody)):
         newString += myBody[counter]
         if myBody[counter] in quotations:
	    quoteCounter = (quoteCounter + 1) % 2
         elif myBody[counter] in openBrackets:
            bracketCounter += 1
         elif myBody[counter] in closeBrackets:
            bracketCounter = max(bracketCounter - 1, 0)
         elif (myBody[counter] in punctuation) & (quoteCounter == 0) & (bracketCounter == 0) & (myBody[counter-1] not in punctuation):
            checkCounter += 1
         counter += 1
  
   if quoteCounter == 1:
	 return newString + '"'
   else:
   	 return newString

def index(request):
    myQuery = session.query(newComment).filter(newComment.body != '[deleted]').filter(~newComment.body.like('%https://%')).filter(newComment.score_ratio > 0.7).filter(newComment.current_score >= 20)
    totalCount = random.randint(0, myQuery.count())
    selectItem = myQuery.slice(totalCount, totalCount + 1).all()[0]
    
    thisBody = processBody(selectItem.body)
    return HttpResponse(thisBody + '<br><br>' + selectItem.writer + '<br>' + \
			selectItem.subreddit + '<br>' + selectItem.write_time.isoformat() + \
			'<br><a href="' + selectItem.link +'">' + selectItem.link + '</a>')
# Create your views here.
