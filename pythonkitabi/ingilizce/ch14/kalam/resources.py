"""
resources.py - application resources

copyright: (C) 2001, Boudewijn Rempt
email:     boud@rempt.xs4all.nl
"""

TRUE=1
FALSE=0

# Pixmaps drawn  by Mark Donohoe for the K Desktop Environment 
#  See http://www.kde.org 

filequit=[
    "22 22 7 1",
    "# c #000000",
    "e c #808080",
    "b c #dcdcdc",
    "a c #ffffff",
    "d c #a0a0a4",
    "c c #dcdcdc",
    ". c None",
    "......................",
    "......................",
    "......................",
    "......................",
    "......................",
    "........#####.........",
    "......##aaaaa##.......",
    ".....#aabbbbbbb#......",
    "....c#abbb#bbbb#d.....",
    "....#abbbb#bbbbd#.....",
    "....#abbbb#bbbbd#d....",
    "....#abbbb#bbbbd#d....",
    "....#abbbb#bbbbd#d....",
    "....#abbbb#bbbbd#d....",
    ".....#bbbb#bbbd#ed....",
    ".....#bbbbbbbdd#d.....",
    "......##ddddd##dd.....",
    ".......d#####ddd......",
    ".........ddddd........",
    "......................",
    "......................",
    "......................"]


filenew=[
    "10 14 5 1",
    " 	c None",
    ".	c #000000",
    "+	c #FFFFFF",
    "@	c #DCDCDC",
    "#	c #C0C0C0",
    ".......   ",
    ".++++@@.  ",
    ".++++#+@. ",
    ".++++#++@.",
    ".++++#....",
    ".+++++###.",
    ".++++++++.",
    ".++++++++.",
    ".++++++++.",
    ".++++++++.",
    ".++++++++.",
    ".++++++++.",
    ".++++++++.",
    ".........."]

filesave=[
    "    14    14        3            1",
    ". c #040404",
    "# c #808304",
    "a c #bfc2bf",
    "..............",
    ".#.aaaaaaaa.a.",
    ".#.aaaaaaaa...",
    ".#.aaaaaaaa.#.",
    ".#.aaaaaaaa.#.",
    ".#.aaaaaaaa.#.",
    ".#.aaaaaaaa.#.",
    ".##........##.",
    ".############.",
    ".##.........#.",
    ".##......aa.#.",
    ".##......aa.#.",
    ".##......aa.#.",
    "a............."
    ]

fileopen=[
    "    16    13        5            1",
    ". c #040404",
    "# c #808304",
    "a c #bfc2bf",
    "b c #f3f704",
    "c c #f3f7f3",
    "aaaaaaaaa...aaaa",
    "aaaaaaaa.aaa.a.a",
    "aaaaaaaaaaaaa..a",
    "a...aaaaaaaa...a",
    ".bcb.......aaaaa",
    ".cbcbcbcbc.aaaaa",
    ".bcbcbcbcb.aaaaa",
    ".cbcb...........",
    ".bcb.#########.a",
    ".cb.#########.aa",
    ".b.#########.aaa",
    "..#########.aaaa",
    "...........aaaaa"
    ]

editcut=[
"22 22 7 1",
"# c #a0a0a4",
"a c #585858",
"b c #303030",
"d c #dcdcdc",
"e c #ffffff",
"c c #c0c0c0",
". c None",
"......................",
"......................",
"......................",
"......................",
"....#aba#.............",
"....bccca#.....ab#....",
"....accccb...#abaa#...",
"....#aacaa..#aba#.....",
".....#bab#.#ab#.......",
".......#aaaba#........",
"..aaaaaaaada#aaaaaa...",
".......#baaaaeeeeed...",
".....#aaa#.#dd#.......",
"....#abcba..daba#.....",
"....accccb..e#abab#...",
"....bccca#.e...aa#....",
"....#aba#..e..........",
"...........d..........",
"...........e..........",
"......................",
"......................",
"......................"]

