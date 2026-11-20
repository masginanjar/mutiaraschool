# -*- coding: utf-8 -*-
"""Konten 6 halaman dalam (about, programs, facilities, gallery, admissions, contact) x 3 bahasa.
Blok: ("text", h2, [paragraf]) | ("list", h2, intro, [butir]) | ("cards", h2, intro, [(h3, p)])
      ("facts", h2, [(angka, label)]) | ("split", h2, [paragraf], img_key, alt)
      ("level", id, nama, sub, deskripsi, [(label, nilai)], [butir], img_key, alt)
      ("steps", h2, [(h3, p)]) | ("faq", h2, [(q, a)]) | ("quote", teks, nama, jabatan)
      ("note", teks) | ("gallery",) | ("contact",)"""

SLUG = {
    "en": dict(about="about", programs="programmes", facilities="facilities", gallery="gallery", admissions="admissions", contact="contact"),
    "id": dict(about="tentang-kami", programs="program", facilities="fasilitas", gallery="galeri", admissions="pendaftaran", contact="kontak"),
    "ar": dict(about="about", programs="programmes", facilities="facilities", gallery="gallery", admissions="admissions", contact="contact"),
}
HERO_IMG = dict(about="g1", programs="x0", facilities="g3", gallery="g5", admissions="x2", contact="hero")

# Foto galeri tambahan (kunci -> alt per bahasa)
XALT = {
    "x0": dict(en="Junior high students and their teacher working on a laptop in class", id="Siswa SMP dan guru belajar bersama menggunakan laptop di kelas"),
    "x1": dict(en="Preschool children cheering with raised hands in the reading corner", id="Anak-anak PAUD bersorak mengangkat tangan di pojok baca"),
    "x2": dict(en="Pupils in red and white uniforms gathered outdoors in the morning", id="Siswa berseragam merah putih berkumpul di luar ruangan pada pagi hari"),
    "x3": dict(en="A teacher using hand puppets and stacking toys with preschool children", id="Guru memakai boneka tangan dan mainan susun bersama anak-anak PAUD"),
    "x4": dict(en="A teacher and primary pupils learning on a tablet in the library", id="Guru dan siswa SD belajar menggunakan tablet di perpustakaan"),
    "x5": dict(en="Two teachers helping pupils read at a table in the school library", id="Dua guru mendampingi siswa membaca di meja perpustakaan sekolah"),
    "x8": dict(en="A teacher and pupils making a felt craft together in class", id="Guru dan siswa membuat prakarya dari kain flanel di kelas"),
    "x9": dict(en="A teacher showing countries on a globe to three pupils", id="Guru menunjukkan negara pada globe kepada tiga siswa"),
    "x13": dict(en="A classroom lesson with pupils in scout uniform and two teachers at the whiteboard", id="Suasana belajar di kelas dengan siswa berseragam pramuka dan dua guru di papan tulis"),
    "x18": dict(en="Young scouts lined up beside their scout leader", id="Pramuka siaga berbaris di samping pembina pramuka"),
    "x19": dict(en="Scouts queuing on the school ramp during an activity", id="Siswa pramuka mengantre di tangga landai sekolah saat kegiatan"),
    "x20": dict(en="Scouts playing a team game with strings and bottles", id="Siswa pramuka bermain permainan kelompok dengan tali dan botol"),
    "x21": dict(en="Three girl scouts chatting and smiling on the school balcony", id="Tiga siswi pramuka berbincang dan tersenyum di balkon sekolah"),
    "x23": dict(en="Scouts seated together in the hall listening to a briefing", id="Siswa pramuka duduk bersama di aula mendengarkan pengarahan"),
    "x24": dict(en="Preschool children eating together at a long table", id="Anak-anak PAUD makan bersama di meja panjang"),
    "x25": dict(en="Children sitting in a row on the grass at an outdoor event", id="Anak-anak duduk berjajar di rumput saat kegiatan luar ruangan"),
    "x26": dict(en="Children doing movement exercises on the field in the evening", id="Anak-anak melakukan gerak dan lagu di lapangan pada sore hari"),
    "x28": dict(en="A guest instructor leading a movement activity with preschool children", id="Instruktur tamu memandu kegiatan gerak bersama anak-anak PAUD"),
}

P = {}

