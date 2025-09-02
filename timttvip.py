import time
import requests
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

API_URL = "https://nguyennamtien.shop/timtik.php?link={link}&key=toiyeuvietnam"

def print_header():
    print("=" * 60)
    print(Fore.CYAN + "🚀 AUTO TYM TIKTOK - Tool Tym Nè Cậu 💖".center(60))
    print("=" * 60)

def countdown(seconds):
    try:
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            print(Fore.YELLOW + f"⏳ Đang đếm ngược: {time_str}", end="\r")
            time.sleep(1)
        print(Fore.GREEN + "✅ Đã hết thời gian chờ! Tiếp tục buff...     ")
    except KeyboardInterrupt:
        print(Fore.RED + "\n⛔ Dừng tool theo yêu cầu người dùng.")
        exit()

def auto_tym(link):
    url = API_URL.format(link=link)
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        response = requests.get(url, timeout=20)
        data = response.json()

        print(f"\n{Fore.GREEN}📌 Thời gian chạy: {current_time}")
        print(f"{Fore.YELLOW}🔗 Link: {link}")

        if data.get("status") == "success":
            print(f"{Fore.BLUE}✅ {data.get('msg')}")
            print(f"🎬 Tiêu đề: {data.get('title')}")
            print(f"👤 Tác giả: {data.get('author')}")
            print(f"❤️ Lượt tim hiện tại: {data.get('likes_now')}")
            print(f"➕ Số tim đã buff: {data.get('sotim')}")
        else:
            print(f"{Fore.RED}❌ Lỗi từ API: {data.get('msg')}")

    except Exception as e:
        print(f"\n{Fore.RED}❌ Lỗi khi gửi yêu cầu tại {current_time}")
        print(f"{Fore.YELLOW}🔗 Link: {link}")
        print(f"{Fore.RED}⚠️ Chi tiết lỗi: {e}")

if __name__ == "__main__":
    print_header()
    print(Fore.MAGENTA + "🔗 Nhập link TikTok thứ 1:")
    link1 = input("➡️  ").strip()

    print(Fore.MAGENTA + "🔗 Nhập link TikTok thứ 2:")
    link2 = input("➡️  ").strip()

    if not link1 or not link2:
        print(Fore.RED + "⛔ Bạn phải nhập đủ 2 link. Thoát chương trình.")
        exit()

    print(f"\n🎯 Bắt đầu auto tym cho 2 video TikTok!\n")
    print("-" * 60)

    links = [link1, link2]

    while True:
        for link in links:
            auto_tym(link)
            print()
        countdown(300)  # 5 phút delay
        print("-" * 60)