editpaste=[
"22 22 4 1",
"# c #000000",
"a c #ffffff",
"b c #c0c0c0",
". c None",
"......................",
"......................",
"......................",
"......................",
"......................",
".........####.........",
".....#####aa#####.....",
"....#bbb#a##a#bbb#....",
"....#bb#aaaaaa#bb#....",
"....#bb########bb#....",
"....#bbbbbb#######....",
"....#bbbbbb#aaaa##....",
"....#bbbbbb#aaaa#a#...",
"....#bbbbbb#a##a###...",
"....#bbbbbb#aaaaaa#...",
"....#bbbbbb#a####a#...",
".....#######aaaaaa#...",
"...........########...",
"......................",
"......................",
"......................",
"......................"]

editcopy=["22 22 4 1",
"# c #000000",
"a c #ffffff",
"b c #c0c0c0",
". c None",
"......................",
"......................",
"......................",
"......................",
"......................",
"....######............",
"....#aaaa##...........",
"....#aaaa#a#..........",
"....#a##a#######......",
"....#aaaab#aaaa##.....",
"....#a#####aaaa#a#....",
"....#aaaab#a##a####...",
"....#a#####aaaaaaa#...",
"....#aaaab#a#####a#...",
"....#######aaaaaaa#...",
"..........#a#####a#...",
"..........#aaaaaaa#...",
"..........#########...",
"......................",
"......................",
"......................",
"......................"]

