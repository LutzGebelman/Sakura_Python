import youtube_dl, os, sys
def play(url):
    if url.find("youtube") != -1:
        ydl_opts = {'format': 'bestaudio',
            'simulate': 'true',
            'forceurl': 'true',
        }
        
        with open('songname.txt', 'w') as f:
            sys.stdout = f
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            sys.stdout = original_stdout
            
            soundfile = open('songname.txt', 'r')
            result = soundfile.readlines()
            return result

            
    elif url.find("spotify") != -1:
        return url
         
    else: print("service is not supported")

def remove(final_link):
    os.remove(final_link)

original_stdout = sys.stdout