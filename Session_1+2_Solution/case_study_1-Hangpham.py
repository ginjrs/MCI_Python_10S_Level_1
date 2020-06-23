print("Giá căn nhà dự án 1")
d = float(input())
r = float(input())
print("Dài = ", str(d))
print("Rộng = ", str(r))
s = round(float(d) * float(r),2)
print("Diện tích = " + str(s))
print("---")
print("Nhập Công thức tính tiền mua nhà từ diện tích và giá nhà đã cung cấp: ")
print("Nhập giá nhà mặt tiền Quận 9: ")
p_q9 = float(input())
print("Giá nhà mặt tiền Quận 9: " + str(p_q9) + " triệu đồng/m2")
price = s * float(p_q9)
print("Số tiền mua nhà: " + str(price) + " triệu đồng")
print("---")
print("Thời gian hoàn vốn: ")
print("Nhập thu nhập hàng tháng cho dự án 1")
income = input()
print("Thu nhập cho thuê hàng tháng: " + str(income) + " triệu đồng")
Ttháng = round(float(price) / float(income),2)
print("Thời gian hoàn vốn tính theo tháng: " + str(Ttháng) + " tháng")
Tnăm = round((int(price) / (int(income) * 12)), 0) 
print("Thời gian hoàn vốn tính theo năm: " + str(Tnăm) + "năm")

print("---")
print("Giá căn nhà dự án 2")
print("Nhập thu nhập hàng tháng cho dự án 2")
income2 = input()
print("Thu nhập hàng tháng cho dự án 2: " + str(income2) + " triệu đồng")
print("Nhập thời gian hoàn vốn dự tính")
Time2 = input()
print("Thời gian hoàn vốn dự tính: " + str(Time2) + " tháng")
price2 = round(float(Time2) * float(income2), 2)
print("Giá trị căn nhà từ dự án 2: " + str(price2) + " triệu đồng")

print("---")
print("So sánh thu nhập 2 dự án")
print("Nhập diện tích giả định S2: ")
S2 = input()
print("Diện tích nhà: " + str(S2) + " m2")
time3 = 144
print("Thời gian hoàn vốn: " + str(time3) + "tháng")
price1_new =  float(S2) * float(p_q9)
print("Giá nhà mặt tiền với diện tích 50m2: " + str(price1_new) + " triệu đồng")
print("Nhập giá hẻm Quận 9: ")
p_hq9 = float(input())
print("Giá nhà mặt tiền Quận 9: " + str(p_hq9) + " triệu đồng/m2")
price2_new = float(S2) * float(p_hq9)
print("Giá nhà hẻm với diện tích 50m2: " + str(price2_new) + " triệu đồng")
print("Thu nhập hằng tháng của từng căn")
income1_new = float(price1_new) / 144
income2_new = float(price2_new) / 144
print("Thu nhập hằng tháng của nhà mặt tiền: " + str(income1_new) + " triệu đồng")
print("Thu nhập hằng tháng của nhà trong hẻm: " + str(income2_new) + " triệu đồng")
Ratio = round(float(income1_new) / float(income2_new), 2)
print("Tỷ lệ chênh lệch từ dự án cho thuê mặt tiền so với nhà trong hẻm: " + str(Ratio) + " lần")
if Ratio > 1.5:
	print("Thu nhập hằng tháng từ căn nhà 1 bằng " + str(Ratio) + " lần thu nhập từ căn nhà 2")
else:
	print("Thu nhập hằng tháng từ căn nhà 1 bằng" + str(Ratio) + " lần thu nhập từ căn nhà 2")		
print("Nhập giá căn hộ và giá đất nền")
p_chq9 = float(input())
p_dnq9 = float(input())

dist9 = {
"Giá nhà mặt tiền (triệu đồng/m2) " : str(p_q9) ,
"Giá nhà hẻm (triệu đồng/m2) " : str(p_hq9) ,
"Giá căn hộ (triệu đồng/m2)" : str(p_chq9) ,
"Giá đất nền (triệu đồng/m2) " : str(p_dnq9)
}

print("---")
print(dist9["Giá đất nền (triệu đồng/m2) "])

print("Sửa giá nhà mặt tiền sau 7 năm")
dist9["Giá nhà mặt tiền (triệu đồng/m2) "] = float(p_chq9) * 3
print(dist9)
