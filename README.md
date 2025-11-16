# 🌍 AI Travel Planner - Trợ Lý Du Lịch Thông Minh

## 📖 Giới Thiệu

**AI Travel Planner** là ứng dụng lập kế hoạch du lịch thông minh sử dụng AI (OpenAI GPT-5-mini) để:
- 🗣️ **Trò chuyện tự nhiên** - Không cần menu phức tạp
- 🎯 **Gợi ý thông minh** - Dựa trên sở thích của bạn
- 🌤️ **Kiểm tra thời tiết** - Tư vấn thời điểm đi tốt nhất
- 📅 **Tạo kế hoạch chi tiết** - Lịch trình từng ngày, ước tính chi phí

## ✨ Tính Năng

### 🔐 Bảo Mật API Key
- Nhập API key **trực tiếp** khi khởi động
- **Không lưu** vào file (100% an toàn)
- Validate key ngay lập tức

### 🤖 AI-Driven Planning Flow

```
Bước 1: Chia sẻ sở thích
├─ Bạn muốn đi đâu?
├─ Ngân sách thế nào? (budget/moderate/luxury)
├─ Thích gì? (biển/núi/văn hóa/ẩm thực/phiêu lưu)
└─ Loại chuyến đi? (nghỉ dưỡng/khám phá/mạo hiểm)

        ↓

Bước 2: AI gợi ý điểm đến
├─ 2-3 điểm đến phù hợp nhất
├─ Lý do phù hợp với bạn
├─ Ước tính chi phí
└─ Đặc điểm nổi bật

        ↓

Bước 3: Chọn điểm đến → AI gợi ý activities
├─ Top attractions
├─ Hoạt động vui chơi
├─ Ẩm thực địa phương
├─ Trải nghiệm độc đáo
└─ Chi phí từng activity

        ↓

Bước 4: Nhập ngày đi → AI check thời tiết
├─ Thời tiết dự báo
├─ Nhiệt độ trung bình
├─ Mùa du lịch tốt nhất
├─ Lời khuyên về quần áo
└─ Cảnh báo nếu cần (mưa bão, quá nóng/lạnh)

        ↓

Bước 5: AI tạo kế hoạch chi tiết
├─ Lịch trình từng ngày
├─ Thời gian cho mỗi activity
├─ Di chuyển giữa các địa điểm
├─ Gợi ý nhà hàng
├─ Tổng chi phí dự kiến
└─ Tips & tricks
```

## 🚀 Cài Đặt & Chạy

### 1. Prerequisites
- Python 3.10+
- Virtual environment (venv)

### 2. Cài Đặt Dependencies

```bash
# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install packages
pip install openai colorama
```

### 3. Lấy API Key

**Bước 1:** Truy cập https://aiportalapi.stu-platform.live/jpe

**Bước 2:** Đăng nhập/Đăng ký tài khoản

**Bước 3:** Tạo API key mới (key sẽ bắt đầu bằng `sk-`)

**Bước 4:** Copy key (sẽ dùng khi chạy app)

### 4. Chạy Ứng Dụng

```bash
python main_ai.py
```

## 📝 Hướng Dẫn Sử Dụng

### Khi Khởi Động

```
===============================================================
✈️   AI Travel Planner - Your Intelligent Travel Assistant   🌍
===============================================================

🔑 API Key Setup
─────────────────────────────────────────────────────────────
To use this application, you need an OpenAI API key.
Get your key from: https://aiportalapi.stu-platform.live/jpe
─────────────────────────────────────────────────────────────

Enter your API key (hidden): [nhập key ở đây]
```

**Lưu ý:** Key của bạn sẽ **ẩn** khi nhập (giống password)

### Sau Khi Validate Key

```
✅ API key validated successfully!

─────────────────────────────────────────────────────────────
Main Menu:
─────────────────────────────────────────────────────────────
1. 🚀 Start Planning (Chat with AI)
2. 🚪 Exit
─────────────────────────────────────────────────────────────

Enter your choice:
```

### Chọn "1" - Bắt Đầu Planning

AI sẽ chào hỏi và hướng dẫn bạn:

```
🤖 AI Assistant: Hi! I'm your travel planning assistant. 
I'd love to help you plan your next adventure! 

Could you tell me:
- Where are you thinking of traveling? (or what kind of place interests you?)
- What's your budget level? (budget-friendly / moderate / luxury)
- What are you interested in? (beaches, culture, food, adventure, etc.)

You: Tôi muốn đi du lịch ở Đà Nẵng, thích biển và ăn hải sản, budget vừa phải

🤖 AI Assistant: Tuyệt vời! Đà Nẵng là lựa chọn tuyệt vời cho bạn!

🏖️ TẠI SAO PHÙ HỢP:
• Bãi biển đẹp: Mỹ Khê, Non Nước (top beaches châu Á)
• Hải sản tươi ngon, giá cả hợp lý (100k-500k/người)
• Nhiều quán ăn ven biển
• Chi phí vừa phải (budget-friendly)

💰 ESTIMATED BUDGET (3-4 ngày):
• Hotel: 500k-1M/đêm (beachfront)
• Food: 200k-400k/ngày
• Activities: 200k-500k/ngày
• Total: ~3-5 triệu/người

🎯 TOP ACTIVITIES TÔI GỢI Ý:
1. Bãi biển Mỹ Khê (FREE)
   - Bơi lội, tắm biển
   - Ngắm hoàng hôn
   
2. Chợ Hải Sản Thọ Quang (200k-500k)
   - Chọn hải sản tươi sống
   - Chế biến tại chỗ
   
3. Cầu Rồng (FREE)
   - Xem rồng phun lửa (9PM cuối tuần)
   - Check-in sống ảo

4. Bà Nà Hills (700k)
   - Cáp treo ngắm cảnh
   - Cầu Vàng iconic

Bạn muốn đi khi nào? Tôi sẽ check thời tiết và tư vấn nhé!

You: Tháng 12 này có ổn không?

🤖 AI Assistant: 🌤️ THỜI TIẾT THÁNG 12 Ở ĐÀ NẴNG:

✅ KHẢ NĂNG ĐI: Khá tốt, nhưng cần lưu ý!

🌡️ NHIỆT ĐỘ:
• Trung bình: 20-25°C
• Ban ngày: 24-26°C (dễ chịu)
• Ban đêm: 19-22°C (mát mẻ)

🌧️ THỜI TIẾT:
• Cuối mùa mưa (Oct-Nov)
• Tháng 12: Ít mưa hơn, khô ráo hơn
• Trời có thể nhiều mây
• Nước biển hơi lạnh (22-24°C)

👕 NÊN MANG:
• Áo dài tay/khoác mỏng (buổi tối)
• Quần short/váy (ban ngày)
• Áo mưa (đề phòng)

⚠️ LƯU Ý:
• Sóng có thể to hơn (cẩn thận khi tắm biển)
• Ít nắng hơn các tháng 3-8
• Giá khách sạn tốt hơn (off-season)

💡 GỢI Ý: Nếu có thể, tháng 3-5 là BEST TIME cho Đà Nẵng 
(nắng đẹp, biển êm, thời tiết lý tưởng)

Bạn vẫn muốn đi tháng 12, hay muốn xem tháng khác?

You: OK luôn, tôi đi 3 ngày 2 đêm từ 15-17/12

🤖 AI Assistant: 🗓️ PERFECT! Để tôi tạo itinerary chi tiết cho bạn:

📅 KẾ HOẠCH 3 NGÀY 2 ĐÊM ĐÀ NẴNG (15-17/12)

─────────────────────────────────────────────────
🌅 NGÀY 1 (15/12) - Arrival & Beach Day
─────────────────────────────────────────────────
Sáng:
• Check-in hotel (Khu vực Mỹ Khê)
• Nghỉ ngơi sau chuyến đi

Trưa (12:00):
• Ăn trưa: Quán Mỹ Khê (150k)
  → Cơm hải sản, canh chua tôm

Chiều (14:00-17:00):
• Bãi biển Mỹ Khê (FREE)
  → Tắm biển, tắm nắng, chụp ảnh
  
Tối (18:00):
• Cầu Rồng (FREE)
  → Xem cầu phun lửa 9PM (Thứ 7)
  
• Dinner: Bé Mặn Seafood (400k/2 người)
  → Tôm hùm nướng, sò huyết

💰 Chi phí ngày 1: ~550k

─────────────────────────────────────────────────
🏔️ NGÀY 2 (16/12) - Bà Nà Hills
─────────────────────────────────────────────────
Sáng (7:00):
• Khởi hành đi Bà Nà Hills
• Mua vé: 700k (cáp treo + vui chơi)

8:00-17:00:
• Cáp treo ngắm cảnh (longest cable car!)
• Cầu Vàng (Golden Bridge)
• Làng Pháp cổ
• Vườn hoa Le Jardin D'Amour
• Lunch tại Bà Nà (250k/người buffet)

Tối (19:00):
• Về khách sạn nghỉ ngơi
• Dinner gần hotel (200k)

💰 Chi phí ngày 2: ~1,150k

─────────────────────────────────────────────────
🍤 NGÀY 3 (17/12) - Local Experience & Departure
─────────────────────────────────────────────────
Sáng (7:00):
• Chợ Hải Sản Thọ Quang
  → Chọn hải sản tươi sống
  → Chế biến tại quán (300k-500k)

Trưa (11:00):
• Check-out hotel
• Ghé Cửa hàng đặc sản mua quà

Chiều:
• Ra sân bay/ga tàu về

💰 Chi phí ngày 3: ~400k

═════════════════════════════════════════════════
💵 TỔNG CHI PHÍ DỰ KIẾN:
═════════════════════════════════════════════════
• Accommodation: 1,000k (500k x 2 đêm)
• Food: 1,100k
• Activities: 700k (Bà Nà)
• Transport local: 300k (taxi/Grab)
• Shopping: 500k (souvenirs)
─────────────────────────────────────────────────
TOTAL: ~3,600,000 VND/người

═════════════════════════════════════════════════
✈️ TIPS & RECOMMENDATIONS:
═════════════════════════════════════════════════
1. Book hotel trước (Mỹ Khê beach area)
2. Mang áo khoác (Bà Nà lạnh 15-18°C)
3. Đặt Grab thay vì taxi (rẻ + an toàn hơn)
4. Mua vé Bà Nà online (rẻ hơn 50k)
5. Ăn hải sản tại Thọ Quang (fresh & cheap)

═════════════════════════════════════════════════

Bạn muốn điều chỉnh gì không? Hoặc cần thêm thông tin gì? 😊
```