editredo=["16 16 70 2",
"Qt c None",
".8 c #000000",
".3 c #000001",
".6 c #010003",
".7 c #020005",
".5 c #03080a",
".X c #03090a",
".S c #030c0b",
".L c #040b06",
".T c #041714",
"#d c #050a0c",
"#. c #050b0c",
"#a c #050d0e",
".F c #050e0d",
".Y c #071112",
".E c #081914",
"#c c #090f10",
".Q c #0a1910",
".M c #0a1f18",
".y c #0b281e",
".R c #0d2419",
".N c #0d3525",
".D c #0f2417",
".4 c #10211f",
".G c #123926",
"#b c #142724",
".9 c #14311f",
".v c #143120",
".z c #143d29",
".o c #153220",
"## c #162d26",
".i c #163321",
".u c #173a23",
".b c #1b4029",
".c c #1b422a",
".x c #1e4335",
".# c #1e472e",
".g c #214a30",
".t c #224b30",
".h c #224b31",
".l c #227d37",
".a c #234e33",
".n c #245135",
".U c #259039",
".O c #2a8f3d",
".q c #2f9645",
".H c #36a34d",
".w c #38774e",
".r c #3bb057",
".V c #3e9951",
".A c #3faf57",
".B c #42b75b",
".s c #43ba5c",
".2 c #468166",
".Z c #55ae72",
".1 c #5aa77b",
".0 c #5ab975",
".C c #7ba08a",
".J c #88ab9c",
".k c #90bd9f",
".I c #9dc6aa",
".d c #afbeba",
".W c #b2d1bc",
".p c #bdcec7",
".j c #bfd0c8",
".m c #c0d1c9",
".f c #c1cecc",
".K c #c2dbca",
".P c #cfe0d4",
".e c #dbeadf",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.#.#.aQtQtQtQtQtQtQtQt",
"QtQtQt.b.c.d.e.f.g.hQtQtQtQtQtQt",
"QtQt.i.j.k.l.l.l.e.m.gQtQtQtQt.n",
"Qt.o.p.l.l.q.r.s.l.l.e.tQtQt.n.u",
"Qt.v.l.w.x.y.y.z.A.B.l.e.g.n.C.u",
".D.l.n.EQtQtQtQt.F.G.H.l.I.J.K.u",
".L.l.MQtQtQtQtQtQtQt.N.H.l.O.P.u",
".Q.R.SQtQtQtQtQtQtQt.T.l.U.V.W.u",
"Qt.X.YQtQtQtQtQtQt.E.l.Z.0.1.2.u",
"Qt.3.4.5QtQtQtQt.6.6.6.7.6.6.8.9",
"QtQt#.##.FQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQt#a#b#cQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQt.3#d.3QtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]

editundo=["16 16 70 2",
"Qt c None",
".4 c #000000",
".9 c #000001",
".5 c #010003",
".6 c #020005",
".7 c #03080a",
".2 c #03090a",
".U c #030c0b",
".P c #040b06",
".T c #041714",
"#d c #050a0c",
"## c #050b0c",
"#c c #050d0e",
".I c #050e0d",
".1 c #071112",
".J c #081914",
"#a c #090f10",
".W c #0a1910",
".O c #0a1f18",
".z c #0b281e",
".V c #0d2419",
".N c #0d3525",
".K c #0f2417",
".8 c #10211f",
".H c #123926",
"#b c #142724",
".3 c #14311f",
".C c #143120",
".y c #143d29",
".u c #153220",
"#. c #162d26",
".n c #163321",
".o c #173a23",
".h c #1b4029",
".g c #1b422a",
".A c #1e4335",
".a c #1e472e",
".c c #214a30",
".p c #224b30",
".b c #224b31",
".k c #227d37",
".# c #234e33",
".i c #245135",
".S c #259039",
".M c #2a8f3d",
".s c #2f9645",
".G c #36a34d",
".B c #38774e",
".r c #3bb057",
".R c #3e9951",
".x c #3faf57",
".w c #42b75b",
".q c #43ba5c",
".X c #468166",
".0 c #55ae72",
".Y c #5aa77b",
".Z c #5ab975",
".v c #7ba08a",
".E c #88ab9c",
".l c #90bd9f",
".F c #9dc6aa",
".f c #afbeba",
".Q c #b2d1bc",
".t c #bdcec7",
".m c #bfd0c8",
".j c #c0d1c9",
".d c #c1cecc",
".D c #c2dbca",
".L c #cfe0d4",
".e c #dbeadf",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt",
"QtQtQtQtQtQtQtQt.#.a.aQtQtQtQtQt",
"QtQtQtQtQtQt.b.c.d.e.f.g.hQtQtQt",
".iQtQtQtQt.c.j.e.k.k.k.l.m.nQtQt",
".o.iQtQt.p.e.k.k.q.r.s.k.k.t.uQt",
".o.v.i.c.e.k.w.x.y.z.z.A.B.k.CQt",
".o.D.E.F.k.G.H.IQtQtQtQt.J.i.k.K",
".o.L.M.k.G.NQtQtQtQtQtQtQt.O.k.P",
".o.Q.R.S.k.TQtQtQtQtQtQtQt.U.V.W",
".o.X.Y.Z.0.k.JQtQtQtQtQtQt.1.2Qt",
".3.4.5.5.6.5.5.5QtQtQtQt.7.8.9Qt",
"QtQtQtQtQtQtQtQtQtQtQt.I#.##QtQt",
"QtQtQtQtQtQtQtQtQtQt#a#b#cQtQtQt",
"QtQtQtQtQtQtQtQt.9#d.9QtQtQtQtQt",
"QtQtQtQtQtQtQtQtQtQtQtQtQtQtQtQt"
]

editfind = ['16 16 12 1',
'. c None',
'# c #000000',
'i c #004041',
'd c #008183',
'b c #00c2c5',
'h c #00ffff',
'g c #313031',
'a c #5a595a',
'e c #838183',
'j c #c5c2c5',
'c c #c5ffff',
'f c #ffffff',
'....###.......a.',
'..##bcb##.......',
'.#dcccccd#...ee.',
'.#ccfffcc#..eaaa',
'#bcfffcccb#.aaag',
'#ccffccccc#..gg.',
'#bcfcccccb#.....',
'.#ccccccc#......',
'.#dcccccd#h.....',
'..##bcb##b##....',
'....###.i#aj#...',
'..a......#gaj#..',
'....a.....#gaj#.',
'.ee........#gaj#',
'eaaa.a......#ga#',
'aaag.........##.'
    ]
