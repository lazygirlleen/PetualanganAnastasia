# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg blck = "images/black.jpg"
image bg wht  = "images/white.jpg"
image bg frst  = "images/forest.png"
image bg vlg  = "images/village.png"
image a = "images/anastasia.png"
image am = "images/anastasiasmile.png"
image c = "images/carrot.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('...', color="#000000")
define a = Character('Anastasia', color="#f651ca")
define c = Character('Carrot-Chan', color="#d26c23")

# Game dimulai disini.
label start:
    play music "audio/In The Darkness.wav"
    scene bg blck with dissolve
    e "Selamat datang di dunia ini"

    e "Kamu adalah orang terpilih"
    menu:
        "Aku dimana?":
            jump explain
        "Wow keren":
            jump happy

label happy:
    e "Kamu orang yang unik"
    e "Selamat kamu diterima kerja"
    a "Hah..."
    
    "Welcome New Actor"
    "Ending 1/4"
    return

label explain:
    e "...."
    e "Kalau begitu selamat tinggal"
    a "Tunggu..."

    stop music
    
    scene bg wht with dissolve
    "Beberapa menit kemudian..."

    play music "audio/First Impression.wav"
    a "Duh aku dimana?"
    
    "Tanpa Anastasia sadari sosok yang terlihat seperti wortel menunggunya bangun"
    scene bg frst with dissolve
    show c at right
    c "Wah masih hidup ternyata"

    show a at left
    a "Emergency Food?"
    "Anastasia menangkap makhluk wortel tersebut"
    c "Aku bukan makanan!"
    a "Enaknya di sop atau tumis yah?"
    c "HEY AKU PUNYA TELINGA"
    a "Kamu tidak terlihat seperti punya"

    "Makhluk wortel tersebut menyadari sepertinya sedang bertemu seorang psikopat"

    c "Aku Wortel-chan, pemimpin suku wortel"

    a "Anak kecil"
    c "HEY"

    c "Ngomong-ngomong siapa namamu?"

    
    stop music

    menu:
        "Galactic Baseballer":
            jump baseball
        "I am the bone of my sword":
            jump sword
        "Panggil aku captain":
            jump captain

label baseball:
    play music "audio/Your Choice.wav"
    c "Rasanya familiar"
    a "Aku sudah menelusuri berbagai galaxy..."
    
    "Wortel-chan menyadari orang ini tidak hanya psikopat, tapi halu juga"

    a "Wortel-chan"
    c "Ya?"
    scene bg frst with dissolve
    show am
    a "Bagaimana kalau kita bertualang bersama menjelajah dunia ini?"
    c "Hey harusnya aku yang bertanya"
    a "Aku anggap itu jawaban iya. Sebagai kepala suku seharusnya kamu punya pengetahuan mendalam mengenai dunia ini"

    "Wortel-chan yang ketakutan hanya bisa mengggangguk setuju dan mengiyakan permintaan sang psikopat maksudnya Anastasia"

    stop music

    "The Journey Of Galactic Baseballer"
    "Ending 2/4"

    return

label captain:
    scene bg frst with dissolve
    play music "audio/Your Choice.wav"

    c "C-captain?"
    show am
    a "Iya, captain Hyperion"
    
    c "Nampak Familiar"
    a "Wah, kalau dipikir pikir kamu mirip kubis itu"
    c "....."
    a "Hey carrot-chan, apakah kamu punya kebun wortel?"
    c "Aku punya"
    a "Nah ayo kita pergi ke rumahmu dan memasak sup wortel. Tenang carrot-chan aku bisa masak kok"

    "Sebenarnya Carrot-chan tidak yakin, tapi dia tidak punya pilihan lain selain mengiyakan permintaan Anastasia"

    stop music

    "Cooking With Captain"
    "Ending 3/4"

    return

label sword:
    play music "audio/Your Choice.wav"

    "Anastasia berkata sambil mengeluarkan senjatanya"
    c "BENTAR BENTAR JANGAN SERANG AKU"
    a "Yah padahal akting ku tadi sudah bagus"
    
    "Carrot-chan berpikir psikopat ini nampaknya lebih gila dari dugaannya"

    a "Ayo kita pergi"
    c "Kemana?"
    a "Tentu saja ke desa wortel, kamu kan kepala sukunya. Ayo tunjukkan jalannya"

    scene bg wht with dissolve

    "Carrot-chan yang sudah pasrah hanya bisa mengangguk setuju dan menunjukkan jalan menuju desa wortel"

    scene bg vlg with dissolve

    show c at left
    c "Capek banget akhirnya sampai"
    show am at right
    a "Kamu masih muda sudah jompo saja"
    
    "Wow sindiran yang sangat bagus untuk kaum jompo muda dari Anastasia..."

    stop music

    "Old but not old"
    "Ending 4/4"

    return