## 🎯 Ví Dụ Conversations

### Example 1: Không biết đi đâu

```
You: Tôi muốn đi du lịch nhưng chưa biết đi đâu, thích biển và ăn uống

🤖 AI: Based on your preferences (beach + food), I suggest:

1. **Đà Nẵng, Vietnam** 🇻🇳
   - Beautiful beaches (Mỹ Khê)
   - Amazing seafood
   - Budget-friendly (3-5M for 3 days)
   
2. **Phuket, Thailand** 🇹🇭
   - Stunning beaches (Patong, Kata)
   - Street food + seafood
   - Moderate budget (10-15M for 3 days)
   
3. **Bali, Indonesia** 🇮🇩
   - Beach paradise
   - Diverse cuisine
   - Moderate (8-12M for 3 days)

Which interests you most?
```

### Example 2: Budget thấp

```
You: Budget 2-3 triệu, đi gần Việt Nam, thích văn hóa

🤖 AI: Perfect! For 2-3M budget, nearby cultural destinations:

1. **Chiang Mai, Thailand** 🇹🇭
   - 300+ temples
   - Night markets
   - 2.5M for 3 days (flight + hotel + food)
   
2. **Luang Prabang, Laos** 🇱🇦
   - UNESCO heritage town
   - Buddhist temples
   - 2M for 3 days (very cheap!)
   
3. **Hội An, Vietnam** 🇻🇳
   - Ancient town
   - Japanese bridge
   - 2M for 3 days (local)

Tell me which one you like!
```

## 💡 Tips & Best Practices

### ✅ Nên:
- Chia sẻ chi tiết sở thích (AI sẽ gợi ý chính xác hơn)
- Hỏi về thời tiết trước khi chốt ngày
- Yêu cầu AI ước tính chi phí chi tiết
- Hỏi tips & tricks từ AI

### ❌ Không nên:
- Chia sẻ API key với người khác
- Để terminal mở khi không dùng
- Quên hỏi về thời tiết/mùa du lịch

## 🔒 Bảo Mật

### API Key:
- ✅ Nhập bằng tay mỗi lần chạy
- ✅ Ẩn khi nhập (hidden input)
- ✅ Chỉ lưu trong memory (không file)
- ✅ Validate ngay lập tức
- ✅ Tự động xóa khi thoát app

### Dữ Liệu:
- ✅ Conversation history chỉ trong session
- ✅ Không lưu thông tin cá nhân
- ✅ Reset khi thoát chat

## 🛠️ Troubleshooting

### Lỗi: "Invalid key format"
**Nguyên nhân:** Key không đúng format
**Giải pháp:** Key phải bắt đầu bằng `sk-`

### Lỗi: "Authentication Error"
**Nguyên nhân:** Key không hợp lệ hoặc hết hạn
**Giải pháp:** 
1. Kiểm tra lại key
2. Tạo key mới từ portal
3. Thử lại

### Lỗi: "Connection timeout"
**Nguyên nhân:** Mạng chậm hoặc API server busy
**Giải pháp:**
1. Kiểm tra kết nối internet
2. Thử lại sau vài giây
3. Khởi động lại app

## 📊 So Sánh Phiên Bản

| Feature | Old Version (main.py) | New Version (main_ai.py) |
|---------|----------------------|--------------------------|
| API Key | Lưu trong .env | Nhập bằng tay (secure) |
| Data | Mock data cố định | AI generate dynamic |
| Menu | 6 options phức tạp | 2 options đơn giản |
| Flow | Rigid (chọn theo menu) | Natural conversation |
| Weather | Không có | AI check & advise |
| Planning | Manual selection | AI-guided step-by-step |
| Flexibility | Thấp | Cao (chat tự nhiên) |

## 🚀 Tính Năng Trong Tương Lai

- [ ] Multi-language support (EN/VI auto-detect)
- [ ] Export itinerary to PDF
- [ ] Real-time flight/hotel price checking
- [ ] Currency conversion
- [ ] Budget tracking
- [ ] Collaborative planning (multi-user)
- [ ] Save/load past itineraries
- [ ] Voice input support

## 📞 Support

Có câu hỏi hoặc vấn đề? 
- Kiểm tra phần Troubleshooting ở trên
- Đọc kỹ error message (AI thường đưa hints)

## 📄 License

MIT License - Free to use and modify

---

**Made with ❤️ using OpenAI GPT-5-mini**

Happy Travels! 🌍✈️🎒
#   a i c o u r s e - g r o u b 7  
 