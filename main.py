from tkinter import *
from tkinter import messagebox

# ==================================================
# FUNGSI DIAGNOSA
# ==================================================
def diagnosa():

    visual = g1.get() + g2.get() + g3.get() + g4.get()
    auditori = g5.get() + g6.get() + g7.get() + g8.get()
    kinestetik = g9.get() + g10.get() + g11.get() + g12.get()

    if visual == 0 and auditori == 0 and kinestetik == 0:
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih minimal satu gejala!"
        )
        return

    # ==========================================
    # PERSENTASE
    # ==========================================
    persen_visual = (visual / 4) * 100
    persen_auditori = (auditori / 4) * 100
    persen_kinestetik = (kinestetik / 4) * 100

    # ==========================================
    # RULE BASE (IF THEN)
    # ==========================================
    if visual > auditori and visual > kinestetik:
        hasil = "VISUAL"

        saran = """
✓ Gunakan mind mapping ✓ Gunakan diagram dan gambar ✓ Belajar dengan infografis
✓ Menonton video pembelajaran ✓ Membuat catatan berwarna
"""

    elif auditori > visual and auditori > kinestetik:
        hasil = "AUDITORI"

        saran = """
✓ Berdiskusi dengan teman ✓ Mendengarkan podcast edukasi ✓ Rekam materi kuliah
✓ Membaca dengan suara keras ✓ Presentasi materi
"""

    elif kinestetik > visual and kinestetik > auditori:
        hasil = "KINESTETIK"

        saran = """
✓ Praktikum langsung ✓ Simulasi ✓ Project Based Learning 
✓ Belajar sambil praktik ✓ Eksperimen sederhana
"""

    else:
        # Jika nilai sama
        if visual == kinestetik and visual > auditori:
            hasil = "VISUAL dan KINESTETIK"

        elif visual == auditori and visual > kinestetik:
            hasil = "VISUAL dan AUDITORI"

        elif auditori == kinestetik and auditori > visual:
            hasil = "AUDITORI dan KINESTETIK"

        else:
            hasil = "SEIMBANG"

        saran = """
✓ Anda memiliki lebih dari satu gaya belajar dominan ✓ Kombinasikan beberapa metode belajar
✓ Gunakan pendekatan yang paling nyaman
"""

    # ==========================================
    # TAMPILKAN HASIL
    # ==========================================
    hasil_text.config(state="normal")
    hasil_text.delete(1.0, END)

    hasil_text.insert(
        END,
        f"""
HASIL DIAGNOSIS

Visual      : {visual}/4 ({persen_visual:.0f}%)
Auditori    : {auditori}/4 ({persen_auditori:.0f}%)
Kinestetik  : {kinestetik}/4 ({persen_kinestetik:.0f}%)

KESIMPULAN

Gaya Belajar Dominan :
{hasil}

REKOMENDASI BELAJAR
{saran}
"""
    )

    hasil_text.config(state="disabled")


# ==================================================
# RESET
# ==================================================
def reset():

    semua = [
        g1,g2,g3,g4,
        g5,g6,g7,g8,
        g9,g10,g11,g12
    ]

    for item in semua:
        item.set(0)

    hasil_text.config(state="normal")
    hasil_text.delete(1.0, END)
    hasil_text.config(state="disabled")


# ==================================================
# WINDOW
# ==================================================
root = Tk()
root.title("Sistem Pakar Penentuan Gaya Belajar Mahasiswa")

root.state("zoomed")
root.configure(bg="#EAF4FF")

# ==================================================
# JUDUL
# ==================================================
Label(
    root,
    text="SISTEM PAKAR PENENTUAN GAYA BELAJAR MAHASISWA",
    font=("Segoe UI",20,"bold"),
    bg="#EAF4FF",
    fg="#003366"
).pack(pady=15)

Label(
    root,
    text="Silakan pilih gejala yang sesuai dengan karakteristik diri Anda",
    font=("Segoe UI",11),
    bg="#EAF4FF"
).pack()

# ==================================================
# VARIABEL
# ==================================================
g1 = IntVar()
g2 = IntVar()
g3 = IntVar()
g4 = IntVar()

g5 = IntVar()
g6 = IntVar()
g7 = IntVar()
g8 = IntVar()

g9 = IntVar()
g10 = IntVar()
g11 = IntVar()
g12 = IntVar()

