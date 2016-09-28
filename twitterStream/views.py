from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render_to_response('twitterStream/index.html')

@csrf_exempt
def submit(request):	
    consumer_key = 'fW6SSlFxISDpR0QFffgxFkaAL'
    consumer_secret = 'nLvXICfe9nE1l1jX9lDy1a72o5BLfkcRp8HEXG2zysytE8oyC6'
    access_token = '763004532448194560-GkZDToyeX6XDrAYeb8PubrF9wPWUa7r'
    access_token_secret = 'ZNVKdfZsLIKmbz56wW1WOIeIsiY3SApHEeTHT6wWPREfg'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


    class MyListener(StreamListener):
 
        def on_data(self, data):
            try:
                with open('python.json', 'a') as f:
                    f.write(data)
                    return True
                #return data.text

            except BaseException as e:
                print(("Error on_data: %s") % str(e))
            return True
 
        def on_error(self, status):
            print(status)
            return True
 
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['python'], async=True)

    if request.method == "POST":
	    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	    from matplotlib.figure import Figure

	    fig=Figure()
	    ax=fig.add_subplot(111)
	    ax.plot(range(10), range(10), '-')
	    canvas=FigureCanvas(fig)
	    response=HttpResponse(content_type='image/png')
	    canvas.print_png(response)
	    return response
	    #return render(request, 'twitterStream/index.html')

