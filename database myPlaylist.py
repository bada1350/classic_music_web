from pymongo import MongoClient

connection = MongoClient('mongodb+srv://carl1350:pcRfM3Rm6ryaf9TX@cluster0.96iktkk.mongodb.net/?retryWrites=true&w=majority')
db = connection.classicMusic

music = db.musics

Beethoven = {
    "order": 1,
    "title": "베토벤",
    "intro1": "\"베토벤의 음악은 보편적이다. 전 세계 어디를 가더라도 그의 음악은 모든 사람에게 통한다.\" - 다니엘 바린보임",
    "intro2": "루트비히 판 베토벤(Ludwig van Beethoven)의 작품을 감상해봅시다.",
    "href": "beethoven",
    "content": [
        "베토벤 교향곡 1번",
        "베토벤 교향곡 2번",
        "베토벤 교향곡 3번",
        "베토벤 교향곡 4번",
        "베토벤 교향곡 5번",
        "베토벤 교향곡 6번",
        "베토벤 교향곡 7번",
        "베토벤 교향곡 8번",
        "베토벤 교향곡 9번"
    ],
    "src": [
        "https://www.youtube.com/watch?v=H8OgDIovJJQ&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=1",
        "https://www.youtube.com/watch?v=4Ba8cEJD814&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=2",
        "https://www.youtube.com/watch?v=C_LNI77aTjc&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=3",
        "https://www.youtube.com/watch?v=lk_Uq_RSOcA&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=4",
        "https://www.youtube.com/watch?v=oZjPpylRW74&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=5",
        "https://www.youtube.com/watch?v=BnojPN5AeXs&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=6",
        "https://www.youtube.com/watch?v=GFAxXMximZo&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=7",
        "https://www.youtube.com/watch?v=BTZL7gerBqA&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=8",
        "https://www.youtube.com/watch?v=tuFeGKIlAVs&list=PLuC1jRip8DLaFgaabyns0UrXYUoFe9W4L&index=9"
    ]
}

Mozart = {
    "order": 2,
    "title": "모차르트",
    "intro1": "\"이 소년은 나중에 우리 모두를 잊히게 할 것이다.\" - 요한 아돌프 하세",
    "intro2": "볼프강 아마데우스 모차르트(Wolfgang Amadeus Mozart)의 작품을 감상해봅시다.",
    "href": "mozart",
    "content": [
        "피아노 소나타 1번 C장조, K.279",
        "피아노 소나타 2번 F장조, K.280",
        "피아노 소나타 3번 Bb장조, K.281",
        "피아노 소나타 4번 Eb장조, K.282",
        "피아노 소나타 5번 G장조, K.283",
        "피아노 소나타 6번 D장조, K.284",
        "피아노 소나타 7번 C장조, K.309",
        "피아노 소나타 8번 A단조, K.310",
        "피아노 소나타 9번 D장조, K.311",
        "피아노 소나타 10번 C장조, K.330",
        "피아노 소나타 11번 A장조, K.331",
        "피아노 소나타 12번 F장조, K.332",
        "피아노 소나타 13번 Bb장조, K.333",
        "피아노 소나타 14번 C단조, K.457",
        "피아노 소나타 15번 F장조, K.533/494",
        "피아노 소나타 16번 C장조, K.545",
        "피아노 소나타 17번 Bb장조, K.570",
        "피아노 소나타 18번 D장조, K.576"
    ],
    "src": [
        "https://www.youtube.com/watch?v=ZixdOZh7zo4&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=1",
        "https://www.youtube.com/watch?v=J9866zX07iw&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=2",
        "https://www.youtube.com/watch?v=xRCGxDeKTTM&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=3",
        "https://www.youtube.com/watch?v=VAZay7fgnWA&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=4",
        "https://www.youtube.com/watch?v=c4_R6z6FHeg&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=5",
        "https://www.youtube.com/watch?v=6TJTGOj03cU&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=6",
        "https://www.youtube.com/watch?v=D95g_FU5cU0&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=7",
        "https://www.youtube.com/watch?v=bZZqSZqJz4Y",
        "https://www.youtube.com/watch?v=BsDMfSrylZM&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=9",
        "https://www.youtube.com/watch?v=31Q1bgpaF18&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=10",
        "https://www.youtube.com/watch?v=x7Pd2OqxfnU&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=11",
        "https://www.youtube.com/watch?v=wXhm-C_mb_k&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=12",
        "https://www.youtube.com/watch?v=9lLaHB7eGKc&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=13",
        "https://www.youtube.com/watch?v=CKtxbloW-ZQ&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=14",
        "https://www.youtube.com/watch?v=tk9fa1CTY9k&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=15",
        "https://www.youtube.com/watch?v=HmkVBf01XhQ&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=16",
        "https://www.youtube.com/watch?v=kVwEkgQ3dPs&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=17",
        "https://www.youtube.com/watch?v=rUgMSF49YE4&list=PL2XuErO9rJH4yyI37FM5QgUPDlDw3vw4T&index=18"
    ]
}

