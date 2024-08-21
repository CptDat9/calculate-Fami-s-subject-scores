<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&center=true&vCenter=true&random=false&width=450&lines=Tính+Điểm+Học+Phần+Toán+Cao+Cấp+Fami" alt="Typing SVG" /></a>
</p>
<div align="center">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/CptDat9/calculate-Fami-s-subject-scores?labelColor=7AA2E3&color=97E7E1">
</div>

## Mô tả

Chương trình này được thiết kế để tính điểm học phần (DHP) cho sinh viên dựa trên các thành phần điểm: điểm kiểm tra (KT1, KT2), điểm tham gia (TP), và điểm thi cuối kỳ (ĐTCK). Chương trình áp dụng quy tắc làm tròn điểm và kiểm tra điều kiện trượt môn dựa trên điểm học phần.

## Cách sử dụng

1. Chương trình sẽ yêu cầu người dùng nhập các thành phần điểm như sau:
    - **KT1:** Điểm kiểm tra lần 1 (0 đến 15).
    - **KT2:** Điểm kiểm tra lần 2 (0 đến 15).
    - **TP:** Điểm tham gia (trong khoảng từ -1 đến 1).
    - **ĐTCK:** Điểm thi cuối kỳ (0 đến 10).

2. Chương trình sẽ tính điểm quá trình (ĐQT) và điểm học phần (DHP) theo công thức đã cho, áp dụng quy tắc làm tròn đến 0.5.

3. Chương trình sẽ kiểm tra các điều kiện trượt môn và thông báo kết quả (trượt hay qua môn) dựa trên ĐHP.

## Công thức tính toán

- **ĐKTĐK:**
  
 ![image](https://github.com/user-attachments/assets/18097213-7c83-4604-b52b-4ddb42d04b41)


- **ĐQT:**
  
![image](https://github.com/user-attachments/assets/1af08362-2a2f-4999-aac4-14193b46dedd)

  
- **DHP:**
  

![image](https://github.com/user-attachments/assets/de04288f-29b3-4c2a-b51c-2097ca340431)


## Kiểm tra điều kiện trượt môn

- Nếu `DHP < 4`, sinh viên trượt môn.
- Nếu `DTCK < 3`, sinh viên cũng trượt môn.

## Yêu cầu hệ thống

- Python 3.x.

## Hướng dẫn cài đặt và chạy chương trình

1. Tải mã nguồn chương trình về máy.
2. Đảm bảo đã cài đặt Python 3.x.
3. Chạy chương trình bằng lệnh sau trong terminal hoặc command prompt:

   ```bash
   python tinh_dhp.py
4. Nhập các giá trị khi được yêu cầu và nhận kết quả từ chương trình.