# ------------------------------------------------------------------ ENGLISH
P["en"] = dict(
    about=dict(
        title="About Us", meta_t="About Mutiara School Bali – History, Vision & Mission",
        meta_d="Learn how Mutiara School Bali began in Jimbaran in 2016, its vision and mission, and the values behind its character-based education.",
        intro="A school in Jimbaran that began with a simple conviction: bright children also need good character.",
        blocks=[
            ("split", "How it started", [
                "Mutiara School Bali was founded on 2 May 2016 by eight founders who shared one concern. They saw growing demand for quality schools in South Kuta, and they worried that lessons too often felt detached from children’s real lives.",
                "Their answer was a school backed by qualified teachers and a curriculum that shapes children who are intelligent, well-mannered and forward-looking. Building A went up soon after the foundation was legally established in 2016.",
                "Enrolment opened in March 2017 and classes began on 6 April 2017, first with preschool and then with primary school. Junior high followed as the school grew."], "g3",
             "Pupils forming a circle on the field in front of the school building"),
            ("photos", ["x1", "x4", "x21"]),
            ("facts", "Early growth", [("94", "students in 2017/2018"), ("199", "students in 2018/2019"), ("30 → 51", "teachers and staff, 2017 to 2018")]),
            ("text", "Why “Mutiara”", ["Mutiara means pearl. The name expresses the founders’ resolve to offer the best quality education, and their hope that every graduate leaves with strong results and noble character. The school motto sums it up: Cerdas, Berbudi, Visioner – bright, virtuous, visionary."]),
            ("cards", "Vision and mission", "Vision: to be an outstanding educational institution that prepares a bright, virtuous and globally minded generation.", [
                ("Professional institution", "Run the school professionally with a learning system that helps children thrive."),
                ("Academic and social excellence", "Shape a generation that excels academically and socially, grounded in religious values."),
                ("Partnership", "Work with every part of the education community to achieve national education goals.")]),
            ("quote", "Mutiara School is here in South Kuta as an education choice centred on character values. We hope our students grow into a generation that is strong, useful and able to lead with dignity – and we invite parents to walk in step with us.",
             "Lailatul Widayati, S.H., M.Pd.", "Director of Education"),
        ]),
    programs=dict(
        title="Programmes & Levels", meta_t="Programmes – Preschool, Primary & Junior High | Mutiara School Bali",
        meta_d="Preschool (PAUD), primary (SD) and junior high (SMP) at Mutiara School Bali: curriculum, school hours, class sizes, clubs and signature programmes.",
        intro="Three levels on one campus, each blending the National Curriculum with Mutiara’s own B.E.S.T curriculum in a full day school system.",
        blocks=[
            ("cards", "The B.E.S.T curriculum", "Alongside the National Curriculum, which assesses knowledge, skills, attitude and behaviour, every level follows four directions.", [
                ("Berkarakter · Character", "Discipline, independence, integrity, love of country and leadership."),
                ("Edukatif · Educative", "Quick learners with broad horizons, vision and curiosity."),
                ("Solutif · Solution-minded", "Able to solve problems for themselves, others and their community."),
                ("Terampil · Skilled", "Equipped with practical life skills.")]),
            ("level", "paud", "Preschool (PAUD)", "Playgroup, Kindergarten A and B",
             "Young children learn through play, exploration and daily good habits, in Indonesian with English practised in everyday activities.",
             [("Entry age", "Playgroup 3, Kindergarten A 4, Kindergarten B 5 (by July)"), ("Class", "Up to 25 children with 2 teachers"),
              ("Kindergarten hours", "Mon–Thu 07.45–13.00, Fri 07.45–11.00"), ("Playgroup hours", "Mon, Wed, Fri 08.00–11.00")],
             ["Entrepreneur: children sell items they bring from home on market days", "Explore Science: simple science presentations linked to the current theme",
              "Clubs: drawing, drum band, taekwondo, coding, Balinese dance", "Playgroup and kindergarten are both accredited"],
             "paud", "Two preschool girls cracking an egg during a cooking activity"),
            ("level", "sd", "Primary School (SD)", "Grades 1–6",
             "Primary years build a strong academic base while nurturing creativity, collaboration, leadership and an entrepreneurial spirit.",
             [("Entry age", "6 years by July of the school year"), ("Class", "Up to 28 pupils with 2 teachers"), ("Hours", "Mon–Thu 07.30–15.00, Fri 07.30–11.00")],
             ["Love of country and active care for local culture", "English and technology as everyday tools", "Optional Qur’an memorisation (tahfidz) class",
              "Clubs: scouts, pencak silat, swimming, futsal, choir, music, drawing, traditional dance"],
             "sd", "A teacher and two pupils exploring a globe in the library"),
            ("level", "smp", "Junior High School (SMP)", "Grades 7–9",
             "Teenagers learn actively and critically with varied methods and media, and are guided step by step towards independence and integrity.",
             [("Class", "Up to 25 students"), ("Hours", "Mon–Thu 07.30–16.30, Fri 07.30–16.00")],
             ["Signature programmes: Best Leadership Program, Business Day, Super Camp, Outing Class", "Reading culture, academic writing and project-based Qur’an study",
              "Self-development activities and care for the environment", "Clubs: scouts, pencak silat, archery, journalism, futsal, basketball, robotics, photography & graphic design, videography, science club, music, cooking, choir"],
             "smp", "Three junior high students working together on a tablet"),
            ("photos", ["x3", "x9", "x20"]),
            ("cards", "Qur’an memorisation (Tahfidz)", "An alternative class for students who wish to memorise faster, taught with the Wafa method.", [
                ("Preschool", "Target: 1 juz"), ("Primary", "Target: 3 juz"), ("Junior high", "Target: 2 juz")]),
            ("note", "School hours follow the school’s published information and may be adjusted each year. Please confirm the current timetable with our team."),
        ]),
    facilities=dict(
        title="Facilities", meta_t="Facilities – Mutiara School Bali, Jimbaran",
        meta_d="Air-conditioned classrooms, library, computer and language labs, sport centre, playgrounds, healthy canteen, transport and catering at Mutiara School Bali.",
        intro="A modern, child-friendly campus near Udayana University, designed so children feel safe, comfortable and free to explore.",
        blocks=[
            ("split", "Spaces for learning", ["Classrooms are air-conditioned and supported by a library, a computer and e-learning lab, a language lab, a multimedia room and a music room. Wi-Fi is available across the learning areas."], "x0",
             "Junior high students and their teacher working on a laptop in class"),
            ("cards", "What you will find on campus", "", [
                ("Learning", "Learning centre, air-conditioned classrooms, library, computer and e-learning lab, language lab, multimedia room."),
                ("Arts and worship", "Music room, prayer room and a dedicated tahfidz room."),
                ("Sport and play", "Sport centre and sports field, indoor and outdoor playgrounds."),
                ("Care and wellbeing", "Counselling room, school health room (UKS) and a healthy canteen."),
                ("Everyday convenience", "School shop, parking area, clean restrooms and Wi-Fi."),
                ("Learning hall", "A hall for assemblies, parent meetings and school events.")]),
            ("photos", ["x5", "g3", "x13"]),
            ("split", "Transport and catering", ["School transport and catering are available through the school cooperative. Families register directly with the cooperative, which also runs a student savings programme."], "g4",
             "Children splashing at the pool edge with a swimming instructor"),
            ("cards", "Online services", "The school runs its registration and academic systems online.", [
                ("Online enrolment", "Register from home through the enrolment form."),
                ("Academic system", "Parents and students can follow academic information online."),
                ("Online payment", "School payments can be made through the school’s payment system.")]),
        ]),
    gallery=dict(
        title="Gallery", meta_t="Photo Gallery – Mutiara School Bali",
        meta_d="Photos of daily life at Mutiara School Bali: classrooms, library, scouts, sports and school events in Jimbaran.",
        intro="Moments from classrooms, the library, the field and school events.",
        blocks=[("gallery",), ("note", "See more of our latest activities on Instagram and YouTube – links are on the Contact page.")]),
    admissions=dict(
        title="Admissions", meta_t="Admissions 2027/2028 – Mutiara School Bali",
        meta_d="How to enrol at Mutiara School Bali for 2027/2028: steps, entry requirements, documents, observation and interview. Enrol via WhatsApp.",
        intro="Enrolment for the 2027/2028 school year is open for preschool, primary and junior high. Transfer students are welcome.",
        blocks=[
            ("steps", "How to enrol", [
                ("Register online", "Fill in the enrolment form. You may also visit the school and our team will help you complete it."),
                ("Pay the registration fee", "The registration fee covers selection and observation."),
                ("Complete your data", "Upload your child’s details and documents online."),
                ("Observation and interview", "Held at the school: one day for preschool and primary, two days for junior high. Results are announced 2–3 days later.")]),
            ("photos", ["x2", "x8", "g6"]),
            ("cards", "Entry requirements", "", [
                ("Preschool", "Age 3 for Playgroup, 4 for Kindergarten A and 5 for Kindergarten B, by July of the school year."),
                ("Primary", "Age 6 by July of the school year, and in good physical and mental health."),
                ("Junior high", "Completed primary school (SD/MI), holds an NISN, and passes the academic test and interview.")]),
            ("list", "Documents to prepare", "", [
                "One 3×4 photo with a red background", "A copy of the birth certificate", "A copy of the family card (Kartu Keluarga)", "A copy of a parent’s or guardian’s ID card (KTP)",
                "Junior high only: legalised copies of grade 4–6 reports and a doctor’s health certificate"]),
            ("faq", "Common questions", [
                ("How much are the fees?", "Fees differ by level and intake period, so we do not list them here. Message us on WhatsApp and our team will send the current fee sheet."),
                ("Can fees be paid in instalments?", "Yes. Instalments are possible; parents sign a commitment form with the finance office."),
                ("Do you accept transfer students?", "Yes, from any school, as long as the administrative requirements are met."),
                ("What if we miss the interview date?", "The application is moved to the next intake period."),
                ("Can I register for a later school year?", "Yes. Register through the form, then confirm with us on WhatsApp.")]),
        ]),
    contact=dict(
        title="Contact", meta_t="Contact Mutiara School Bali – Jimbaran, Bali",
        meta_d="Address, WhatsApp, email, office hours and map for Mutiara School Bali, Jl. Lingkar Timur Udayana No. 8, Jimbaran, Bali.",
        intro="We are happy to answer questions and welcome families who would like to visit the campus.",
        blocks=[("contact",)]),
)

