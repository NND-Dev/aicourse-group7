# 🌍 AI Travel Planner

Ứng dụng AI giúp lập kế hoạch du lịch thông minh - tự động gợi ý điểm đến, hoạt động, kiểm tra thời tiết và tạo lịch trình chi tiết.

## ✨ Tính năng

- 🤖 **Chat với AI**: Trò chuyện tự nhiên để plan chuyến đi
- 🎯 **Gợi ý thông minh**: AI đề xuất điểm đến phù hợp với sở thích
- 🌤️ **Kiểm tra thời tiết**: Tư vấn thời gian tốt nhất để đi
- 📅 **Lịch trình chi tiết**: Tạo kế hoạch đầy đủ từ A-Z

## 🚀 Cách chạy

### 1. Cài đặt

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Cài dependencies
pip install -r requirements.txt
```

### 2. Chạy ứng dụng

```bash
python main.py
python main1.py
python main2.py
```

### 3. Sử dụng

1. Nhập **API key** khi được yêu cầu (lấy từ: https://aiportalapi.stu-platform.live/jpe)
2. Chọn **"Start Planning"** từ menu
3. Chat với AI về chuyến đi của bạn
4. AI sẽ hướng dẫn từng bước: sở thích → điểm đến → hoạt động → lịch trình

## 📦 Dependencies

- Python 3.8+
- openai==1.3.0
- httpx==0.25.2
- colorama==0.4.6

## 🎯 Demo

```
You: Tôi muốn đi biển, thích ăn hải sản
AI: Đà Nẵng là lựa chọn tuyệt vời! Bãi biển đẹp, hải sản tươi ngon...

You: Nên đi tháng mấy?
AI: Tháng 3-8 là thời gian lý tưởng, thời tiết nắng đẹp...
```

## 📝 License

MIT License

---

**Made with ❤️ by Group 7**
