flaskHeroku

Testing out using flask and heroku to make a simple RESTful backend.  I will try to consume it with a Dart Webapp. 
Here is the site: http://enigmatic-hamlet-9450.herokuapp.com/


Ok, it turns out that the .dart file gets compiled into a .js file.
Flask, I think, loads up the files in static at launch and then doesn't look at the directory again.
So this means the .js is never loaded and  I get 404.  

This is not documented anywhere in either flask or dart.  I had to look at the network logs.
I changed the dart.js to have the static/prepended and then I realized what the issue was. 

I'm going to move this project to using JS, because Dart is a poo turd pile.  

Dart and Flask combine their powers into a hairy drooling T-Rex.  