# ------------------------------------------------------------------ INDONESIA
P["id"] = dict(
    about=dict(
        title="Tentang Kami", meta_t="Tentang Mutiara School Bali – Sejarah, Visi & Misi",
        meta_d="Kenali awal berdirinya Mutiara School Bali di Jimbaran pada 2016, visi dan misinya, serta nilai di balik pendidikan karakternya.",
        intro="Sekolah di Jimbaran yang berangkat dari keyakinan sederhana: anak yang cerdas juga perlu berakhlak baik.",
        blocks=[
            ("split", "Awal perjalanan", [
                "Mutiara School Bali berdiri pada 2 Mei 2016, digagas delapan orang pendiri yang punya kegelisahan sama. Kebutuhan masyarakat Kuta Selatan akan sekolah bermutu terus tumbuh, sementara pelajaran di sekolah sering terasa jauh dari kehidupan nyata anak.",
                "Jawaban mereka adalah sekolah dengan guru yang mumpuni dan kurikulum yang membentuk anak cerdas, santun, dan berpikir ke depan. Gedung A mulai dibangun tidak lama setelah yayasan resmi berdiri pada 2016.",
                "Pendaftaran dibuka Maret 2017 dan kegiatan belajar dimulai 6 April 2017, diawali kelas PAUD lalu SD. Jenjang SMP menyusul seiring sekolah berkembang."], "g3",
             "Siswa membentuk lingkaran di lapangan depan gedung sekolah"),
            ("photos", ["x1", "x4", "x21"]),
            ("facts", "Pertumbuhan awal", [("94", "siswa pada 2017/2018"), ("199", "siswa pada 2018/2019"), ("30 → 51", "guru dan staf, 2017 ke 2018")]),
            ("text", "Mengapa “Mutiara”", ["Nama Mutiara mencerminkan tekad para pendiri untuk memberi pendidikan dengan mutu terbaik, sekaligus harapan agar setiap lulusan membawa prestasi dan akhlak mulia. Semboyan sekolah merangkumnya: Cerdas, Berbudi, Visioner."]),
            ("cards", "Visi dan misi", "Visi: menjadi lembaga pendidikan unggul yang menyiapkan generasi cerdas, berbudi luhur, dan berwawasan global.", [
                ("Lembaga profesional", "Mengelola sekolah secara profesional dengan sistem belajar yang kondusif."),
                ("Unggul akademik dan sosial", "Membentuk generasi yang unggul secara akademik dan cerdas secara sosial, berlandaskan nilai-nilai religius."),
                ("Kemitraan", "Bekerja sama dengan seluruh unsur pendidikan demi tercapainya tujuan pendidikan nasional.")]),
            ("quote", "Mutiara School hadir di Kuta Selatan sebagai pilihan pendidikan yang berpusat pada nilai karakter. Kami berharap siswa tumbuh menjadi generasi yang kuat, berdaya guna, dan mampu memimpin dengan bermartabat. Mari, Ayah Bunda, kita melangkah seirama.",
             "Lailatul Widayati, S.H., M.Pd.", "Direktur Pendidikan"),
        ]),
    programs=dict(
        title="Program & Jenjang", meta_t="Program PAUD, SD & SMP | Mutiara School Bali",
        meta_d="PAUD, SD, dan SMP di Mutiara School Bali: kurikulum, jam belajar, jumlah siswa per kelas, ekstrakurikuler, dan program khas tiap jenjang.",
        intro="Tiga jenjang dalam satu lingkungan, masing-masing memadukan Kurikulum Nasional dengan Kurikulum B.E.S.T khas Mutiara dalam sistem full day school.",
        blocks=[
            ("cards", "Kurikulum B.E.S.T", "Di samping Kurikulum Nasional yang menilai pengetahuan, keterampilan, sikap, dan perilaku, setiap jenjang mengikuti empat arah berikut.", [
                ("Berkarakter", "Disiplin, mandiri, berintegritas, cinta tanah air, dan berjiwa pemimpin."),
                ("Edukatif", "Cepat belajar, berwawasan luas, visioner, dan ingin tahu."),
                ("Solutif", "Mampu memecahkan masalah bagi diri sendiri, orang lain, dan masyarakat."),
                ("Terampil", "Dibekali kecakapan hidup yang praktis.")]),
            ("level", "paud", "PAUD", "Kelompok Bermain, TK A, dan TK B",
             "Anak belajar lewat bermain, bereksplorasi, dan pembiasaan baik, dengan bahasa Indonesia dan pembiasaan bahasa Inggris dalam kegiatan harian.",
             [("Usia masuk", "KB 3 tahun, TK A 4 tahun, TK B 5 tahun (per Juli)"), ("Kelas", "Maksimal 25 anak dengan 2 guru"),
              ("Jam TK", "Senin–Kamis 07.45–13.00, Jumat 07.45–11.00 WITA"), ("Jam KB", "Senin, Rabu, Jumat 08.00–11.00 WITA")],
             ["Entrepreneur: anak berjualan barang yang dibawa dari rumah pada hari pasar", "Explore Science: presentasi sains sederhana sesuai tema belajar",
              "Ekstrakurikuler: menggambar, drumband, taekwondo, coding, tari Bali", "KB dan TK sudah terakreditasi"],
             "paud", "Dua siswi PAUD memecahkan telur saat kegiatan memasak"),
            ("level", "sd", "Sekolah Dasar (SD)", "Kelas 1–6",
             "Masa SD membangun dasar akademik yang kuat sambil menumbuhkan kreativitas, kolaborasi, kepemimpinan, dan jiwa wirausaha.",
             [("Usia masuk", "6 tahun pada bulan Juli tahun ajaran berjalan"), ("Kelas", "Maksimal 28 siswa dengan 2 guru"), ("Jam belajar", "Senin–Kamis 07.30–15.00, Jumat 07.30–11.00 WITA")],
             ["Cinta tanah air dan ikut melestarikan budaya lokal", "Bahasa Inggris dan teknologi sebagai bekal sehari-hari", "Kelas tahfidz Al-Qur’an bagi yang berminat",
              "Ekstrakurikuler: pramuka, pencak silat, renang, futsal, paduan suara, musik, menggambar, tari daerah"],
             "sd", "Guru dan dua siswa mengamati globe di perpustakaan"),
            ("level", "smp", "Sekolah Menengah Pertama (SMP)", "Kelas 7–9",
             "Remaja belajar secara aktif dan kritis dengan beragam metode dan media, serta dibimbing bertahap menuju pribadi mandiri dan berintegritas.",
             [("Kelas", "Maksimal 25 siswa"), ("Jam belajar", "Senin–Kamis 07.30–16.30, Jumat 07.30–16.00 WITA")],
             ["Program khas: Best Leadership Program, Business Day, Super Camp, Outing Class", "Budaya membaca, narasi akademik, dan kajian Al-Qur’an berbasis proyek",
              "Kegiatan pengembangan diri dan kepedulian lingkungan", "Ekstrakurikuler: pramuka, pencak silat, panahan, jurnalistik, futsal, basket, robotik, fotografi & desain grafis, videografi, klub karya ilmiah, musik, memasak, paduan suara"],
             "smp", "Tiga siswa SMP belajar bersama menggunakan tablet"),
            ("photos", ["x3", "x9", "x20"]),
            ("cards", "Tahfidz Al-Qur’an", "Kelas alternatif bagi siswa yang ingin menghafal lebih cepat, diajarkan dengan metode Wafa.", [
                ("PAUD", "Target 1 juz"), ("SD", "Target 3 juz"), ("SMP", "Target 2 juz")]),
            ("note", "Jam belajar mengikuti informasi yang dipublikasikan sekolah dan dapat disesuaikan tiap tahun. Silakan konfirmasi jadwal terbaru kepada tim kami."),
        ]),
    facilities=dict(
        title="Fasilitas", meta_t="Fasilitas Mutiara School Bali, Jimbaran",
        meta_d="Ruang kelas ber-AC, perpustakaan, lab komputer dan bahasa, sport center, area bermain, kantin sehat, transportasi, dan katering di Mutiara School Bali.",
        intro="Lingkungan sekolah modern dan ramah anak di dekat Universitas Udayana, dirancang agar anak merasa aman, nyaman, dan leluasa bereksplorasi.",
        blocks=[
            ("split", "Ruang untuk belajar", ["Ruang kelas ber-AC didukung perpustakaan, lab komputer dan e-learning, lab bahasa, ruang multimedia, serta ruang musik. Wi-Fi tersedia di area belajar."], "x0",
             "Siswa SMP dan guru belajar bersama menggunakan laptop di kelas"),
            ("cards", "Yang tersedia di sekolah", "", [
                ("Belajar", "Learning center, ruang kelas ber-AC, perpustakaan, lab komputer dan e-learning, lab bahasa, ruang multimedia."),
                ("Seni dan ibadah", "Ruang musik, musala, dan ruang tahfidz."),
                ("Olahraga dan bermain", "Sport center dan lapangan olahraga, area bermain indoor dan outdoor."),
                ("Pendampingan dan kesehatan", "Ruang konseling, UKS, dan kantin sehat."),
                ("Kenyamanan harian", "Toko sekolah, area parkir, toilet bersih, dan Wi-Fi."),
                ("Aula pembelajaran", "Aula untuk pertemuan, kegiatan orang tua, dan acara sekolah.")]),
            ("photos", ["x5", "g3", "x13"]),
            ("split", "Transportasi dan katering", ["Layanan antar-jemput dan katering tersedia melalui koperasi sekolah. Orang tua mendaftar langsung ke koperasi, yang juga mengelola program tabungan siswa."], "g4",
             "Anak-anak bermain air di tepi kolam bersama pelatih renang"),
            ("cards", "Layanan online", "Sistem pendaftaran dan akademik sekolah berjalan secara daring.", [
                ("Pendaftaran online", "Mendaftar dari rumah melalui formulir pendaftaran."),
                ("Sistem akademik", "Orang tua dan siswa dapat memantau informasi akademik secara daring."),
                ("Pembayaran online", "Pembayaran sekolah dapat dilakukan melalui sistem pembayaran sekolah.")]),
        ]),
    gallery=dict(
        title="Galeri", meta_t="Galeri Foto Mutiara School Bali",
        meta_d="Foto keseharian di Mutiara School Bali: kelas, perpustakaan, pramuka, olahraga, dan kegiatan sekolah di Jimbaran.",
        intro="Momen dari ruang kelas, perpustakaan, lapangan, dan berbagai kegiatan sekolah.",
        blocks=[("gallery",), ("note", "Kegiatan terbaru kami dapat dilihat di Instagram dan YouTube. Tautannya ada di halaman Kontak.")]),
    admissions=dict(
        title="Pendaftaran", meta_t="Pendaftaran Siswa Baru 2027/2028 – Mutiara School Bali",
        meta_d="Cara mendaftar di Mutiara School Bali Tahun Pelajaran 2027/2028: langkah, syarat usia, dokumen, observasi, dan wawancara. Daftar lewat WhatsApp.",
        intro="Pendaftaran Tahun Pelajaran 2027/2028 dibuka untuk PAUD, SD, dan SMP. Siswa pindahan juga diterima.",
        blocks=[
            ("steps", "Alur pendaftaran", [
                ("Daftar online", "Isi formulir pendaftaran. Bisa juga datang ke sekolah dan tim kami akan membantu mengisinya."),
                ("Bayar biaya pendaftaran", "Biaya pendaftaran digunakan untuk proses seleksi dan observasi."),
                ("Lengkapi data", "Unggah data dan dokumen ananda secara online."),
                ("Observasi dan wawancara", "Dilaksanakan di sekolah: satu hari untuk PAUD dan SD, dua hari untuk SMP. Hasil diumumkan 2–3 hari kemudian.")]),
            ("photos", ["x2", "x8", "g6"]),
            ("cards", "Syarat masuk", "", [
                ("PAUD", "Usia 3 tahun untuk KB, 4 tahun untuk TK A, dan 5 tahun untuk TK B pada bulan Juli tahun ajaran berjalan."),
                ("SD", "Usia 6 tahun pada bulan Juli tahun ajaran berjalan, sehat jasmani dan rohani."),
                ("SMP", "Lulus SD/MI, memiliki NISN, serta lulus tes akademik dan wawancara.")]),
            ("list", "Dokumen yang disiapkan", "", [
                "Pas foto 3×4 latar merah, 1 lembar", "Fotokopi akta kelahiran", "Fotokopi kartu keluarga", "Fotokopi KTP orang tua/wali",
                "Khusus SMP: fotokopi rapor kelas 4–6 yang dilegalisasi dan surat keterangan sehat dari dokter"]),
            ("faq", "Pertanyaan yang sering muncul", [
                ("Berapa biayanya?", "Biaya berbeda tiap jenjang dan gelombang, jadi tidak kami cantumkan di sini. Kirim pesan WhatsApp dan tim kami akan mengirim rincian biaya terbaru."),
                ("Apakah biaya bisa dicicil?", "Bisa. Orang tua menandatangani surat kesanggupan di bagian keuangan."),
                ("Apakah menerima siswa pindahan?", "Ya, dari sekolah mana pun, selama persyaratan administrasi terpenuhi."),
                ("Bagaimana kalau berhalangan hadir saat wawancara?", "Pendaftaran dialihkan ke gelombang berikutnya."),
                ("Bisakah mendaftar untuk tahun ajaran berikutnya?", "Bisa. Daftar lewat formulir, lalu konfirmasi kepada kami melalui WhatsApp.")]),
        ]),
    contact=dict(
        title="Kontak", meta_t="Kontak Mutiara School Bali – Jimbaran, Bali",
        meta_d="Alamat, WhatsApp, email, jam layanan, dan peta Mutiara School Bali, Jl. Lingkar Timur Udayana No. 8, Jimbaran, Bali.",
        intro="Kami senang menjawab pertanyaan Ayah Bunda dan menyambut keluarga yang ingin berkunjung ke sekolah.",
        blocks=[("contact",)]),
)

