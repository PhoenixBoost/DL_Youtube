import yt_dlp

def download_video(url):
    try:
        # ตัวเลือกสำหรับ yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # เลือกคุณภาพที่ดีที่สุดทั้งวีดีโอและเสียง
            'outtmpl': '%(title)s.%(ext)s',  # ตั้งชื่อไฟล์ที่ดาวน์โหลดตามชื่อวีดีโอ
        }

        # ดาวน์โหลดวีดีโอ
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("กำลังดาวน์โหลดวีดีโอที่มีคุณภาพสูงสุด...")
            ydl.download([url])
        
        print("ดาวน์โหลดเสร็จสิ้น!")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    video_url = input("กรุณาใส่ URL ของวีดีโอ YouTube ที่ต้องการดาวน์โหลด: ")
    download_video(video_url)
