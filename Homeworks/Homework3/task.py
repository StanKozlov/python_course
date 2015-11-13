class Song:
    def __init__(self, name, artist, album, album_position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = album_position
        self.duration = duration
        self.year = year
    def __repr__(self):
        song = 'Song \'%s\' by %s in %s, number %s, %s year, %s seconds' %(self.name, self.artist, self.album, self.position, self.year, self.duration)
        return song
    def __lt__(self, other): 
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False 
def import_songs(file_name):
    input_file = open(file_name, 'r')
    lines = input_file.readlines()
    song_list = []
    for i in lines:
        name, artist, album, position, year, duration = i.split('\t')
        song_list.append(Song(name, artist, album, position, year, duration))
    return song_list
def export_songs(songs, file_names):
    songs_list = import_songs(songs)
    with open(file_names, "w") as export_file:
        for song in songs_list:
            export_file.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (song.name, song.artist, song.album, song.position, song.year, song.duration))


#Самый "частый" исполнитель
def finding_max(array):
    dictionary = {}
    for i in array:
        if i in dictionary:
            dictionary[i] +=1
        else:
            dictionary[i] = 1
    return dictionary

song_list = import_songs('songs1.txt')
artists = []
durations = []

for song in song_list:
    artists.append(song.artist)
    durations.append(int(song.duration))
    
dictionary = finding_max(artists)
key_key =  max(dictionary, key = dictionary.get)
print(key_key)

#самая длинная песня
def finding_greatest(array):
    max_val = array[0]
    for i in array:
        if i > max_val:
            max_val = i
    return max_val

max_duration = finding_greatest(durations)
for song in song_list:
    if int(song.duration) == max_duration:
        print('%s\t%s' % (song.name, song.artist))
        break
#самый длинный альбом одного исполнителя
dictionary_albums = {}
for song in song_list:
    title = '%s\t%s' %(song.album, song.artist)
    if title in dictionary_albums: 
        dictionary_albums[title] += int(song.duration)
    else:
        dictionary_albums[title] = int(song.duration)
print(max(dictionary_albums, key = dictionary_albums.get))


#топ 10 слов
new_dictionary = {}
dictionary = {}
for song in song_list:
    line = song.name.lower().split(' ')
    new_dictionary = finding_max(line)
    for key in new_dictionary:
        if key in dictionary:
            dictionary[key] += new_dictionary[key]
        else:
            dictionary[key] = new_dictionary[key]
words = []
top_words = []
sorted_d = sorted(dictionary.items(), key = lambda x: x[1])
top = len(sorted_d)
if top > 10:
    top_words = sorted_d[top-10:top]
else:
    top_words = sorted_d
words = [(tup[0]) for tup in top_words]
string = ''
for word in words[:len(words)-1]:
    string += '%s\t' % (word)
    
string += '%s\t' % words[len(words)-1]
string = string.replace((')' or '"' or "'" or ',' or '.' or '('), '')
print(string)

#Автор с наибольшим количеством альбомов
author_albums = {}
titles_dict = {}
for song in song_list:
    title = '%s\t%s' %(song.album, song.artist)
    if song.artist not in author_albums:
        author_albums[song.artist] = 1
        titles_dict[title] = 1
    else:
        if title not in titles_dict:
            author_albums[song.artist] += 1
        else:
            author_albums[song.artist] = 1
print(max(author_albums, key = author_albums.get))

def filter_songs(songs, word):
    good_songs = []
    word = word.lower() #чтобы не отметать капс
    for song in songs:
        if word in song.artist or word in song.name.lower():
            good_songs.append(song)
    return good_songs






