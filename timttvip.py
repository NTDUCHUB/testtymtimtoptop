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

def auto_tym(link, total_tim):
    url = API_URL.format(link=link)
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        response = requests.get(url, timeout=20)
        data = response.json()

        print(f"\n{Fore.GREEN}📌 Thời gian chạy: {current_time}")
        print(f"{Fore.YELLOW}🔗 Link: {link}")

        if data.get("status") == "success":
            new_tim = data.get('sotim', 0)
            total_tim += new_tim

            print(f"{Fore.BLUE}✅ {data.get('msg')}")
            print(f"🎬 Tiêu đề: {data.get('title')}")
            print(f"👤 Tác giả: {data.get('author')}")
            print(f"❤️ Lượt tim hiện tại: {data.get('likes_now')}")
            print(f"➕ Số tim đã buff lần này: {new_tim}")
            print(f"{Fore.MAGENTA}➕ Tổng số tim đã buff: {total_tim}")
            return total_tim
        else:
            print(f"{Fore.RED}❌ Lỗi từ API: {data.get('msg')}")
            return total_tim

    except Exception as e:
        print(f"\n{Fore.RED}❌ Lỗi khi gửi yêu cầu tại {current_time}")
        print(f"{Fore.YELLOW}🔗 Link: {link}")
        print(f"{Fore.RED}⚠️ Chi tiết lỗi: {e}")
        return total_tim

if __name__ == "__main__":
    print_header()
    print(Fore.MAGENTA + "🔗 Nhập link TikTok:")
    link = input("➡️  ").strip()

    if not link:
        print(Fore.RED + "⛔ Bạn phải nhập link. Thoát chương trình.")
        exit()

    print(f"\n🎯 Bắt đầu auto tym cho video TikTok!\n")
    print("-" * 60)

    total_tim = 0

    while True:
        total_tim = auto_tym(link, total_tim)
        print()
        countdown(300)  # 5 phút delay
        print("-" * 60)
