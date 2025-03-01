import streamlit as st
import random

st.set_page_config(page_title="Whoop Whoop", page_icon="👑", layout="wide",
                   initial_sidebar_state="auto") #menu_items=True

# little fun at the beginning of the month (it's a meme)
st.video("https://www.youtube.com/watch?v=tAhK0oyC-4o")
st.divider()

# header
st.markdown("# Happy Birthday, Sascha!! 👑")
st.markdown("*... Also zumindest nachträglich ✨🎈*")


# birthday image
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDJub3JrMHF0YXdxcm5mcGp1bDVkc2dtMmJ1cmlpeXNoMThvMXhmZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wGKrkvHxZT6PVpw635/giphy.gif")
with col2:
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzN1cjkxM20zandwcHkzcGRiaTZibjluNGVzcmF1bmJwcDhhY3NpdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.gif")
with col3:
    st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjViY2JvNWRuMnV4eTB1OGphanN1ampyY2l2ejVyaDlsemgzNWFpeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/31VVbt1NFZ2B2Et8hY/giphy.gif")

st.divider()


# b-day wishes
st.markdown("## Lieber Sascha,")
st.markdown("### Herzlichen Glückwunsch zu Deinem Geburtstag (nachträglich)! ✨")
st.markdown("Wir wünschen Dir von ganzem Herzen:")
st.markdown("* ❤  Gesundheit (ganz, ganz wichtig!)\n"
            "* 😁 Zufriedenheit\n"
            "* 💸💸💸 viel Geld natürlich, für ...\n"
            "* ... weitere tolle Reisen und Abenteuer ✈🌎\n"
            "* 🥊 so wenig Stress auf der Arbeit wie möglich 🥋\n"
            "* den ganzen Kram wie Liebe, Erfolg, Glück, langes Leben ✨\n"
            "* ✨ 'und natürlich die Erfüllung Deiner Wünsche!' ,  mein Standart-Satz ✨"
            )

st.divider()


# birthday song
st.video("https://www.youtube.com/watch?v=HQ5EsTLFJxw")
st.markdown("![Hab' eine schöne Feier!](https://www.youtube.com/watch?v=HQ5EsTLFJxw)")

st.divider()

#even more fun!
st.markdown("### More Fun ✨✨")

# some lists
sprueche = [
    "Alles Gute zum Geburtstag! 🎂 Möge dein Jahr voller Glück und Freude sein!",
    "Herzlichen Glückwunsch! 🎈 Genieße deinen besonderen Tag in vollen Zügen!",
    "Happy Birthday! 🎁 Bleib gesund, glücklich und lass dich feiern!",
    "Heute ist dein Tag! 🎊 Lass es krachen und genieße jede Sekunde!",
    "Ein weiteres Jahr voller Abenteuer und Glück liegt vor dir! 🥳",
    "Geburtstage sind die perfekte Ausrede, um Kuchen zu essen! 🍰 Viel Spaß!",
    "Mögen alle deine Wünsche in Erfüllung gehen! ✨ Genieße deinen Ehrentag!",
    "Das Leben ist eine Reise – und Geburtstage sind schöne Zwischenstopps.",
]

meme_urls = [
    "https://a.pinatafarm.com/600x400/cda0b27da4/belated-birthday-a382d704c4c1510d45f8425b31f45bb2-meme.jpeg",
    "https://i.pinimg.com/736x/73/bf/f6/73bff648103271c9ab2a8e678db744c6.jpg",
    "https://i.pinimg.com/736x/db/71/74/db717479a2f01c905678394a71afb311.jpg",
    "https://i.pinimg.com/736x/0d/e6/fb/0de6fbcefb36f1b05400a224259689fc.jpg",
    "https://i.pinimg.com/736x/8f/ba/03/8fba03dc13709d2cc6d12c64f1bcf902.jpg",
    "https://i.pinimg.com/736x/98/2e/eb/982eeb2e215e5721e026c763215bd641.jpg",
    "https://i.pinimg.com/736x/22/a3/2a/22a32ad2272cd54f4278137428329e9c.jpg",
    "https://i.pinimg.com/736x/00/7f/ca/007fcaa2e1a0355260c7168e7e952a7e.jpg",
    "https://i.pinimg.com/736x/ea/07/6d/ea076de00fbcb46b87a67a693c809713.jpg",
    "https://i.pinimg.com/736x/64/48/1a/64481a34512682a068ddd0bb1ce1d41b.jpg",
    "https://i.pinimg.com/736x/d0/30/54/d030540970d341daab5e74d64bc387aa.jpg",
    "https://i.pinimg.com/736x/71/f0/02/71f002d6326fbdfd17ebf53f44f5445d.jpg",
    ]

# again some buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Spruch gefällig? 🎁"):
        spruch = random.choice(sprueche)
        st.subheader(f"💬 {spruch}")

with col2:
    if st.button("Effekt gefällig? 🎈"):
        st.balloons()

with col3:
    if st.button("🤣 Zeig mir ein Geburtstags-Meme!"):
        st.image(random.choice(meme_urls))

st.divider()
st.markdown("## 🎵 Ein letztes Lied zum Abschluss!")
st.video("https://www.youtube.com/watch?v=CZ9WIZxhodo")
