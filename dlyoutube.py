import yt_dlp  #นำเข้าไลบรารีชื่อ yt_dlp เพื่อใช้ดาวน์โหลดวิดีโอจาก YouTube
def download_youtube_video(url, save_path="."): #ตั้งชื่อฟังก์ชันชื่อ download_youtube_video และมีการรับพารามิเตอร์ 2 ตัว
    ydl_opts = {      #กำหนดตัวเลือกให้กับ yt_dlp เช่น
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'best' #ดาวน์โหลดคุณภาพดีที่สุด
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  #สร้าง object YoutubeDL โดยใช้ options ที่เลือก ใช้ ydl.download([url]) เพื่อดาวน์โหลดวิดีโอจากลิงก์ที่ใส่มา
        ydl.download([url]) #ดาวน์โหลดวิดีโอจาก URL
video_url = input("Enter the YouTube video URL: ") # รับ URL จากผู้ใช้ผ่านทางและแสดงข้อความ "Enter the YouTube video URL: "

download_youtube_video(video_url, save_path=".") #เรียกใช้ฟังก์ชัน download_youtube_video 