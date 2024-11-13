
#main character
define b = Character("Budi")
#konglomerat, pengutang, bos
define pt = Character("Pak Tono")
#rina
define r = Character("Rina")
define ibu = Character("Ibu Rina")
define mama = Character("Ibu Budi")

default pekerjaan_sampingan = False
default energy = True
default utang = 100000
default pt_affection = 0
default hari_ke = 0


image bg kamargf = "KamarGF.png"
image bg kamarrl = "KamarReal.png"
image bg kotagf = "KotaGF.png"
image bg kotarl = "KotaReal.png"

label start:

    # Intro story disini
    "Pada suatu hari yang cerah Budi bangun pagi seperti biasa setelah mendengar panggilan mendesak dari Ibu Rina"

    mama "Bud! Bud!..  ada yang nyariin kamu tuh didepan"

    b "Seriusan mah??!"

    "Budi pun berjalan menghampiri jendela, Budi berpikir untuk melihat siapa mencarinya"

    b "Waduh siapa iih!!!? Gak kenal!!!!?"

    "Budi berencana untuk menemuinya. Budi pun bergegas membuka pintu rumah"

    "??????" "Apakah benar ini Rumah Budi"

    "......."

    $ hari_ke += 1
    jump bedroom
    
    label bedroom:
        scene bg kamargf
        menu:
            "Sekarang Akan Melakukan Apa?"
            
            "Cari Kerja" if pekerjaan_sampingan == False:
                jump carikerja
            
            "Kerja" if pekerjaan_sampingan and energy:
                jump kerja
            
            "Judi":
                jump Judi
            
            "Istirahat" if energy == False:
                $ hari_ke += 1
                $ energy = True
                scene black
                b "aduh cape euy, istirahat dulu"
                if hari_ke == 7:
                    jump End
                else:
                    jump bedroom
            
            "Bayar Utang" if hari_ke >= 6:
                jump End







label carikerja:
    "Budi Berjalan ke sebuah Taman Kota yang indah"

    "Budi Menemukan brosur tentang lowongan perkerjaan yang ditempel di tiang listrik"

    b "setelah menemmukan brosur tersebut, budi kembali pulang ke rumah"

    b "di rumah budi berkata akan mendatangi lokasi lowongan tersebut yang berlokasi di depok"

    "setelah sampai di kantor budi melakukan wawancara dengan HRD, lalu budi diterima kerja setelah melakukan wawancara"
    $ pekerjaan_sampingan = True
    jump kerja

label Judi:
    "Budi pun pergi ke suatu tempat...."

    b "hehehe"
    jump bedroom

label kerja:
    "heheh"
    $ energy = False
    $ pt_affection += 1
    $ utang -= 5000
    jump bedroom

label End:
    "end Game"

return