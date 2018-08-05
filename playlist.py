playlist = {
    'title': 'love song',
    'author' : 'kerry parrt',
    'song' : [
        {'title':'song1','artist':['kerry'],'duration':2.4},
        {'title':'song2','artist':['kerry1'],'duration':4},
        {'title':'song3','artist':['kerry2'],'duration':3.4}
    ]
}

total = 0
for song in playlist['song']:
    total += song['duration'];
print(total)