import tkinter as tk
from tkinter import messagebox

class HealthcareGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Healthcare Quiz")
        self.root.geometry("600x450")
        self.root.configure(bg="#f0f8ff")
        
        self.score = 0
        self.current_index = 0
        self.is_redeem_phase = False
        
        # Original pool of situations
        self.all_situations = [
            {
                "id": 1,
                "text": "Situasi 1: Seorang rakan tiba-tiba jatuh pitam (pengsan) di pejabat.",
                "choices": ["Bawa pergi ke hospital dengan segera.", "Rehatkan sahaja dia di rumah."],
                "correct": 0,
                "feedback_correct": "Tindakan pantas menyelamatkan nyawa.",
                "feedback_wrong": "Bahaya kerana kita tidak tahu punca sebenar."
            },
            {
                "id": 2,
                "text": "Situasi 2: Jari tangan melecur sedikit kerana terkena air panas sewaktu membancuh air.",
                "choices": ["Sapu ubat gigi tebal-tebal pada bahagian yang melecur.", "Alirkan air paip sejuk pada luka melecur dan sapu krim ubat."],
                "correct": 1,
                "feedback_correct": "Air sejuk mengurangkan haba dan cegah bengkak.",
                "feedback_wrong": "Ubat gigi boleh memerangkap haba dan sebabkan jangkitan."
            },
            {
                "id": 3,
                "text": "Situasi 3: Mangsa Tercekik Makanan",
                "choices": ["Biarkan mangsa terus batuk tanpa berbuat apa apa.", "Berikan hentakan belakang sebanyak 5 kali."],
                "correct": 1,
                "feedback_correct": "Dapat memberikan tekanan untuk mengeluarkan objek.",
                "feedback_wrong": "Objek akan terus tersangkut dan menyekat oksigen ke peparu."
            },
            {
                "id": 4,
                "text": "Situasi 4: Terasa sesak nafas secara tiba-tiba dan sukar bernafas dengan normal.",
                "choices": ["Cari penyedut inhaler kecemasan atau dapatkan bantuan oksigen segera.", "Paksa diri berlari cepat untuk buka saluran pernafasan."],
                "correct": 0,
                "feedback_correct": "Rawatan awal oksigen/inhaler selamatkan pesakit sesak nafas.",
                "feedback_wrong": "Aktiviti berat akan memburukkan lagi keadaan."
            },
            {
                "id": 5,
                "text": "Situasi 5: Seorang rakan anda terseliuh kaki ketika berlari semasa aktiviti sukan.",
                "choices": ["Rehatkan kaki yang cedera, letakkan ais pada kawasan sakit dan elakkan memberi tekanan.", "Urut kaki yang terseliuh dengan kuat dan teruskan berlari."],
                "correct": 0,
                "feedback_correct": "Kaki yang terseliuh perlu direhatkan dan diberikan rawatan awal RICE.",
                "feedback_wrong": "Mengurut dengan kuat atau meneruskan aktiviti boleh memburukkan kecederaan."
            },
            {
                "id": 6,
                "text": "Situasi 6: Seorang rakan terjatuh ketika bermain bola sepak dan mengalami luka kecil pada lutut.",
                "choices": ["Bersihkan luka menggunakan ubat antiseptik atau pencuci luka, kemudian letakkan hansaplast.", "Terus letakkan hansaplast tanpa membersihkan luka terlebih dahulu."],
                "correct": 0,
                "feedback_correct": "Luka perlu dibersihkan terlebih dahulu untuk menghalang risiko jangkitan kuman.",
                "feedback_wrong": "Jika terus menutup luka tanpa membersihkannya, kotoran akan melambatkan penyembuhan."
            },
            {
                "id": 7,
                "text": "Situasi 7: Seseorang mengalami pendarahan hidung (hidung berdarah) secara tiba-tiba.",
                "choices": ["Duduk tegak, tundukkan kepala ke depan sedikit, dan picit bahagian lembut hidung.", "Dongakkan kepala ke belakang dan baring secara rata."],
                "correct": 0,
                "feedback_correct": "Menunduk ke depan menghalang darah daripada masuk ke dalam kerongkong atau peparu.",
                "feedback_wrong": "Mendongakkan kepala boleh menyebabkan darah mengalir ke kerongkong dan menyebabkan tersedak."
            }
        ]
        
        # Active list of questions for the current phase
        self.active_situations = list(self.all_situations)
        self.wrong_situations = []
        
        self.setup_ui()
        self.load_situation()

    def setup_ui(self):
        self.title_label = tk.Label(self.root, text="=== SMART HEALTHCARE QUIZ ===", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#2c3e50")
        self.title_label.pack(pady=15)
        
        self.phase_label = tk.Label(self.root, text="FASA UTAMA", font=("Arial", 10, "bold"), bg="#2ecc71", fg="white", padx=10, pady=2)
        self.phase_label.pack(pady=5)
        
        self.situation_label = tk.Label(self.root, text="", font=("Arial", 11, "bold"), bg="#f0f8ff", fg="#34495e", wraplength=500, justify="center")
        self.situation_label.pack(pady=15)
        
        self.btn_choice1 = tk.Button(self.root, text="", font=("Arial", 10), width=50, height=2, wrap=450, bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", command=lambda: self.check_answer(0))
        self.btn_choice1.pack(pady=10)
        
        self.btn_choice2 = tk.Button(self.root, text="", font=("Arial", 10), width=50, height=2, wrap=450, bg="#e67e22", fg="white", activebackground="#d35400", activeforeground="white", command=lambda: self.check_answer(1))
        self.btn_choice2.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="", font=("Arial", 10, "italic"), bg="#f0f8ff", fg="#7f8c8d")
        self.score_label.pack(side="bottom", pady=15)

    def load_situation(self):
        if self.current_index < len(self.active_situations):
            sit = self.active_situations[self.current_index]
            self.situation_label.config(text=sit["text"])
            self.btn_choice1.config(text=sit["choices"][0])
            self.btn_choice2.config(text=sit["choices"][1])
            
            if not self.is_redeem_phase:
                self.score_label.config(text=f"Markah: {self.score} / {len(self.all_situations)}")
            else:
                self.score_label.config(text=f"Fasa Penebusan: Sila betulkan {len(self.active_situations) - self.current_index} soalan baki.")
        else:
            self.handle_phase_end()

    def check_answer(self, chosen_index):
        sit = self.active_situations[self.current_index]
        
        if chosen_index == sit["correct"]:
            if not self.is_redeem_phase:
                self.score += 1
            else:
                # If they fix it in redemption phase, add to score
                self.score += 1
            messagebox.showinfo("BETUL!", f"-> [BETUL!] {sit['feedback_correct']}")
        else:
            messagebox.showerror("SALAH!", f"-> [SALAH!] {sit['feedback_wrong']}")
            # Keep track of wrong answers only during the first pass
            if not self.is_redeem_phase:
                self.wrong_situations.append(sit)
                
        self.current_index += 1
        self.load_situation()

    def handle_phase_end(self):
        if not self.is_redeem_phase:
            if len(self.wrong_situations) > 0:
                messagebox.showinfo("Fasa Penebusan!", f"Pusingan pertama tamat! Markah semasa: {self.score} / {len(self.all_situations)}.\n\nAnda tersalah jawab {len(self.wrong_situations)} soalan. Anda diberi peluang kedua untuk membetulkannya sekarang!")
                # Switch to redemption phase
                self.is_redeem_phase = True
                self.active_situations = list(self.wrong_situations)
                self.current_index = 0
                self.phase_label.config(text="FASA PENEBUSAN (REDEEM)", bg="#e74c3c")
                self.load_situation()
            else:
                self.show_final_results()
        else:
            self.show_final_results()

    def show_final_results(self):
        total = len(self.all_situations)
        msg = f"PERMAINAN TAMAT!\nMarkah Akhir: {self.score} / {total}\n\n"
        
        if self.score == total:
            msg += "Tahniah! Anda berjaya menjawab semua dengan betul (termasuk penebusan)!"
        else:
            msg += "Bagus! Pengetahuan kesihatan kecemasan anda telah meningkat!"
            
        messagebox.showinfo("Keputusan Akhir", msg)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HealthcareGame(root)
    root.mainloop()