Bach = {
    "order": 3,
    "title": "바흐",
    "intro1": "\"마치 날개라도 달린 듯 그의 발은 페달 위를 날아다녔고, 힘찬 소리가 천둥처럼 교회안에 쩌렁쩌렁 울려펴졌다.\" - 콘스탄틴 벨러만",
    "intro2": "요한 제바스티안 바흐(Johann Sebastian Bach)의 작품을 감상해봅시다.",
    "href": "bach",
    "content": [
        "무반주 첼로 모음곡 1번 G장조 BWV 1007",
        "무반주 첼로 모음곡 2번 d단조 BWV 1008",
        "무반주 첼로 모음곡 3번 C장조 BWV 1009",
        "무반주 첼로 모음곡 4번 E♭장조 BWV 1010",
        "무반주 첼로 모음곡 5번 c단조 BWV 1011",
        "무반주 첼로 모음곡 6번 D장조 BWV 1012"
    ],
    "src": [
        "https://www.youtube.com/watch?v=UuQZ8VuZTSA&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=1",
        "https://www.youtube.com/watch?v=dxMSoEeOOOU&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=2",
        "https://www.youtube.com/watch?v=QYZU3HHWaLE&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=3",
        "https://www.youtube.com/watch?v=LivsP2dUce0&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=4",
        "https://www.youtube.com/watch?v=gMIJslhMwZ8&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=5",
        "https://www.youtube.com/watch?v=gG2Py1XBXew&list=PL4lU1D8c_L_yvEWGCtqTbd_W_-gPiEx20&index=6"
    ]
}

Chopin = {
    "order": 4,
    "title": "쇼팽",
    "intro1": "\"쇼팽은 그의 모든 인생을 피아노에 바쳤고, 우리 피아니스트들은 그를 피아노의 절대, 절대신이라고 생각합니다. 그는 그 어떤, 그 어느 작곡가보다도 훨씬 더 피아노와 밀접하게 연관되어 있습니다.\" - 아르투르 루빈스타인",
    "intro2": "프레데리크 쇼팽(Frédéric Chopin)의 작품을 감상해봅시다.",
    "href": "chopin",
    "content": [
        "쇼팽 녹턴 Op. 9, 1번",
        "쇼팽 녹턴 Op. 9, 2번",
        "쇼팽 녹턴 Op. 9, 3번",
        "쇼팽 녹턴 Op. 15, 1번",
        "쇼팽 녹턴 Op. 15, 2번",
        "쇼팽 녹턴 Op. 15, 3번",
        "쇼팽 녹턴 Op. 27, 1번",
        "쇼팽 녹턴 Op. 27, 2번",
        "쇼팽 녹턴 Op. 32, 1번",
        "쇼팽 녹턴 Op. 32, 2번",
        "쇼팽 녹턴 Op. 37, 1번",
        "쇼팽 녹턴 Op. 37, 2번",
        "쇼팽 녹턴 Op. 48, 1번",
        "쇼팽 녹턴 Op. 48, 2번",
        "쇼팽 녹턴 Op. 55, 1번",
        "쇼팽 녹턴 Op. 55, 2번",
        "쇼팽 녹턴 Op. 62, 1번",
        "쇼팽 녹턴 Op. 62, 2번",
        "쇼팽 녹턴 Op. 72, 1번"
    ],
    "src": [
        "https://www.youtube.com/watch?v=WnFs85pLmj4&list=PL552450E1514256AB&index=1",
        "https://www.youtube.com/watch?v=Nu48Z45ibxQ&list=PL552450E1514256AB&index=2",
        "https://www.youtube.com/watch?v=sx31YcLXAug&list=PL552450E1514256AB&index=3",
        "https://www.youtube.com/watch?v=waoKj8tAb7A&list=PL552450E1514256AB&index=4",
        "https://www.youtube.com/watch?v=u-vmSSkFdwE&list=PL552450E1514256AB&index=5",
        "https://www.youtube.com/watch?v=L1w2_2WG5q4&list=PL552450E1514256AB&index=6",
        "https://www.youtube.com/watch?v=8lvNjO3TQAA&list=PL552450E1514256AB&index=7",
        "https://www.youtube.com/watch?v=E_2PjSzZO9o&list=PL552450E1514256AB&index=8",
        "https://www.youtube.com/watch?v=U92QEmtR63E&list=PL552450E1514256AB&index=9",
        "https://www.youtube.com/watch?v=ttLRonyyMak&list=PL552450E1514256AB&index=10",
        "https://www.youtube.com/watch?v=9PB3bYaWosM&list=PL552450E1514256AB&index=11",
        "https://www.youtube.com/watch?v=ymouzrzzgZ0&list=PL552450E1514256AB&index=12",
        "https://www.youtube.com/watch?v=h_vZtpjNKVE&list=PL552450E1514256AB&index=13",
        "https://www.youtube.com/watch?v=nqEk73LvnzQ&list=PL552450E1514256AB&index=14",
        "https://www.youtube.com/watch?v=NONg06Pf0v8&list=PL552450E1514256AB&index=15",
        "https://www.youtube.com/watch?v=MyVFBkHepRw&list=PL552450E1514256AB&index=16",
        "https://www.youtube.com/watch?v=2oYaEHzn6Kg&list=PL552450E1514256AB&index=17",
        "https://www.youtube.com/watch?v=zf8YUL_jlF0&list=PL552450E1514256AB&index=18",
        "https://www.youtube.com/watch?v=vJpAIOFN5WQ&list=PL552450E1514256AB&index=19"
    ]
}

