# -*- coding: utf-8 -*-
"""Artikel blog (bahasa Inggris) dari unggahan Instagram @sekolahmutiarabali.
Satu entri = satu unggahan. Hanya fakta dari caption & gambar unggahan itu.
Gambar: src/assets/img/blog/<kunci>.jpg  (diambil dari unggahan sumber).
Tracker otomatis: content/blog-tracker.csv (dibuat oleh build.py)."""

IG = "https://www.instagram.com/sekolahmutiarabali/"

POSTS = [
    dict(
        code="Df9VkrsxMUU", kind="Reel", ts="2026-11-20T09:32:14Z", processed="2026-11-21",
        slug="paud-hajj-simulation",
        title="PAUD Mutiara Learns About the Hajj Through a Hands-On Simulation",
        meta="Playgroup and Kindergarten A children at PAUD Mutiara took part in a Hajj simulation, learning and practising the stages of the pilgrimage.",
        paras=[
            "PAUD Mutiara held a Hajj simulation (manasik haji) for children from Kindergarten A (TK A) and Playgroup (KB).",
            "With great enthusiasm and excitement, the children learned about the stages of the Hajj pilgrimage and practised them one by one, turning the lesson into a fun and meaningful learning experience.",
            "Through this activity, the school hopes to introduce the children to the Hajj, nurture their love of worship and instil religious values from an early age.",
            "Small steps today, building a foundation of goodness for tomorrow.",
        ],
        imgs=[("paud-hajj-simulation-1", "Young PAUD Mutiara students in light-blue uniforms and headscarves lined up outdoors during the Hajj simulation, with the title “Manasik Haji, TK A & KB”")],
        note="Reel: only the cover image and caption could be reviewed; the video footage itself was not described.",
    ),
    dict(
        code="Df9UeDrFxDF", kind="Photo", ts="2026-11-20T09:20:32Z", processed="2026-11-21",
        slug="jhs-theater-rri-pro-1-denpasar",
        title="Mutiara JHS Theater Goes Live on RRI PRO 1 Denpasar with “Jemputan yang Tak Kunjung Datang”",
        meta="Four Mutiara junior high students perform “Jemputan yang Tak Kunjung Datang” live on RRI PRO 1 Denpasar on Sunday, 22 November 2026.",
        paras=[
            "A stage, a story and voices full of confidence: Mutiara School students are ready to showcase their creativity and courage through the JHS Theater of Mutiara School.",
            "On the Idola Anak programme, the students will present the radio drama “Jemputan yang Tak Kunjung Datang”, broadcast live on RRI PRO 1 Denpasar. Listeners can look forward to a performance filled with storytelling, imagination and expression.",
            "Tune in and support their performance!",
        ],
        facts=[
            ("Performers", "Amira Aisyah Sodikin (Grade 7 Kaizen), Ni Made Naraya Aulia Ramadhani D. (Grade 7 Keizen), Amirah Laksmi Fitriani (Grade 8 Bung Tomo), Kinan Mutiara Aziz (Grade 7 Leadership)"),
            ("Host", "Lili Lintang, RRI PRO 1 host"),
            ("Date", "Sunday, 22 November 2026"),
            ("Time", "11:00–11:50 AM WITA"),
            ("Where to listen", "RRI PRO 1 Denpasar, FM 105.2 MHz, or stream via RRI Digital"),
        ],
        imgs=[("jhs-theater-rri-1", "Poster for the Idola Anak JHS Theater of Mutiara School, showing four students in white headscarves, host Lili Lintang and the broadcast details for 22 November 2026")],
        note="Class name is written “Kaizen” and “Keizen” in the caption; kept as written.",
    ),
    dict(
        code="Df85C-eRz-d", kind="Reel", ts="2026-11-20T05:21:12Z", processed="2026-11-21",
        slug="friday-reminder-spread-kindness",
        title="A Friday Reminder from Mutiara School: Keep Spreading Kindness",
        meta="Mutiara School’s Friday message: never tire of doing good, even through the smallest acts, and keep spreading kindness.",
        paras=[
            "Kindness always finds its way back to us. So never grow tired of doing good, even through the smallest and simplest acts.",
            "Keep spreading kindness, stay sincere and be a source of happiness for others. Every good deed has value in the sight of Allah.",
            "The reel carries the message: “Think good thoughts, act kindly and pray for good things, and Allah will surely reward you with the best,” together with the verse “Is the reward for good anything but good?” (QS Ar-Rahman: 60).",
            "May this Friday remind us all to keep improving ourselves and to increase our good deeds. Blessed Friday, and keep spreading kindness!",
        ],
        imgs=[("friday-kindness-1", "A Mutiara student wearing headphones reads aloud from a book, with a Friday message and a verse from Surah Ar-Rahman written above")],
        note="Reel: cover text was translated from Indonesian; the video footage itself was not described.",
    ),
    dict(
        code="Df8sdACl3W4", kind="Photo", ts="2026-11-20T03:31:12Z", processed="2026-11-21",
        slug="world-childrens-day-2026",
        title="Happy World Children’s Day 2026 from Mutiara School",
        meta="On World Children’s Day, 20 November 2026, Mutiara School celebrates every child as a precious gift with unique dreams and endless potential.",
        paras=[
            "Happy World Children’s Day! On 20 November 2026, Mutiara School joined the celebration with a simple message: every child deserves to be loved, protected and given the chance to dream.",
            "Every child is a precious gift, carrying unique dreams, endless potential and the hope of a brighter future. Children deserve to grow up in a world filled with love, kindness, safety and opportunities to discover their potential.",
            "Let us work together to create an environment where every child feels valued, heard and supported to become the best version of themselves. Because every child matters, and every childhood deserves to be filled with happiness and beautiful memories.",
        ],
        imgs=[("world-childrens-day-1", "World Children’s Day 2026 poster from Mutiara School showing four smiling young students in a green field under a bright sky")],
    ),
    dict(
        code="Df6XF0Nl6zO", kind="Carousel", ts="2026-11-19T05:45:48Z", processed="2026-11-21",
        slug="grade-6-scientific-proposal-presentations",
        title="Exploring Ideas, Inspiring Discovery: Grade 6 Scientific Proposal Presentations",
        meta="On 12 November 2026, Grade 6 students at Sekolah Mutiara presented their scientific proposals, building critical thinking and confidence.",
        paras=[
            "Grade 6 students at Sekolah Mutiara presented their scientific proposals on 12 November 2026, under the theme “Exploring Ideas, Inspiring Discovery”.",
            "Working in groups in front of their classmates, the students shared their ideas, explored topics that interested them and practised thinking critically and creatively. One group’s slides, for example, were about making tempeh.",
            "The activity encouraged the students to build confidence, communicate their ideas clearly and take their first steps towards scientific discovery.",
            "May their curiosity keep inspiring meaningful learning and new discoveries.",
        ],
        imgs=[
            ("grade-6-science-1", "A Grade 6 girl in a beige headscarf speaks and gestures during her scientific proposal presentation, under the title “Exploring Ideas, Inspiring Discovery”"),
            ("grade-6-science-2", "Groups of Grade 6 students stand in front of a projected slide about tempeh making while presenting their proposal"),
            ("grade-6-science-3", "Two groups of Grade 6 students take turns presenting beside a projected slide in their classroom"),
            ("grade-6-science-4", "Grade 6 students read from their notes as they present to the class"),
        ],
        note="Carousel of 10 images; 4 used in the article.",
    ),
    dict(
        code="Df3aM5Jyrv7", kind="Reel", ts="2026-11-18T02:15:39Z", processed="2026-11-21",
        slug="new-student-observation-and-interview",
        title="Getting to Know Our Future Students: Observation and Interview Day",
        meta="Mutiara School held observation and interview sessions for prospective students on 14 November 2026 as part of new student admissions.",
        paras=[
            "Mutiara School held an observation and interview session for prospective students on 14 November 2026 as part of the new student admission process.",
            "The sessions gave the school a chance to get to know each prospective student more closely, including their potential, character and readiness to begin their learning journey at Mutiara School.",
            "Every child is unique and has extraordinary potential. Together with Mutiara School, let’s grow into a generation that is smart, virtuous and visionary!",
        ],
        imgs=[("observation-interview-1", "A young boy plays with colourful blocks and a bead maze at a table during the observation session, with the text “14 November 2026, Observasi & Wawancara”")],
        note="Reel: date taken from the cover text; the video footage itself was not described.",
    ),
    dict(
        code="Df1eR72x0tw", kind="Reel", ts="2026-11-17T08:12:22Z", processed="2026-11-21",
        slug="why-parents-choose-mutiara-school",
        title="Why Parents Choose Mutiara School",
        meta="In a new video, Mutiara School parents share why they chose the school. Watch it on Instagram and register your child today.",
        paras=[
            "“A parent’s trust, a child’s brighter future.” In this video, titled “Mengapa Ayah Bunda memilih Sekolah Mutiara” (Why parents choose Sekolah Mutiara), parents share their story with the school.",
            "Through every story and experience, Mutiara School is inspired to keep growing and to provide the best education for every child. Thank you for being part of the Mutiara School family!",
            "To hear the parents in their own words, watch the full video on Instagram.",
            "Ready, Set, Grow! Mutiara School, the School of Leaders.",
        ],
        imgs=[("why-parents-choose-1", "Black-and-white photo of a father and mother standing outside the school building, with the title “Mengapa Ayah Bunda memilih Sekolah Mutiara”")],
        note="Reel: what the parents say is only in the video audio, which could not be reviewed, so it is not quoted.",
    ),
    dict(
        code="Df0zxPdF6ot", kind="Carousel", ts="2026-11-17T02:00:58Z", processed="2026-11-21",
        slug="munaqosyah-2026",
        title="Munaqosyah 2026: Growing with the Qur’an at Sekolah Mutiara",
        meta="Sekolah Mutiara held its Munaqosyah 2026 on Friday, 6 November 2026, where students showed their Qur’an recitation and memorisation.",
        paras=[
            "Alhamdulillah, Sekolah Mutiara successfully held its Munaqosyah 2026 on Friday, 6 November 2026, under the theme “Growing with the Qur’an”.",
            "The occasion gave students the opportunity to demonstrate their Qur’anic knowledge, recitation and memorisation, showing the results of their learning and dedication.",
            "May this experience strengthen the students’ love for the Holy Qur’an and inspire them to keep learning, practising and applying its teachings in daily life, growing into a generation with strong faith, noble character and a deep connection to the Qur’an.",
            "Proud of every step, inspired by every achievement!",
        ],
        imgs=[
            ("munaqosyah-2026-1", "A boy wearing a black cap and headphones reads from the Qur’an during Munaqosyah 2026"),
            ("munaqosyah-2026-2", "Teachers speak into microphones while students in white clothing sit on the floor holding copies of the Qur’an"),
            ("munaqosyah-2026-3", "Six students wearing headphones read and recite during the Munaqosyah"),
        ],
        note="Carousel of 9 images; 3 used in the article.",
    ),
    dict(
        code="DfzFtapkj-w", kind="Photo", ts="2026-11-16T09:59:07Z", processed="2026-11-21",
        slug="paud-outing-bali-zoo-2026",
        title="Mutiara Kindergarten Outing 2026: Off to Bali Zoo!",
        meta="PAUD Mutiara’s November 2026 outing takes the little explorers to Bali Zoo to discover wildlife and make memories with friends.",
        paras=[
            "Coming soon: the Mutiara Kindergarten Outing 2026, “Melali lan Melajah Sareng PAUD Mutiara ke Bali Zoo” (travelling and learning together with PAUD Mutiara at Bali Zoo).",
            "In November 2026 it is time for an exciting adventure filled with fun, discovery and new experiences. On this outing to Bali Zoo, our little explorers will discover fascinating wildlife, spark their curiosity and create wonderful memories with their friends.",
            "Because every adventure is an opportunity to learn, explore and grow!",
            "Want to experience the excitement of our outings? Come and be part of the Mutiara School family. Stay tuned for next year’s adventures and register your child today. Bilingual classes have limited seats, for Preschool, Primary School and Junior High School.",
        ],
        imgs=[("paud-outing-bali-zoo-1", "Purple poster for the PAUD Mutiara outing to Bali Zoo in November 2026, with three young students riding a rhinoceros among other zoo animals")],
        register=True,
    ),
    dict(
        code="Dfmk3L4klde", kind="Photo", ts="2026-11-11T13:21:12Z", processed="2026-11-21",
        slug="sd-outing-2026",
        title="Mutiara Elementary School Outing 2026: Fun, Friends and Field Trips",
        meta="In November 2026, Mutiara Elementary students go on educational field trips to Secret Garden, Bali Zoo, Bedugul Asri and The Sila’s.",
        paras=[
            "Learning doesn’t always have to happen inside the classroom. There is so much to discover through exciting journeys, new experiences and meaningful moments together.",
            "In November 2026, Mutiara Elementary School students will enjoy educational field trips to several interesting destinations: Secret Garden, Bali Zoo, Bedugul Asri and The Sila’s.",
            "Every journey brings new experiences, every moment together creates a story and every adventure becomes a beautiful memory to cherish. Fun, friends and field trips: making memories together!",
            "Want to experience the excitement of our outings? Come and be part of the Mutiara School family. Stay tuned for next year’s adventures and register your child today.",
        ],
        imgs=[("sd-outing-1", "Red poster for the SD Mutiara outing in November 2026, with two smiling students waving from the window of a yellow school bus")],
        register=True,
    ),
]

POSTS.sort(key=lambda p: p["ts"], reverse=True)