# ==================================================
# KNOWLEDGE BASE
# ==================================================
frame = LabelFrame(
    root,
    text="Knowledge Base (Basis Pengetahuan)",
    font=("Segoe UI",12,"bold"),
    bg="white",
    padx=20,
    pady=20
)

frame.pack(
    fill="x",
    padx=20,
    pady=15
)

# VISUAL
Label(
    frame,
    text="VISUAL",
    font=("Segoe UI",12,"bold"),
    fg="blue",
    bg="white"
).grid(row=0,column=0,sticky="w")

Checkbutton(frame,text="Suka belajar menggunakan gambar",variable=g1,bg="white").grid(row=1,column=0,sticky="w")
Checkbutton(frame,text="Mudah memahami diagram",variable=g2,bg="white").grid(row=2,column=0,sticky="w")
Checkbutton(frame,text="Suka menonton video pembelajaran",variable=g3,bg="white").grid(row=3,column=0,sticky="w")
Checkbutton(frame,text="Mudah mengingat warna",variable=g4,bg="white").grid(row=4,column=0,sticky="w")

# AUDITORI
Label(
    frame,
    text="AUDITORI",
    font=("Segoe UI",12,"bold"),
    fg="green",
    bg="white"
).grid(row=0,column=1,padx=80,sticky="w")

Checkbutton(frame,text="Mudah memahami penjelasan lisan",variable=g5,bg="white").grid(row=1,column=1,padx=80,sticky="w")
Checkbutton(frame,text="Suka berdiskusi",variable=g6,bg="white").grid(row=2,column=1,padx=80,sticky="w")
Checkbutton(frame,text="Mudah mengingat suara",variable=g7,bg="white").grid(row=3,column=1,padx=80,sticky="w")
Checkbutton(frame,text="Suka mendengarkan podcast",variable=g8,bg="white").grid(row=4,column=1,padx=80,sticky="w")

# KINESTETIK
Label(
    frame,
    text="KINESTETIK",
    font=("Segoe UI",12,"bold"),
    fg="red",
    bg="white"
).grid(row=0,column=2,sticky="w")

Checkbutton(frame,text="Suka praktik langsung",variable=g9,bg="white").grid(row=1,column=2,sticky="w")
Checkbutton(frame,text="Belajar sambil bergerak",variable=g10,bg="white").grid(row=2,column=2,sticky="w")
Checkbutton(frame,text="Cepat memahami saat mencoba sendiri",variable=g11,bg="white").grid(row=3,column=2,sticky="w")
Checkbutton(frame,text="Sulit diam dalam waktu lama",variable=g12,bg="white").grid(row=4,column=2,sticky="w")

# ==================================================
# TOMBOL
# ==================================================
frame_btn = Frame(root,bg="#EAF4FF")
frame_btn.pack(pady=10)

Button(
    frame_btn,
    text="PROSES DIAGNOSIS",
    width=20,
    font=("Segoe UI",11,"bold"),
    bg="#007ACC",
    fg="white",
    command=diagnosa
).grid(row=0,column=0,padx=10)

Button(
    frame_btn,
    text="RESET",
    width=15,
    font=("Segoe UI",11,"bold"),
    bg="#DC3545",
    fg="white",
    command=reset
).grid(row=0,column=1,padx=10)

# ==================================================
# JUDUL HASIL
# ==================================================
Label(
    root,
    text="HASIL DIAGNOSA",
    font=("Segoe UI",12,"bold"),
    bg="#EAF4FF",
    fg="black"
).pack(anchor="w", padx=20)

# ==================================================
# AREA HASIL
# ==================================================
frame_hasil = Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)

frame_hasil.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

scrollbar = Scrollbar(frame_hasil)
scrollbar.pack(side=RIGHT, fill=Y)

hasil_text = Text(
    frame_hasil,
    font=("Segoe UI",10),
    bg="white",
    fg="#003366",
    wrap=WORD,
    borderwidth=0,
    yscrollcommand=scrollbar.set
)

hasil_text.pack(
    fill=BOTH,
    expand=True,
    padx=10,
    pady=10
)

scrollbar.config(command=hasil_text.yview)

hasil_text.config(state="disabled")

# ==================================================
# FOOTER
# ==================================================
Label(
    root,
    text="Project UAS Artificial Intelligence - Sistem Pakar Gaya Belajar Mahasiswa",
    font=("Segoe UI",10),
    bg="#EAF4FF",
    fg="gray"
).pack(pady=5)

root.mainloop() 