# ------------------------------------------------------------------ ARAB
P["ar"] = dict(
    about=dict(
        title="من نحن", meta_t="عن مدرسة موتيارا بالي – التاريخ والرؤية والرسالة",
        meta_d="تعرّف على بداية مدرسة موتيارا بالي في جيمباران عام 2016، ورؤيتها ورسالتها، والقيم التي يقوم عليها تعليمها الأخلاقي.",
        intro="مدرسة في جيمباران انطلقت من قناعة بسيطة: الطفل الذكي يحتاج كذلك إلى خلق حسن.",
        blocks=[
            ("split", "كيف بدأنا", [
                "تأسست مدرسة موتيارا بالي في 2 مايو 2016 على يد ثمانية مؤسسين جمعهم همّ واحد. فقد لاحظوا تزايد حاجة أهالي جنوب كوتا إلى مدارس ذات جودة، وأقلقهم أن الدروس كثيراً ما تبدو بعيدة عن حياة الأطفال الواقعية.",
                "فكان الجواب مدرسة بمعلمين أكفاء ومنهج يكوّن أطفالاً أذكياء، مهذبين، يتطلعون إلى المستقبل. وبدأ بناء المبنى «أ» بعد وقت قصير من تأسيس المؤسسة رسمياً عام 2016.",
                "فُتح باب التسجيل في مارس 2017 وبدأت الدراسة في 6 أبريل 2017 بصفوف التعليم المبكر ثم المرحلة الابتدائية، وتلتها المرحلة المتوسطة مع نمو المدرسة."], "g3",
             "تلاميذ في الساحة وخلفهم مبنى مدرسة موتيارا"),
            ("facts", "النمو في البدايات", [("94", "طالباً في 2017/2018"), ("199", "طالباً في 2018/2019"), ("30 ← 51", "معلماً وموظفاً من 2017 إلى 2018")]),
            ("text", "لماذا «موتيارا»", ["موتيارا تعني اللؤلؤة. ويعبّر الاسم عن عزم المؤسسين على تقديم أفضل تعليم، وعن أملهم في أن يتخرج كل طالب بنتائج متميزة وخلق كريم. ويلخّص شعار المدرسة ذلك: ذكاء، أخلاق، رؤية."]),
            ("cards", "الرؤية والرسالة", "الرؤية: أن نكون مؤسسة تعليمية متميزة تُعِدّ جيلاً ذكياً، نبيل الأخلاق، ذا نظرة عالمية.", [
                ("مؤسسة محترفة", "إدارة المدرسة باحتراف ضمن نظام تعليمي محفّز."),
                ("تفوق علمي واجتماعي", "تكوين جيل متفوق أكاديمياً واجتماعياً على أساس القيم الدينية."),
                ("الشراكة", "التعاون مع جميع أطراف العملية التعليمية لتحقيق أهداف التعليم الوطني.")]),
            ("quote", "جاءت مدرسة موتيارا إلى جنوب كوتا خياراً تعليمياً محوره القيم الأخلاقية. نأمل أن ينشأ طلابنا جيلاً قوياً نافعاً قادراً على القيادة بكرامة، وندعو أولياء الأمور إلى أن يسيروا معنا بخطى واحدة.",
             "Lailatul Widayati, S.H., M.Pd.", "مديرة التعليم"),
        ]),
    programs=dict(
        title="البرامج والمراحل", meta_t="البرامج – التعليم المبكر والابتدائي والمتوسط | مدرسة موتيارا بالي",
        meta_d="التعليم المبكر والمرحلة الابتدائية والمتوسطة في مدرسة موتيارا بالي: المنهج، ساعات الدراسة، عدد الطلاب في الصف، الأنشطة والبرامج المميزة.",
        intro="ثلاث مراحل في بيئة واحدة، تجمع كل منها بين المنهج الوطني ومنهج B.E.S.T الخاص بموتيارا في نظام اليوم الدراسي الكامل.",
        blocks=[
            ("cards", "منهج B.E.S.T", "إلى جانب المنهج الوطني الذي يقيّم المعرفة والمهارة والموقف والسلوك، تسير كل مرحلة في أربعة اتجاهات.", [
                ("Berkarakter · الشخصية", "انضباط واستقلالية ونزاهة وحب للوطن وروح قيادية."),
                ("Edukatif · المعرفة", "سرعة في التعلم مع أفق واسع ورؤية وفضول."),
                ("Solutif · الحلول", "قدرة على حل المشكلات للنفس وللآخرين وللمجتمع."),
                ("Terampil · المهارة", "مهارات حياتية عملية.")]),
            ("level", "paud", "التعليم المبكر (PAUD)", "مجموعة اللعب، الروضة أ، الروضة ب",
             "يتعلم الصغار باللعب والاستكشاف والعادات الحسنة، باللغة الإندونيسية مع ممارسة الإنجليزية في الأنشطة اليومية.",
             [("سن القبول", "مجموعة اللعب 3، الروضة أ 4، الروضة ب 5 (في يوليو)"), ("الصف", "حتى 25 طفلاً مع معلمتين"),
              ("دوام الروضة", "الإثنين–الخميس 07:45–13:00، الجمعة 07:45–11:00"), ("دوام مجموعة اللعب", "الإثنين والأربعاء والجمعة 08:00–11:00")],
             ["ريادة الأعمال: يبيع الأطفال أشياء يحضرونها من البيت في يوم السوق", "استكشاف العلوم: عروض علمية مبسطة مرتبطة بموضوع التعلم",
              "الأنشطة: الرسم، فرقة الطبول، التايكوندو، البرمجة، الرقص البالي", "مجموعة اللعب والروضة حاصلتان على الاعتماد"],
             "paud", "أطفال التعليم المبكر في مدرسة موتيارا يشاركون في نشاط عملي"),
            ("level", "sd", "المرحلة الابتدائية (SD)", "الصفوف 1–6",
             "تبني سنوات الابتدائية أساساً أكاديمياً متيناً وتنمّي الإبداع والتعاون والقيادة وروح المبادرة.",
             [("سن القبول", "6 سنوات في يوليو من العام الدراسي"), ("الصف", "حتى 28 تلميذاً مع معلمَين"), ("الدوام", "الإثنين–الخميس 07:30–15:00، الجمعة 07:30–11:00")],
             ["حب الوطن والمشاركة في حفظ الثقافة المحلية", "الإنجليزية والتقنية أدوات يومية", "صف اختياري لتحفيظ القرآن الكريم",
              "الأنشطة: الكشافة، البنشاك سيلات، السباحة، كرة الصالات، الكورال، الموسيقى، الرسم، الرقص الشعبي"],
             "sd", "تلاميذ الابتدائية يقرؤون ويتأملون مجسّم الكرة الأرضية في المكتبة"),
            ("level", "smp", "المرحلة المتوسطة (SMP)", "الصفوف 7–9",
             "يتعلم الطلاب بنشاط وتفكير نقدي بطرائق ووسائل متنوعة، ويُرافَقون خطوة خطوة نحو الاستقلالية والنزاهة.",
             [("الصف", "حتى 25 طالباً"), ("الدوام", "الإثنين–الخميس 07:30–16:30، الجمعة 07:30–16:00")],
             ["برامج مميزة: Best Leadership Program، Business Day، Super Camp، Outing Class", "ثقافة القراءة والكتابة الأكاديمية ودراسة القرآن بالمشاريع",
              "أنشطة تطوير الذات والعناية بالبيئة", "الأنشطة: الكشافة، البنشاك سيلات، الرماية، الصحافة، كرة الصالات، كرة السلة، الروبوتات، التصوير والتصميم، الفيديو، النادي العلمي، الموسيقى، الطبخ، الكورال"],
             "smp", "طلاب المرحلة المتوسطة في نقاش جماعي"),
            ("cards", "تحفيظ القرآن الكريم", "صف بديل للطلاب الراغبين في الحفظ بوتيرة أسرع، يُدرَّس بطريقة «وفا».", [
                ("التعليم المبكر", "الهدف: جزء واحد"), ("الابتدائية", "الهدف: 3 أجزاء"), ("المتوسطة", "الهدف: جزءان")]),
            ("note", "ساعات الدوام بحسب المعلومات المنشورة من المدرسة وقد تُعدَّل كل عام. يُرجى التأكد من الجدول الحالي لدى فريقنا."),
        ]),
    facilities=dict(
        title="المرافق", meta_t="مرافق مدرسة موتيارا بالي، جيمباران",
        meta_d="صفوف مكيّفة، مكتبة، مختبرات حاسوب ولغات، مركز رياضي، ساحات لعب، مقصف صحي، نقل ووجبات في مدرسة موتيارا بالي.",
        intro="مدرسة حديثة وصديقة للطفل قرب جامعة أودايانا، صُمّمت ليشعر الأطفال بالأمان والراحة وحرية الاستكشاف.",
        blocks=[
            ("split", "أماكن للتعلم", ["الصفوف مكيّفة وتدعمها مكتبة ومختبر للحاسوب والتعلم الإلكتروني ومختبر لغات وقاعة وسائط متعددة وغرفة موسيقى. وتتوفر شبكة واي فاي في أماكن التعلم."], "x0",
             "معلمة ترافق تلاميذ الابتدائية أثناء التعلم بالحاسوب في الصف"),
            ("cards", "ما تجده في المدرسة", "", [
                ("التعلم", "مركز تعلم، صفوف مكيّفة، مكتبة، مختبر حاسوب وتعلم إلكتروني، مختبر لغات، قاعة وسائط متعددة."),
                ("الفنون والعبادة", "غرفة موسيقى، مصلّى، وغرفة خاصة بالتحفيظ."),
                ("الرياضة واللعب", "مركز رياضي وملعب، وساحات لعب داخلية وخارجية."),
                ("الرعاية والصحة", "غرفة إرشاد، عيادة مدرسية، ومقصف صحي."),
                ("راحة يومية", "متجر المدرسة، موقف سيارات، دورات مياه نظيفة، وواي فاي."),
                ("قاعة التعلم", "قاعة للاجتماعات ولقاءات أولياء الأمور وفعاليات المدرسة.")]),
            ("split", "النقل والوجبات", ["تتوفر خدمة النقل المدرسي والوجبات عبر تعاونية مدرسة موتيارا بالي. يسجّل أولياء الأمور مباشرة لدى التعاونية التي تدير كذلك برنامج ادخار الطلاب."], "g4",
             "أطفال في حصة سباحة مع المدربين"),
            ("cards", "خدمات إلكترونية", "تعمل أنظمة التسجيل والشؤون الأكاديمية في المدرسة عبر الإنترنت.", [
                ("التسجيل الإلكتروني", "سجّل من المنزل عبر استمارة التسجيل."),
                ("النظام الأكاديمي", "يتابع أولياء الأمور والطلاب المعلومات الأكاديمية عبر الإنترنت."),
                ("الدفع الإلكتروني", "يمكن سداد المدفوعات المدرسية عبر نظام الدفع الخاص بالمدرسة.")]),
        ]),
    gallery=dict(
        title="المعرض", meta_t="معرض صور مدرسة موتيارا بالي",
        meta_d="صور من الحياة اليومية في مدرسة موتيارا بالي: الصفوف، المكتبة، الكشافة، الرياضة والفعاليات المدرسية في جيمباران.",
        intro="لحظات من الصفوف والمكتبة والملعب وفعاليات المدرسة.",
        blocks=[("gallery",), ("note", "شاهد أحدث أنشطتنا على إنستغرام ويوتيوب. الروابط في صفحة «اتصل بنا».")]),
    admissions=dict(
        title="التسجيل", meta_t="التسجيل للعام 2027/2028 – مدرسة موتيارا بالي",
        meta_d="طريقة التسجيل في مدرسة موتيارا بالي للعام الدراسي 2027/2028: الخطوات، شروط القبول، الوثائق، الملاحظة والمقابلة. سجّل عبر واتساب.",
        intro="التسجيل للعام الدراسي 2027/2028 مفتوح للتعليم المبكر والابتدائية والمتوسطة، ونرحّب بالطلاب المنتقلين.",
        blocks=[
            ("steps", "خطوات التسجيل", [
                ("سجّل عبر الإنترنت", "املأ استمارة التسجيل، أو زُر المدرسة وسيساعدك فريقنا في تعبئتها."),
                ("ادفع رسوم التسجيل", "تغطي رسوم التسجيل إجراءات الاختيار والملاحظة."),
                ("أكمل البيانات", "ارفع بيانات الطفل ووثائقه عبر الإنترنت."),
                ("الملاحظة والمقابلة", "تُجرى في المدرسة: يوم واحد للتعليم المبكر والابتدائية، ويومان للمتوسطة. تُعلَن النتائج بعد يومين إلى ثلاثة أيام.")]),
            ("cards", "شروط القبول", "", [
                ("التعليم المبكر", "3 سنوات لمجموعة اللعب، 4 للروضة أ، 5 للروضة ب، في يوليو من العام الدراسي."),
                ("الابتدائية", "6 سنوات في يوليو من العام الدراسي، مع سلامة الصحة الجسدية والنفسية."),
                ("المتوسطة", "إتمام المرحلة الابتدائية، وامتلاك الرقم الوطني للطالب (NISN)، واجتياز الاختبار الأكاديمي والمقابلة.")]),
            ("list", "الوثائق المطلوبة", "", [
                "صورة شخصية 3×4 بخلفية حمراء", "نسخة من شهادة الميلاد", "نسخة من بطاقة العائلة", "نسخة من هوية ولي الأمر",
                "للمتوسطة فقط: نسخ مصدّقة من شهادات الصفوف 4–6 وشهادة صحية من الطبيب"]),
            ("faq", "أسئلة شائعة", [
                ("كم تبلغ الرسوم؟", "تختلف الرسوم بحسب المرحلة وفترة التسجيل، لذلك لا نذكرها هنا. راسلنا عبر واتساب وسيرسل فريقنا تفاصيل الرسوم الحالية."),
                ("هل يمكن الدفع بالتقسيط؟", "نعم، ويوقّع ولي الأمر تعهداً لدى القسم المالي."),
                ("هل تقبلون الطلاب المنتقلين؟", "نعم، من أي مدرسة، بشرط استيفاء المتطلبات الإدارية."),
                ("ماذا لو تعذّر الحضور في موعد المقابلة؟", "يُنقل الطلب إلى فترة التسجيل التالية."),
                ("هل يمكن التسجيل لعام دراسي لاحق؟", "نعم. سجّل عبر الاستمارة ثم أكّد لنا عبر واتساب.")]),
        ]),
    contact=dict(
        title="اتصل بنا", meta_t="اتصل بمدرسة موتيارا بالي – جيمباران، بالي",
        meta_d="العنوان، واتساب، البريد الإلكتروني، ساعات العمل والخريطة لمدرسة موتيارا بالي، Jl. Lingkar Timur Udayana No. 8، جيمباران، بالي.",
        intro="يسعدنا الرد على استفساراتكم واستقبال الأسر الراغبة في زيارة المدرسة.",
        blocks=[("contact",)]),
)
