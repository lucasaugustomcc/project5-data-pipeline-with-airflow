class SqlQueries:
    user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    SELECT DISTINCT (user_id), first_name, last_name, gender, level
    FROM staging_events
    WHERE user_id IS NOT NULL AND page  =  'NextSong'
    """)

    song_table_insert = ("""
        INSERT INTO songs (song_id, title, artist_id, year, duration)
        SELECT DISTINCT (song_id), title, artist_id, year, duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        INSERT INTO artists (artist_id, name, location, latitude, longitude)
        SELECT DISTINCT(artist_id) as artist_id,
            artist_name as name,
            artist_location as location,
            nullif(artist_latitude,'') as latitude,
            nullif(artist_longitude,'') as longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        INSERT into time (start_time, hour, day, month, week, weekday, year)
            SELECT DISTINCT (TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second')
                as start_time,
            DATE_PART(hrs, start_time) as hour,
            DATE_PART(day, start_time) as day,
            DATE_PART(mon, start_time) as month,
            DATE_PART(w, start_time) as week,
            DATE_PART(dow, start_time) as weekday,
            DATE_PART(yrs , start_time) as year
            FROM staging_events
    """)

    songplay_table_insert = ("""
        INSERT INTO songplays (
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent
            )
        SELECT TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second' as start_time,
            se.user_id,
            se.level,
            s.song_id as song_id,
            a.artist_id as artist_id,
            se.session_id,
            se.location,
            se.user_agent
        FROM staging_events se
        JOIN songs s ON (se.song = s.title)
        JOIN artists a ON (se.artist = a.name)
    """)