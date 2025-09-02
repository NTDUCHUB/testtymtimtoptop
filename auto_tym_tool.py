import time
import requests
import argparse
from datetime import datetime

# URL API auto tym
API_URL = "https://nguyennamtien.shop/timtik.php?link={link}&key=toiyeuvietnam"

# Hàm gửi yêu cầu đến API
def auto_tym(link):
    url = API_URL.format(link=link)
    try:
        response = requests.get(url, timeout=20)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ KẾT QUẢ: {response.text}")
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ LỖI: {e}")

# Chương trình chính
def main():
    parser = argparse.ArgumentParser(description="🛠 Tool Auto Tym TikTok by Python")
    parser.add_argument("link", help="🔗 Link TikTok video cần buff tym")
    parser.add_argument("--delay", type=int, default=300, help="⏱ Thời gian chờ giữa mỗi lần buff (giây). Mặc định: 300")
    args = parser.parse_args()

    print(f"\n🚀 Đang chạy Auto Tym cho link: {args.link}")
    print(f"⏱ Sẽ lặp lại mỗi {args.delay} giây\n")

    while True:
        auto_tym(args.link)
        print("🕓 Chờ tiếp...\n")
        time.sleep(args.delay)

if __name__ == "__main__":
    main()
