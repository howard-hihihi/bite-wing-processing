original_img : 原圖。
img_025 : 把圖片分成四等分，各自使用中值濾波器減少噪聲，再各自使用 CLAHE。
img_050 : 上個步驟的 1、2 合併(5)，3、4 合併(6)，5、6 ，再各自使用 CLAHE。
img_100 : 上個步驟的 5、6 合併(7)，使用 CLAHE。
average_img : 把 img_050 和 original_img 的每個像素做平均。