Vivaldi = {
    "order": 5,
    "title": "비발디",
    "intro1": "\"그의 음악은 야성적이고 불규칙적이다.\" - 존 호킨스 경",
    "intro2": "안토니오 비발디(Antonio Vivaldi)의 작품을 감상해봅시다.",
    "href": "vivaldi",
    "content": [
        "협주곡 1번 마장조, 작품번호 8번, RV. 269 \"봄\" 1악장",
        "협주곡 1번 마장조, 작품번호 8번, RV. 269 \"봄\" 2악장",
        "협주곡 1번 마장조, 작품번호 8번, RV. 269 \"봄\" 3악장",
        "협주곡 2번 사단조, 작품번호 8번, RV. 315 \"여름\" 1악장",
        "협주곡 2번 사단조, 작품번호 8번, RV. 315 \"여름\" 2악장",
        "협주곡 2번 사단조, 작품번호 8번, RV. 315 \"여름\" 3악장",
        "협주곡 3번 바장조, 작품번호 8번, RV. 293 \"가을\" 1악장",
        "협주곡 3번 바장조, 작품번호 8번, RV. 293 \"가을\" 2악장",
        "협주곡 3번 바장조, 작품번호 8번, RV. 293 \"가을\" 3악장",
        "협주곡 4번 바단조, 작품번호 8번, RV. 297 \"겨울\" 1악장",
        "협주곡 4번 바단조, 작품번호 8번, RV. 297 \"겨울\" 2악장",
        "협주곡 4번 바단조, 작품번호 8번, RV. 297 \"겨울\" 3악장"
    ],
    "src": [
        "https://www.youtube.com/watch?v=aWNXGiENvvg&list=PL077764AA439803F2&index=1",
        "https://www.youtube.com/watch?v=mYQvLFuIZ5I&list=PL077764AA439803F2&index=2",
        "https://www.youtube.com/watch?v=C9thrT9EDNI&list=PL077764AA439803F2&index=3",
        "https://www.youtube.com/watch?v=BT5hVcE5YWg&list=PL077764AA439803F2&index=4",
        "https://www.youtube.com/watch?v=8QO7FAeLm0c&list=PL077764AA439803F2&index=5",
        "https://www.youtube.com/watch?v=zj-9k8LZ3pI&list=PL077764AA439803F2&index=6",
        "https://www.youtube.com/watch?v=Mt40j2QX8-s&list=PL077764AA439803F2&index=7",
        "https://www.youtube.com/watch?v=NFWf1EK1Y04&list=PL077764AA439803F2&index=8",
        "https://www.youtube.com/watch?v=7ZhOWFJgoGc&list=PL077764AA439803F2&index=9",
        "https://www.youtube.com/watch?v=UV5WTRLTPOU&list=PL077764AA439803F2&index=10",
        "https://www.youtube.com/watch?v=UstQF86Gj4E&list=PL077764AA439803F2&index=11",
        "https://www.youtube.com/watch?v=SUoFUBAtt94&list=PL077764AA439803F2&index=12"
    ]
}

Liszt = {
    "order": 6,
    "title": "리스트",
    "intro1": "\"나는 지금 내 펜이 무엇을 쓰고 있는지 모르겠네. 리스트가 지금 나의 연습곡을 연주하고 있는데, 그가 나의 머릿속의 생각을 날려버리고 있네. 그의 연주를 빼앗아오고 싶을 정도라네.\" - 프레데리크 쇼팽, 페르디난트 힐러에게 쓴 편지에서",
    "intro2": "프란츠 리스트(Franz Liszt)의 작품을 감상해봅시다.",
    "href": "liszt",
    "content": [
        "성 도로테아",
        "위안 2번",
        "위안 3번",
        "물 위를 걷는 파올라의 성 프란체스코",
        "회색 구름",
        "고독 속의 신의 축복",
        "장송곡",
        "슬픔의 곤돌라 1번",
        "꿈 속에서"
    ],
    "src": [
        "https://www.youtube.com/watch?v=-Tc7J368Dkw",
        "https://www.youtube.com/watch?v=G7Yo7u-O2QM",
        "https://www.youtube.com/watch?v=705LabZ1U88",
        "https://www.youtube.com/watch?v=-1L7eVj-u_Q",
        "https://www.youtube.com/watch?v=F1hEpDsnzTE",
        "https://www.youtube.com/watch?v=_v_Tz6BtH4I",
        "https://www.youtube.com/watch?v=zpuNjz9JMnE",
        "https://www.youtube.com/watch?v=Cp5nrxi6TfE",
        "https://www.youtube.com/watch?v=NKAqdL4rXc4"
    ]
}

music.insert_one(Beethoven)
music.insert_one(Mozart)
music.insert_one(Bach)
music.insert_one(Chopin)
music.insert_one(Vivaldi)
music.insert_one(Liszt)