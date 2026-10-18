#Student-specific inputs
LAST_NAME = "Bautista"
STUDENT_ID = "TUPM-26-3506"
FAVORITE_ARTIST = "CONAN GRAY"

SEED_DIGIT = int(STUDENT_ID[-1])

ID_SUM = sum(
    int(ch)
    for ch in STUDENT_ID
    if ch.isdigit()
)

NAME_LENGTH = len(LAST_NAME)

ARTIST_LENGTH = len(
    FAVORITE_ARTIST.replace(" ", "")
)

ARTIST_SUM = sum(
    ord(ch) - 64
    for ch in FAVORITE_ARTIST.replace(" ", "")
)