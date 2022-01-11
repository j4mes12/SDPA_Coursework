"""
Name: James Stephenson
Section: Part 3
Description: This script contains the functions that we will be using to
extract the data from the spotify api. This includes the following functions:
- A function to get the album uris and names
- A function to get all the song uris in an album
- A function to extract the track features using a song uri
- A function that extracts the track audio features using the song uri
- A function that uses the previous functions to get all the track information
we desire for each track in the album.

"""


def get_album_uri_and_names(nr_data):
    """This function gets all the uris and ablum names from a new release
    requests and outputs it out as a tuple of two lists.

    ---Parameters---
    nr_data: dict
    dictionary of call requests from new_release spotipy method.

    ---Returns---
    (album_names, album_uri): tuple
    tuple of two lists. first list contains the album names of the request
    and the second contains the uris of the request.
    """

    # Get album names from api
    album_names = [album["name"] for album in nr_data["albums"]["items"]]

    # Get album uris from api
    album_uri = [album["uri"] for album in nr_data["albums"]["items"]]

    return (album_names, album_uri)


def get_song_uris_from_album(album_uri, sp):
    """Function to create list of the album song uris from the album's uri.

    ---Parameters---
    album: str
    string of the album uri

    sp: Spotify class
    A spotipy python library for the Spotify Web API


    ---Returns---
    song_uris: list
    list of song uris
    """

    # Get song uris for each song in album
    song_uris = [song["uri"] for song in sp.album_tracks(album_uri)["items"]]

    return song_uris


def get_track_features(input_dict, song_uri, sp, features):
    """Function that takes a song uri and adds the song information to an
    input dictionary.

    ---Parameters---
    input_dict: dict
    dictionary of the form {'feature1' : [...], 'feature2' : [...], ...}

    song_uri: str
    string of song uri

    sp: Spotify class
    A spotipy python library for the Spotify Web API

    features: list
    list of track features that we want to extract from the Spotify API


    ---Returns---
    input_dict: dict
    dictionary containing the song information of the album uri
    """

    # Get track information from api
    sp_track = sp.track(song_uri)

    # Loop through all track features and extract information
    # In some cases, these features are within dicitonary values
    for k in features:
        if k == "album":
            input_dict[k].append(sp_track["album"]["name"])
        elif k == "popularity":
            input_dict[k].append(sp_track["popularity"])
        elif k == "artist":
            input_dict[k].append(sp_track["album"]["artists"][0]["name"])
        elif k == "release_date":
            input_dict[k].append(sp_track["album"][k])
        else:
            input_dict[k].append(sp_track[k])

    return input_dict


def get_audio_features(input_dict, song_uri, sp, features):
    """Function that adds audio feature information to an input dictionary
    from a specified song uri

    ---Parameters---
    input_dict: dict
    dictionary of the form {'feature1' : [...], 'feature2' : [...], ...}

    song_uri: str
    strinf of the song uri

    sp: Spotify class
    A spotipy python library for the Spotify Web API

    features: list
    list of audio features that we want to extract from the Spotify API


    ---Returns---
    input_dict: dict
    dictionary containing the song information of the album uri
    """

    # Get audio features from api
    audio = sp.audio_features(song_uri)[0]

    # Loop through all features we want and extract them from the api
    for k in features:

        # Catch missing values so they can be dealt with later
        if audio is None:
            input_dict[k].append(None)
        else:
            input_dict[k].append(audio[k])

    return input_dict


def get_album_info(album_uri, sp, track_features, audio_features):
    """Function that gets all the song information features from a specified
    album uri.

    ---Parameters---
    album_uri: str
    string of an album uri

    album_names: str
    strong of the album name

    sp: Spotify class
    A spotipy python library for the Spotify Web API

    track_features: list
    list of track features that we want to extract from the spotify api

    audio_features: list
    list of audio features that we want to extract from the spotify api


    ---Returns---
    track_info: dict
    dictionary of the form {'feature1' : [...], 'feature2' : [...], ...}
    """

    track_info = {k: [] for k in track_features + audio_features}

    # Get uri for each song in album
    nr_song_uris = get_song_uris_from_album(album_uri, sp)

    # Loop through these uri and get features for each one
    for song_uri in nr_song_uris:

        track_info = get_track_features(
            track_info, song_uri, sp, track_features
        )

        track_info = get_audio_features(
            track_info, song_uri, sp, audio_features
        )

    return track_info
